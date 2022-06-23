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
import mysql.connector

def get_dictionary_ebay(search_phrase):
    # create function that given a search phrase gives the item_link dictionary

    chrome_options = Options()  # Instantiate an options class for the selenium webdriver
    chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    time.sleep(10)

    # From website get all the tags
    url = "https://www.ebay.com/"
    driver.get(url)
    time.sleep(4)

    html_text = driver.page_source
    # convert based on 'html parser'
    soup = BeautifulSoup(html_text, 'html.parser')
    # get the search bar of ebay
    CSS_TUPLE = (By.CSS_SELECTOR, "#gh-ac")

    abc = driver.find_element(*CSS_TUPLE);
    abc.send_keys(search_phrase)
    abc.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)

    time.sleep(2)
    html_text = driver.page_source.encode('utf-8')
    # print(html_text)
    print("BREAK \n\n\n\n\n")

    # Create an action sequence where it clicks on each item , goes to the page and gets som value
    # Returns back and does the same thing for the next item

    # create an action sequence
    # locate the link by xpath or create a function

    # use bs4 to get link
    soup = BeautifulSoup(html_text, 'html.parser')
    # divs = soup.find("div" , {"class": "srp-main srp-main--isLarge"})
    divs_container = soup.find("div", {"class": "srp-river-results clearfix"})
    bullet_list = divs_container.find("ul")

    # have a list for all links
    # click on each link and get info4

    # create list to store value
    item_link_ebay_dict = {}
    for url_list in bullet_list.find_all("li", {"class": re.compile("^s-item s-item__pl-on-bottom")}):
        # Get name and link
        link = url_list.find("a")
        name = url_list.find("h3")
        name = name.get_text()

        # print(link['href'])
        # print(name.get_text())

        item_link_ebay_dict[name] = link['href']

        print("\n")

    # print(item_link_ebay_dict)
    return item_link_ebay_dict
    # use x path
    # //*[@id="srp-river-results"]/ul/li[2]
    # get all the list
    # click on a link using xpath

    # XPath_tuple =(By.XPATH , "//*[@id='srp-river-results']/ul/li[2]//div/div[1]/div/a")
    # Since we want to use action chains best way is to get the name of the product and open it

    # abc = driver.find_element(*XPath_tuple).click()

    # for i in range(3):
    #     driver.implicitly_wait(3)
    #     try:
    #
    #         LINK_TUPLE = (By.LINK_TEXT , item_link[i])
    #
    #         abc = driver.find_element(*LINK_TUPLE)
    #         abc.click()
    #     #     get page_source and then go back
    #         driver.back()
    #     except:
    #         print("Could not find link for " + item_link[i])
    #     driver.implicitly_wait(10);

    # create an action_sequence
    # go to each url and gather select information

    # class="srp-main srp-main--isLarge"
    # <div id="mainContent"
    # <div class = "srp-river srp-layout-inner">
    # <div id = "srp-river-main>
    # <div class = "srp-river-results clearfix"
    # <ul class = "srp-river-results clearfix"> contains lists
    # <li class = "srp-river-answer srp-river-answer--NAVIGATION"
    # <LI CLASS = "sitem s-item__pl-on-button">




