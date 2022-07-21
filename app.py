from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# import regex library.
import re

# Options for Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--log-level=1')
options.add_argument('--disable-gpu')

# Create chrome driver instance.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Open wikipedia home page.
driver.get("https://www.wikipedia.org/")

# Wikipedia title is "Wikipedia".
# title = driver.find_element(By.CLASS_NAME, value="central-textlogo__image")
# print(title.text)

# Get search bar.
search_bar = driver.find_element(By.ID, value="searchInput")

# Press enter
search_bar.send_keys("ASD", Keys.ENTER)

# Switch driver to current url.
driver.get(driver.current_url)

# Check that the page title is "ASD".
title = driver.find_element(By.CLASS_NAME, value="firstHeading")
assert driver.title == "ASD - Wikipedia"

# Get the link text from "Adaptive software development" from the page.
link = driver.find_element(By.LINK_TEXT, value="Adaptive software development")

link.click()

driver.get(driver.current_url)


assert driver.title == "Adaptive software development - Wikipedia"


# Get the element with a class of mw-parser-output.
content = driver.find_element(By.CLASS_NAME, value="mw-parser-output")

# get all the p elements from content.

p_tags = content.find_elements(By.TAG_NAME, value="p")


# Loop over all p tags.
for p in p_tags:
    # Get the text from the p tag.
    text = p.text

    # Remove citations.
    text = re.sub(r"\[[0-9]*\]", "", text)
    # Print the text.
    # print(text)

    # Create a dict to hold url text and url.
    url_dict = {}
    # If any urls in p tag, add text to url_dict as the key and the url as the value.
    urls = p.find_elements(By.TAG_NAME, value="a")

    for url in urls:
      url_dict[url.text] = url.get_attribute("href")


    # Print the url_dict in a readable format.
    for key, value in url_dict.items():
        print(key, value)
  


