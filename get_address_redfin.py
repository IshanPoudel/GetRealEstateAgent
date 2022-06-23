import re
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
# chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
time.sleep(10)

link = "https://www.redfin.com/TX/Arlington/1109-Auburn-Dr-76012/home/32312027"
driver.get(link)
time.sleep(4)


html_text = driver.page_source

# file = open("Check_file_for_individual_house" , "r")
# convert based on 'html parser'
soup = BeautifulSoup(html_text, 'html.parser')
# print(soup)

home = soup.find("div", {"id": "content"})
home = home.find("div", {"data-react-server-container": "10" , "class":"aboveBelowTheRail"})
home = home.find("div", {"class": "alongTheRail"})

address = home.find_all("div" , {"class" : "dp-col-sm-12 dp-col-md-8" })

for div_tags in address:
    #find divs if present
    check_divs = div_tags.find("div" , {"class":"Section AddressBannerSectionV2 white-bg not-omdp"})
    if check_divs is not None:
        address = check_divs


# print(address)







# address_2 = None
# while address_2 is None:
#     try:
#
#         address_1 = home.find("div", {"data-react-server-root-id": list_of_server_root_id_for_address[i],
#                                            "class": "dp-col-sm-12 dp-col-md-8"})
#         address_2 = address_1.find("section", {"class": "Section AddressBannerSectionV2 white-bg not-omdp"})
#         i = i + 1
#     except Exception:
#         print(traceback.format_exc())
#         quit()
#     #if you could not find ,
#
#
# address = address_2.find("div" , {"class" : "street-address"}  )
# address=  address.get_text()
# print("The address is address"+ address )