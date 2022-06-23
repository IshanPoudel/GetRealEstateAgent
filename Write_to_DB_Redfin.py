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


# # // get_list_of_houses and use it to look for address.
#
#
# # get the links from the database.
# list = get_list_of_houses()
#
# if len(list) == 0:
#     print("List is empty")
#     quit()
#
# house_link = list[0]
# print("Getting real_estate_info_for house " + house_link)
#
#
#
# agent_list = get_real_estate_info(house_link)
#
# if agent_list is None:
#     print("No values in the list")
# else:
#     print(agent_list)
#
#
# house_link=list[1]
# print("Getting real_estate_info_for_house" + house_link)
#
# agent_list = get_real_estate_info(house_link)
#
# if agent_list is None:
#     print("No values in the list")
# else:
#     print(agent_list)



#create a database.
#one table for house_id and house_link
#one table for house_id and address and other info ,
#one table for real estate agent info
#one table from trec
#final table corelating all .

db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"  ,
    database = "real_estate")


mycursor = db.cursor()

# mycursor.execute ("DROP DATABASE IF EXISTS real_estate")
# mycursor.execute ("CREATE DATABASE REAL_ESTATE")
# mycursor.execute("CREATE TABLE house_link(  link VARCHAR(1000) , int houseID PRIMARY KEY AUTO_INCREMENT )")
# mycursor.execute("CREATE TABLE house_link(  link VARCHAR(1000)  , houseID int PRIMARY KEY AUTO_INCREMENT )")



# //store values in the database

#urls for the houses.
url = "https://www.redfin.com/city/30794/TX/Dallas/filter/sort=lo-days,viewport=34.25294:31.40081:-94.60209:-98.39237"
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
            quit()

    mycursor.execute("DESCRIBE house_link")

    for x in mycursor:
        print(x)

#at this point all have been read , you only need to read the new ones ,


