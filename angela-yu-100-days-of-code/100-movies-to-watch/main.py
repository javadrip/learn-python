import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

h3s = soup.find_all(name="h3", class_="title")

titles = [h3.getText() for h3 in h3s]
movies = titles[::-1]

print(movies)
