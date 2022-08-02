''' Preliminary file to get some more scores for houses. Disregard'''


#from the house_link get house_specs.
# PRICE
# BED AND BATH
# SQ FT
# LOT SIZE
# year built
# car-dependent walk score

import time
import logging
import csv
from bs4 import BeautifulSoup
from redfin import get_list_of_houses

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

import traceback

chrome_options = Options()  # Instantiate an options class for the selenium webdriver
chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
time.sleep(10)

link = "https://www.redfin.com/TX/Dallas/3414-Lindenwood-Ave-75205/home/32067482"

driver.get(link)

try:
    html_text = driver.page_source
    # convert based on 'html parser'
    soup = BeautifulSoup(html_text, 'html.parser')
    # print(soup)
except:
    print("Could not get source")
    print(traceback.format_exc())
    quit()

home = soup.find("div", {"id": "content"})

home = home.find("div", {"data-react-server-container": "10"})
home = home.find("div", {"class": "alongTheRail"})

address = home.find_all("div", {"class": "dp-col-sm-12 dp-col-md-8"})

for div_tags in address:
    # find divs if present
    check_divs = div_tags.find("section", {"class": "Section MainHouseInfoPanel"})
    # print(check_divs)
    if check_divs is not None:
        address = check_divs
        print("found section mainhouseinfopannel")


home = address.find("div" , {"class" : "sectionContainer"})
# print(home)
home = home.find("div" , {"class" : "house-info-container"})
home = home.find("div" , {"class" : "content clear-fix"})
key_details = home.find_all("div" , {"class" : "keyDetailsList"})

# for all divs in key_detail_list search for status , property_type , style , community , lotsize
for details in key_details:
    key_detail_list = details.find_all("div" )
    for each_value in key_detail_list:
        print(each_value.get_text())
        print("\n")
        #year built , lot size and community
        #price
        #price,sq ft

