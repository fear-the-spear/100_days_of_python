from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

story_titles = soup.select(selector="tr.athing")
score_tags = soup.select(selector="span.score")

title_tag = [lines.select_one(selector="span a") for lines in story_titles]
article_text = [title.getText() for title in title_tag]
article_link = [title.select_one(selector="span.titleline a").get(
    "href") for title in story_titles]
article_upvotes = [int(score.getText().split()[0]) for score in score_tags]

max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(article_text[max_index])
print(article_link[max_index])
print(f"Upvotes: {max_value}")
