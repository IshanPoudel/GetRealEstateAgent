''' From a particular sql file , get all the house_listings.'''

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



def get_list_of_houses(url):
    list_of_houses = []

    try:
        chrome_options = Options()  # Instantiate an options class for the selenium webdriver
        # chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        time.sleep(10)

        # From website get all the tags



        driver.get(url)
        time.sleep(20)

        driver.implicitly_wait(10)
        html_text = driver.page_source
        # convert based on 'html parser'
        soup = BeautifulSoup(html_text, 'html.parser')
        # print(soup)
        # print("AFTER BREAK \n\n")

        # //*[@id="MapHomeCard_5"]

        # get all the div ids .

        homecard_list = soup.find("div", {"id": "content"})
        homecard_list = homecard_list.find("div", {"data-react-server-container": "7"})
        homecard_list = homecard_list.find("div", {"data-react-server-container": "14"})
        homecard_list = homecard_list.find("div", {"data-react-server-container": "18"})
        homecard_list = homecard_list.find("div", {"data-react-server-root-id": "22"})

        homecard_list = homecard_list.find("div", {"class": "HomeViewsAndDisclaimer"})
        homecard_list = homecard_list.find("div", {"class": "HomeViews"})
        homecard_list = homecard_list.find("div", {"class": "PhotosView bg-color-white"})
        homecard_list = homecard_list.find("div")

        # find all homnecard_List
        homecard_list = homecard_list.find_all("div", {"id": re.compile("^MapHomeCard")})

        text = "3D WALKTHROUGH"

        # homecard_list = soup.find("div" , {"class": "HomeCardContainer defaultSplitMapListView"})


        for home in homecard_list:

            text_blob = home.get_text()
            if (text not in text_blob):
                # get_link
                home = home.find("a")
                home = home['href']
                home = "https://www.redfin.com" + home
                list_of_houses.append(home)

        return list_of_houses


    except Exception as e:
        print(e)
        return list_of_houses








#get those without any 3d scan icon on top

