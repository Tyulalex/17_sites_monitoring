# Sites Monitoring Utility

script takes a txt file with urls as an input and check:
 - site responds with 200
 - domain expired more than in 30 days

 urls in txt file shall be divided with \n
 

# System requirements
required python 3.5 installed
pip install -r requirements.txt

# How to install and run

to run it: 
on windows:
```
    python check_sites_health.py --path <path_to_file_with_urls>
```
on linux might require 
```
  python3 check_sites_health.py --path <path_to_file_with_urls>
  ```
--path shall be in the format of your system

Supported Systems: Windows, Unix
[TODO. There will be project description]

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

