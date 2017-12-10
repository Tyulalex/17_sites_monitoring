import argparse
import requests
import whois
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path',
        help='path to file with urls')
    return parser.parse_args()


def load_urls4check(path):
    with open(path) as url_file:
        return url_file.read().splitlines()


def is_server_respond_with_200(url):
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return True
    return False


def is_domain_expired_in_more_than_1_month(domain_name):
    expiration_date = get_domain_expiration_date(domain_name)
    now = datetime.now()
    return (expiration_date - now).days > 30


def get_domain_expiration_date(domain_name):
    domain_info = whois.whois(domain_name)
    if type(domain_info.expiration_date) is list:
        return domain_info.expiration_date[1]
    return domain_info.expiration_date


def collect_errors(url):
    errors = []
    if not is_server_respond_with_200(url):
        errors.append(
            'ERROR: HEALTHCHECK STATUS is not 200'.format(url))
    if not is_domain_expired_in_more_than_1_month(url):
        errors.append(
            'WARNING: domain expired in less than 30 days')
    return errors


if __name__ == '__main__':
    path = parse_args().path
    urls = load_urls4check(path)
    for url in urls:
        errors = collect_errors(url)
        if errors:
            for error in errors:
                print(error)
        else:
            print('HEALTHCHECK for {} is OK'.format(url))
