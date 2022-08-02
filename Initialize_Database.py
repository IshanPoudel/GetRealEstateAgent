''' Initializes the database for value entry'''
import mysql.connector
import config

db = mysql.connector.connect(host="localhost" ,
    user = config.user ,
    passwd= config.password
    )

mycursor = db.cursor()

mycursor.execute("DROP DATABASE IF EXISTS REAL_ESTATE")
mycursor.execute("CREATE DATABASE REAL_ESTATE")

db = mysql.connector.connect(host="localhost" ,
    user = config.user ,
    passwd= config.password,
    db='real_estate'

    )

mycursor = db.cursor()

#create house_link table
mycursor.execute("CREATE TABLE house_link(  link VARCHAR(1000)  , houseID int PRIMARY KEY AUTO_INCREMENT , data_present VARCHAR(10) default 'false' )")

#create house_agent_table
mycursor.execute("CREATE TABLE HOUSE_AGENT (house_id int PRIMARY KEY ,FOREIGN KEY(house_id) REFERENCES house_link(houseID), street_address VARCHAR(1000) , state_address  VARCHAR(1000) , agent_name VARCHAR(1000) , AGENCY VARCHAR(1000) , trec VARCHAR(10) , updated_on_final VARCHAR(10) default 'false')")

#create agent_record
mycursor.execute ("CREATE TABLE agent_record (agent_id int PRIMARY KEY AUTO_INCREMENT , trec_id VARCHAR(10) , name VARCHAR(200) , phone_number VARCHAR(20) , email VARCHAR(50) , address VARCHAR(200))")

#create final_agent
query = "CREATE TABLE final_agent(agent_id int PRIMARY KEY AUTO_INCREMENT , trec VARCHAR(10) , name VARCHAR(100) , phone VARCHAR(100) , email VARCHAR(100) , business_address VARCHAR(100) , listed_property_address VARCHAR(100) ,house_address_city VARCHAR(100) , house_link VARCHAR(500) ) "
mycursor.execute(query)