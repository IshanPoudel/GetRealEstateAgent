''' Initializes the database for value entry'''
import mysql.connector

db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"
    )

mycursor = db.cursor()

mycursor.execute("DROP DATABASE IF EXISTS REAL_ESTATE_INFORMATION")
mycursor.execute("CREATE DATABASE REAL_ESTATE_INFORMATION")


db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot" ,
    database="REAL_ESTATE_INFORMATION"
    )

mycursor  = db.cursor()


mycursor.execute("CREATE TABLE HOUSE_LINK (link VARCHAR(1000) ,  houseID int PRIMARY KEY AUTO_INCREMENT , Date_Added datetime default now() , DataScraped Boolean not null default 0) ")

#for each house , print the street_address , agent_addres
mycursor.execute("CREATE TABLE HOUSE_AGENT (house_id int , street_address VARCHAR(1000) , state_address  VARCHAR(1000) , agent_name VARCHAR(1000) , AGENCY VARCHAR(1000) , trec VARCHAR(10) , Updated_on_Final Boolean not null default 0)")


q1 = "CREATE TABLE agent_record (agent_id int PRIMARY KEY AUTO_INCREMENT , trec_id VARCHAR(10) , name VARCHAR(200) , phone_number VARCHAR(20) , email VARCHAR(50) , address VARCHAR(200))"
mycursor.execute(q1)