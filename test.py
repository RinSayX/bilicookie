import requests
from bs4 import BeautifulSoup
from selenium import *


url = "https://bilibili.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
bili = requests.get(url, headers=headers)
cookies = bili.cookies
for cookie in cookies:
    print(f"Name: {cookie.name}, Value: {cookie.value}")



