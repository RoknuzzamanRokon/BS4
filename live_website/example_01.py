from bs4 import BeautifulSoup
import requests


url = "https://news.ycombinator.com/"

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")


content_tag = soup.find(name="a", rel="noreferrer")

link_tag = content_tag.get('href')

print(link_tag.title())
# print(link_tag.find('b'))
# print(link_tag.upper())
# # print(link_tag.title())

print(link_tag)

# print(content_tag.getText())

print("\n\n\n")


# print(article_find_all_method)
print("\n\n\n")


print("There print all website list in using 'getText'")
print("\n\n")

article_find_all_method = soup.find_all(class_="sitebit comhead")

for tag in article_find_all_method:
    text = tag.getText()
    print(text)

print("\n\n\n")


print("There print 'a' tag all content text")
print("\n\n")

article_find_all_method_2 = soup.find_all(name="a", rel="noreferrer")

for tag2 in article_find_all_method_2:
    text2 = tag2.get_text()
    print(text2)

print("\n\n\n")

article_find_all_method_3 = soup.find_all(name="span", title="2023-07-26T11:19:07")

for tag3 in article_find_all_method_3:
    text3 = tag3.get_text()
    print(text3)

print("\n\n\n")

article_find_all_method_4 = soup.find(name='span', class_="score")
print(article_find_all_method_4)


print("\n\n\n")

print("There in print all points")
print("\n")


article_find_all_method_5 = soup.find_all(name='span', class_="score")

for tag5 in article_find_all_method_5:
    text5 = tag5.getText()
    print(text5)


print("\n\n\n")

print("\n\n\n")

article_find_all_method_6 = soup.find_all(class_="sitebit comhead")

for tag6 in article_find_all_method_6:
    text6 = tag6.get_text('t')
    print(text6)

print("\n\n\n")