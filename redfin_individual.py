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





def get_real_estate_info(link):


    chrome_options = Options()  # Instantiate an options class for the selenium webdriver
    chrome_options.add_argument("--headless")  # So that a chrome window does not pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    time.sleep(10)


    driver.get(link)
    time.sleep(4)

    blank_list = []
    blank_list.append("Error")


    try:
        html_text = driver.page_source
        # convert based on 'html parser'
        soup = BeautifulSoup(html_text, 'html.parser')
        # print(soup)
    except:
        print("Could not get source")
        print(traceback.format_exc())
        return blank_list
        quit()


    #get_property_address
    #xpath :  //*[@id="content"]/div[11]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/header/h1/div[1]/text()[1]
    #get real estate agents_name
    #xpath: //*[@id="house-info"]/div/div/div[3]/div[1]/div/div/div/div/span/span[1]
    #get agents_real_estate_number
    #xpath" //*[@id="house-info"]/div/div/div[3]/div[1]/div/div/div/div/span/span[2]/span

    try:

        home = soup.find("div" , {"id":"content"})

        home = home.find("div"  , {"data-react-server-container" : "10"})
        home = home.find("div" , {"class":"alongTheRail"})
        # print(home)
        # home = home.find("div" , {  "class":"dp-col-sm-12 dp-col-md-8"})

        list_of_server_root_id = ["22" , "27" ]

        i=0
        home_2 = None
        while home_2 is None:

             home_1 = home.find("div" , {"data-react-server-root-id":list_of_server_root_id[i] , "class": "dp-col-sm-12 dp-col-md-8"})
             home_2 = home_1.find("section" , {"class":"MainHouseInfoPanel"})
             i=i+1
        home_3 = home_2.find("div" , {"class" : "sectionContainer"})
        home_4 = home_3.find("div" , {"class" : "house-info-container"})
        home_5 = home_4.find( "div" , {"class":"agent-basic-details"})
        agent_details = home_5.find("span")


        agent_info = agent_details.get_text()
        abc = agent_info.split('•')




        # get the address of the house
        #iterate through server_root_id_until_you_find one with class="Section AddressBannerSectionV2 white-bg not-omdp"

        address = home.find_all("div", {"class": "dp-col-sm-12 dp-col-md-8"})

        for div_tags in address:
            # find divs if present
            check_divs = div_tags.find("div", {"class": "Section AddressBannerSectionV2 white-bg not-omdp"})
            if check_divs is not None:
                address = check_divs

        street_address = address.find("div", {"class": "street-address"})
        state_address = address.find("div", {"class": "dp-subtext"})

        street_address = street_address.get_text()
        state_address = state_address.get_text()

        print(street_address + state_address)






    except Exception:
        print("Error while getting the details")
        print(traceback.format_exc())
        return blank_list
        quit()



    try:

        num_of_details = len(abc)
        #preprocess
        real_estate_agent_name = abc[0][10:]
        real_estate_agent_trec = abc[1][6:]
        if num_of_details == 3:
            real_estate_brokerage = abc[2][1:]
        else:
            real_estate_brokerage = "None"

        # print(real_estate_agent_name)
        # print(real_estate_agent_trec)
        # print(real_estate_brokerage)

        # return [street_address , state_address ,real_estate_agent_name , real_estate_agent_trec , real_estate_brokerage]
        info = []
        info.append(street_address)
        info.append(state_address)
        info.append(real_estate_agent_name)
        info.append(real_estate_agent_trec)
        info.append(real_estate_brokerage)
        return info

    except:
        print(traceback.format_exc())
        return blank_list










