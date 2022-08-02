'''From the agent_list , get the houseID , and
co-relate with the master trec sql file and insert into final table'''
import re
import time
import logging
import csv
import traceback
import concurrent.futures
from bs4 import BeautifulSoup
from redfin import get_list_of_houses
from redfin_individual import get_real_estate_info
import threading
from threading import Lock

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
import xlrd
import pandas as pd
import config

#for each agent in the address database
#store it in the final table.


def corelate():


    db = mysql.connector.connect(host="localhost",
                                 user=config.user,
                                 passwd=config.password,
                                 db='real_estate'

                                 )
    mycursor = db.cursor()





    join_query = " SELECT h.house_id ,h.trec , h.agent_name , a.phone_number , a.email , a.address as 'AGENT ADDRESS' , h.street_address , h.state_address from house_agent h JOIN agent_record a ON h.trec = a.trec_id WHERE h.updated_on_final = 'false' "
    mycursor.execute(join_query)
    rows = mycursor.fetchall()
    for value in rows:
        try:

            #get all required values
            trec = value[1]
            name = value[2]
            phone = value[3]
            email = value[4]
            agent_address = value[5]
            listed_property_street_address = value[6] + " " + value[7]

            #get house_link.
            house_id = value[0]
            query = "SELECT link from house_link WHERE houseID="+str(house_id)
            mycursor.execute(query)
            house_link = mycursor.fetchall()
            for value in house_link:
                value = house_link[0]
            house_link=value[0]




            query = "INSERT INTO final_agent(trec, name, phone, email, business_address , listed_property_address , house_link) VALUES( %s, %s, %s, %s, %s, %s, %s )"


            mycursor.execute(query , (trec , name , phone , email , agent_address , listed_property_street_address , house_link))
            db.commit()
            # change the value of update_on_final of the table to "true"
            change_to_true_query = "UPDATE house_agent SET updated_on_final = 'true' WHERE house_id="+str(house_id)
            mycursor.execute(change_to_true_query)
            db.commit()
            print("Updated value")
        except:
            print("Could not print")
            print(traceback.format_exc())

