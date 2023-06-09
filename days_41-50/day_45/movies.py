from bs4 import BeautifulSoup
import requests

with open("movies.txt", "w") as file:
    url = "https://variety.com/lists/best-movies-of-all-time/the-graduate-1967-2/"
    response = requests.get(url=url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    titles = soup.select(selector="article div div h2")
    for title in titles[::-1]:
        file.write(f"{title.getText().strip()}\n")
