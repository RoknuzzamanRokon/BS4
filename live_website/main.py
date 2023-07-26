from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
lv_web_page = response.text

soup = BeautifulSoup(lv_web_page, "html.parser")
article_tag = soup.find(name='a', rel="noreferrer")

# for tag in all_tag_find:
#     all_tags_find_all = tag.getText()
#     print(all_tags_find_all)

# all_tag = soup.find(name='a', rel="noreferrer")
# print(all_tag.getText())
#
# tag_find = soup.find(name="a", rel="noreferrer")
# print(tag_find.text)

article_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_="score").getText()

print(article_link)
print(article_upvote)