import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://headsupfortails.com/pages/learn-with-huft')
driver.implicitly_wait(30)

start_button = driver.find_element(By.CLASS_NAME, 'formbutton')
pop_op = driver.find_element(By.CLASS_NAME, 'saraPopupBanner')
pop_op_exit = pop_op.find_element(By.TAG_NAME, 'span')

if pop_op_exit.is_displayed():
    driver.execute_script("arguments[0].click();", pop_op_exit)
start_button.click()

# select cat or dog
cat_dog_selection_box = driver.find_element(By.CSS_SELECTOR, '.ln_forminner.next')

animal_options = cat_dog_selection_box.find_elements(By.CLASS_NAME, 'flex-3')
animal_next_button = cat_dog_selection_box.find_element(By.TAG_NAME, 'button')

dog_age_box = driver.find_element(By.CSS_SELECTOR, '.ln_forminner.dog')
cat_age_box = driver.find_element(By.CSS_SELECTOR, '.ln_forminner.cat')

dog_age_options = dog_age_box.find_elements(By.CLASS_NAME, 'form-group-radio')
cat_age_options = cat_age_box.find_elements(By.CLASS_NAME, 'form-group-radio')

dog_age_next_button = dog_age_box.find_element(By.TAG_NAME, 'button')
cat_age_next_button = cat_age_box.find_element(By.TAG_NAME, 'button')


def getFinalData(driver, type):
    topics_box = driver.find_element(By.CSS_SELECTOR, '.ln_forminner.topics.next')
    topic_options = topics_box.find_elements(By.CLASS_NAME, 'form-group')
    topic_show_button = topics_box.find_element(By.TAG_NAME, 'button')

    for topic in topic_options:
        topic.click()

    topic_show_button.click()
    data_box = driver.find_element(By.CSS_SELECTOR, '.bb_cardfull_training.d-flexwraps')
    data = data_box.find_elements(By.CSS_SELECTOR, '.bb_blgcard_ver.d-flexwrap')

    results = []

    for article in data:
        link_data = article.find_element(By.CLASS_NAME, 'bb_cardcont_ver')
        link = link_data.find_element(By.TAG_NAME, 'a')
        print(link.text)
        results.append({'link': link.get_attribute('href'), 'title': link.text, 'type': type})

    print(len(results))
    return results


# make it clean later
# dogs :
ittr = 0
dogs_results = []

while ittr == 0 or ittr != len(dog_age_options):
    animal_options[0].click()
    animal_next_button.click()

    dog_age_options[ittr].click()
    dog_age_next_button.click()
    ittr += 1
    dogs_results.append(getFinalData(driver, 'dog'))
    reset_button = driver.find_element(By.CLASS_NAME, 'resultreset')
    reset_button.click()
    time.sleep(1)


dogs_results = [item for sublist in dogs_results for item in sublist]
# cats :
ittr = 0
cats_results = []

while ittr == 0 or ittr != len(cat_age_options):
    animal_options[1].click()
    animal_next_button.click()

    cat_age_options[ittr].click()
    cat_age_next_button.click()
    ittr += 1
    cats_results.append(getFinalData(driver, 'cat'))
    reset_button = driver.find_element(By.CLASS_NAME, 'resultreset')
    reset_button.click()
    time.sleep(1)

cats_results = [item for sublist in cats_results for item in sublist]

final_results = {
    'cat': cats_results,
    'dog': dogs_results
}

with open('articles.json', "w") as json_file:
    json.dump(final_results, json_file)
