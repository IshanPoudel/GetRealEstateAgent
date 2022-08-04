'''First Step: Given link to Redfin , Zillow find a way to get the new links from a file and store it
 into the database table named house_Link'''


import re
import time
import logging
import csv
from bs4 import BeautifulSoup
from redfin import get_list_of_houses
from redfin_individual import get_real_estate_info

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
import config



def get_all_links():




    db = mysql.connector.connect(host="localhost",
                                 user=config.user,
                                 passwd=config.password,
                                 db='real_estate'

                                 )

    mycursor = db.cursor()


    # //store values in the database

    url = config.url
    url_list = []
    url_list.append(url)

    for i in range(2 , 7):
        url_list.append(url+"/page-"+str(i))

    for url in url_list:
        time.sleep(20)
        print("Getting values from "+ url)


        house_link = get_list_of_houses(url)

        #need to know which errors did not work
        if house_link is None:
            print(url + "did not work")

        for house in house_link:
            # check if it is already in the database.
            # you have an incoming stream of houses , once you reach a house that has already been read previously you stop
            query = "SELECT link FROM house_link WHERE link = " + " '" + house + "'"
            mycursor.execute(query)
            check_if_present = mycursor.fetchall()

            if not check_if_present:
                mycursor.execute("INSERT INTO house_link ( link ) VALUES (%s )",
                                 (house,))
                db.commit()
                print("Inserted into database")




            if check_if_present:

                print("Up to Date")
                print(house + "already in the table")


        mycursor.execute("DESCRIBE house_link")
        #use a different sql query

        for x in mycursor:
            print(x)

    #at this point all have been read , you only need to read the new ones ,


