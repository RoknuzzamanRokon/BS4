from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
lv_web_page = response.text

soup = BeautifulSoup(lv_web_page, "html.parser")
all_tag_find = soup.find_all(name='a', rel="noreferrer")

for tag in all_tag_find:
    all_tags_find_all = tag.getText()
    print(all_tags_find_all)

# all_tag = soup.find(name='a', rel="noreferrer")
# print(all_tag.getText())