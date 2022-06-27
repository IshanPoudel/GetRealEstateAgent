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




db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"  ,
    database = "real_estate")


#create a table
mycursor = db.cursor()




# q1 = "CREATE TABLE agent_record (agent_id int PRIMARY KEY AUTO_INCREMENT , trec_id VARCHAR(10) , name VARCHAR(200) , phone_number VARCHAR(20) , email VARCHAR(50) , address VARCHAR(200))"
# mycursor.execute(q1)

# after creating table

# read csv file
location = "/Users/user/Desktop/master_trec.xlsx"
data = pd.read_excel(r'/Users/user/Desktop/master_trec.xlsx')
data.columns = ['TREC_ID' ,'NAME' ,'PHONE' , 'EMAIL' , 'STREET' , 'CITY' , 'STATE' , 'ZIP' ]
df = data.iloc[ :  , :]

count =0
for  row in df.itertuples():
    try:
        # print(row[0])
        # print(row[1])
        # print(row[2])
        # print(row[3])
        trec = "0"+str(row[1])+" "
        address= str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " " + str(row[8])
        # print(str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]))
        query = "I"
        mycursor.execute(query , (trec , str(row[2]) , str(row[3]) , str(row[4]) , address ))

        print("Added agent " + str(row[1])+"'s record.")
        db.commit()
    except:
        print("Error")
        print(traceback.format_exc())



print("total" + str(count))


# for values in df:
#     if not values:
#         values = " "
#
# trec = str(df[0])
# name = str(df[1])
# phone = str(df[2])
# email = str(df[3])
# address = str(df[4]) + " " + str(df[5]) + " " + str(df[6])+ " " + str(df[7])
#
    # print(row['TREC_ID'])
    # print(row['NAME'])
    # print(row['PHONE'])
    # print(row['EMAIL'])
    # print(row['STREET'] + " " + row['CITY'] + " " + row['STATE'] + " " + row['ZIP'])
