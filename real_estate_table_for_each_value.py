''' For each house link in the house_link table ,
split it into threads and get the house specs for each value and update it.'''


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






# ALTER TABLE table1 ADD COLUMN foo INT DEFAULT 0;
# ALTER TABLE house_agent ADD COLUMN updated_on_final VARCHAR(10) DEFAULT "false";
def chunks(list_to_split , n_parts):


    n_parts = max(1, n_parts)
    n_parts = min(n_parts , len(list_to_split))

    print("Splitting into" + str(n_parts) + " parts")

    chunk_size, remainder = divmod(len(list_to_split), n_parts)




    return (list_to_split[i*chunk_size+min(i,remainder):(i+1)*chunk_size+min(i+1 , remainder)]  for i in range(n_parts))








def update_to_db(link_and_id ):
    count = 0;
    for link , id in link_and_id:
        time.sleep(randint(5 , 20))

        to_commit = get_real_estate_info(link)
        query = "INSERT INTO house_agent(house_id , street_address , state_address , agent_name , AGENCY , trec ) VALUES (%s , %s , %s , %s , %s , %s)"
        if to_commit[0]=='Error':
            print("Error")
        else:
            #change value of house_agent_table
            try:

                mycursor.execute(query , (int(id) , str(to_commit[0]), str(to_commit[1]) , str(to_commit[2]) , str(to_commit[4]) , str(to_commit[3]) ) )
                db.commit()

                #change value of data_present of house_link table to true
                Q = "UPDATE house_link SET data_present = 'true' WHERE houseID="+str(id)
                mycursor.execute(Q)
                db.commit()

                print("Updated house with address"+ to_commit[0]+to_commit[1] + " and agent" + to_commit[2])
                count = count+1

            except Exception:
                print("Could not update")
                print(traceback.format_exc())
    print("Updated " + str(count) + "values")







def get_real_estate_table_for_each_value():
    db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="rootroot",
                                     database="real_estate")

    mycursor = db.cursor()

    mycursor.execute("SELECT link , houseID FROM house_link WHERE data_present = 'false'")
    link_and_id = mycursor.fetchall()


    split_link_into_n_parts = 5
    list_for_threads = chunks(link_and_id ,split_link_into_n_parts)



    #split the list into equal sizes and feed it to the function below .
    #link_and_id have to be split into equal parts.


    lock = Lock()

    threads = []

    # for house_link_and_id in list_for_threads:
    #     print(house_link_and_id)
    #     print("haha")

    for house_link_and_id in list_for_threads:
        t = threading.Thread(target= update_to_db , args = (house_link_and_id , ))
        t.start()
        print("I started a thread")
        threads.append(t)

    for thread in threads:
        thread.join()

