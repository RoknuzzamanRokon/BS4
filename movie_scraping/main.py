import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
url_requests = requests.get(url)

url_text_requests = url_requests.text


soup = BeautifulSoup(url_text_requests, "html.parser")


all_movie_list = soup.find_all(name='h3', class_="lister-item-header")
movie_list = []
for movie in all_movie_list:
    lists = movie.getText()
    movie_list.append(lists)


numbers = []
names = []
years = []

for item in movie_list:
    # Separate the number using string manipulation
    number = item.split('.')[0].split('\n')[1].strip()
    numbers.append(number)

    # Separate the name using string manipulation
    name = item.split('\n')[2].strip()
    names.append(name)

    # Separate the year using string manipulation
    year = item.split('(')[1].split(')')[0]
    years.append(year)


with open('movies.csv', 'w') as csvfile:
#     fieldnames = ['Number', 'Name', 'Year']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for i in range(len(movie_list)):
#         writer.writerow({'Number': numbers[i], 'Name': names[i], 'Year': years[i]})




