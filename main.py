from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    read_file = file.read()

soup = BeautifulSoup(read_file, "html.parser")

all_ancer_tag = soup.find_all(name='a')


for tag in all_ancer_tag:
    x = tag.get('href')
    print(x)


heading = soup.find(name='h1', id='name')
print(heading)

find_class = soup.find(name='h3', class_='heading')
print(find_class.text)

company_url = soup.select_one(selector='p a')
print(company_url)


heading = soup.select(".heading")
print(heading)