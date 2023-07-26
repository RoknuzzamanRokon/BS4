from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
lv_web_page = response.text

soup = BeautifulSoup(lv_web_page, "html.parser")
# print(soup.find_all('a'))
all_tag = soup.find(name='a', rel="noreferrer")


print(all_tag.getText())