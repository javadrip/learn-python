from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

spans = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for span in spans:
    records = span.find('a')
    article_texts.append(records.getText())
    article_links.append(records.get("href"))

article_upvotes = [int(score_span.getText().split()[0]) for score_span in soup.find_all(name="span", class_="score")]

max_upvote = max(article_upvotes)
max_upvote_article = int(article_upvotes.index(max_upvote))

print(f" Winner is '{article_texts[max_upvote_article]}', here {article_links[max_upvote_article]} with total of {article_upvotes[max_upvote_article]} points.")

# from bs4 import BeautifulSoup

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# # <title>Angela's Personal Site</title>

# print(soup.title.name)
# # title

# print(soup.title.string)
# # Angela's Personal Site

# # Indents the soup contents
# print(soup.prettify())

# # Finds the first <a> tag
# print(soup.a)
# # <a href="https://www.appbrewery.co/">The App Brewery</a>

# # Finds all <a> tags and stores in a list
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # Get the anchor texts
#     print(tag.getText())
#     # Get all the links in <a> tags
#     print(tag.get("href"))

# # Find a specific heading with <h1> tag and "name" id
# heading = soup.find(name="h1", id="name")
# print(heading)

# # class is a reserved keyword in Python, so use class_ to find classes
# # Find a specific heading with <h3> tag and "heading" class
# section_heading = soup.find(name="h3", class_="heading")

# # Find urls using CSS selectors
# company_url = soup.select_one(selector="p a")
# print(company_url)

# # Find the element with id="name"
# name = soup.select_one("#name")
# print(name)

# # Find all elements with class="heading"
# headings = soup.select(".heading")
# print(headings)
