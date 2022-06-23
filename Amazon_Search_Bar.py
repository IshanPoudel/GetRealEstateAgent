import re
import time
import logging
import csv
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



def get_dictionary_amazon(Search_phrase):
    chrome_options = Options()  # Instantiate an options class for the selenium webdriver
    # chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    time.sleep(10)


    # From website get all the tags
    url = "https://www.amazon.com/"
    driver.get(url)
    time.sleep(4)

    html_text = driver.page_source
    # convert based on 'html parser'
    soup = BeautifulSoup(html_text, 'html.parser')
    # get the search bar of ebay
    CSS_TUPLE = (By.CSS_SELECTOR, "#twotabsearchtextbox")

    abc = driver.find_element(*CSS_TUPLE);
    driver.implicitly_wait(10)
    abc.send_keys(Search_phrase)
    abc.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)
    time.sleep(2)
    html_text = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html_text, 'html.parser')
    driver.quit()

    div_search_class = soup.find("div", {"class": "s-main-slot s-result-list s-search-results sg-row"})

    div_container = div_search_class.find_all("div", {"data-component-type": "s-search-result"})

    item_link_amazon_dict = []

    for search_result in div_container:
        try:
            name = search_result.find("h2")
            name = name.get_text()

            #     Get link for the thing
            link = search_result.find("a", {"class": "a-link-normal s-no-outline"})
            link = link['href']

            item_link_amazon_dict[name] = "https://www.amazon.com/" + link

        except Exception as e:
            print("Not Found \n")
            print(e)

    return(item_link_amazon_dict)




