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
from random import randint


db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"  ,
    database = "real_estate")

#create secondary table for each id with the house_id from the primary table

# CREATE TABLE house_agent(house_id int PRIMARY KEY ,
#                                               FOREIGN KEY(house_id) REFERENCES house_link(houseID) ,
#                                                                                street_address VARCHAR(100) ,
#                                                                                               state_address VARCHAR(100) ,
#                                                                                                             agent_name VARCHAR(100) ,
#                                                                                                                        AGENCY VARCHAR(100) ,
#                                                                                                                               trec VARCHAR(10));

#get value from house_link table with data_present true.
mycursor = db.cursor()

mycursor.execute("SELECT link , houseID FROM house_link WHERE data_present = 'false'")
link_and_id = mycursor.fetchall()

for (link , id) in link_and_id:
    print(link)
    print(id)




for link , id in link_and_id:
    time.sleep(randint(5 , 20))

    to_commit = get_real_estate_info(link)
    query = "INSERT INTO house_agent(house_id , street_address , state_address , agent_name , AGENCY , trec ) VALUES (%s , %s , %s , %s , %s , %s)"
    if to_commit[0]=='Error':
        print("Error")
    else:
        #change value of house_agent_table
        mycursor.execute(query , (int(id) , str(to_commit[0]), str(to_commit[1]) , str(to_commit[2]) , str(to_commit[4]) , str(to_commit[3]) ) )
        db.commit()
        #change value of data_present of house_link table to true
        Q = "UPDATE house_link SET data_present = 'true' WHERE houseID="+str(id)
        mycursor.execute(Q)
        db.commit()
        print("Updated house with address"+ to_commit[0]+to_commit[1] + " and agent" + to_commit[2])


