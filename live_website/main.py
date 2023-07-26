from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
lv_web_page = response.text

soup = BeautifulSoup(lv_web_page, "html.parser")

print(soup.title)