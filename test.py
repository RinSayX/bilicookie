import requests
from selenium import *


url = "https://bilibili.com"
headers = {}
bili = requests.get(url)
cookies = bili.cookies
for cookie in cookies:
    print(f"Name: {cookie.name}, Value: {cookie.value}")



