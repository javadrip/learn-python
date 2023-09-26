import requests
from bs4 import BeautifulSoup

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/2000-08-12"

response = requests.get(URL)
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)
