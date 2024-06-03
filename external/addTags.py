import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def addTags(article):
    try:
        url = article['link']

        driver = webdriver.Chrome()

        driver.get(url)
        driver.implicitly_wait(10)

        ul = driver.find_element(By.CSS_SELECTOR, '.blog_tabs.d-flex')
        a_tags = ul.find_elements(By.TAG_NAME, 'a')
        tags_text = []
        for a in a_tags:
            print(a.text)
            tags_text.append(a.text)

        article['tags'] = tags_text

        return article
    except:
        return article

file_path = 'articles.json'

with open(file_path, 'r') as file:
    data = json.load(file)

results = []

for animal in data.values():
    for article in animal:
        results.append(addTags(article))


with open('articles_final.json', "w") as json_file:
    json.dump(results, json_file)
