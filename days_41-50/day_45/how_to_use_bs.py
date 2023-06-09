from bs4 import BeautifulSoup

with open("./bs_test_website.html") as file:
    content = file.read()
    # replaces all new lines with spaces instead
    # print(content)

soup = BeautifulSoup(content, 'html.parser')
print(soup)  # prints the entire html document
print(soup.h1)  # prints the FIRST h1 tag
print(soup.p)  # prints the FIRST p tag
print(soup.find_all(name='a'))  # finds ALL a tags

all_anchor_tags = soup.find_all(name='a')

# get text from all the anchor tags
for tag in all_anchor_tags:
    print(tag.getText())

# get links from all the anchor tags
for tag in all_anchor_tags:
    print(tag.get('href'))

# get tags by attribute
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# selecting a tag nested within other tags (in this case, an a tag within a p)
company_url = soup.select_one(selector="p a")
print(company_url)
# can use class/id selectors as well
name = soup.select_one(selector="#name")
print(name)

h3_heading = soup.select_one(selector=".heading")
print(h3_heading)

# selecting ALL tags of a specific selector
all_headings = soup.select(selector=".heading")
print("All Headings:", all_headings)

# get the value of a key
form_tag = soup.find("h3")
box_value = form_tag.get("box")
print(box_value)
