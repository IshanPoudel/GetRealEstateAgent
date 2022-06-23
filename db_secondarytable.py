# from our primary table Items we have a unique item id for each product
# in our secondary table , for each item , we are going to get link from the primary table ,
# use our ebay_individual_item function and then store it in our secondary table.

#primary key
# "CREATE TABLE Items(search_phrase VARCHAR(50) , name VARCHAR(300)
# , link VARCHAR(1000) , website VARCHAR(50) , itemID int PRIMARY KEY AUTO_INCREMENT

#we use itemID as our foreign key in the second table.

import mysql.connector
from Ebay_Search_Bar import get_dictionary_ebay
from Amazon_Search_Bar import get_dictionary_amazon
from Ebay_Individual_Item import get_individual_item

db = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd="rootroot" ,
    database = "ecommercelist"
)

mycursor = db.cursor()


#create secondary table
# mycursor.execute("DROP TABLE item_description")
# mycursor.execute("CREATE TABLE item_description(id int PRIMARY KEY, FOREIGN KEY(id) REFERENCES Items(itemID),price VARCHAR(50)  )")

# Store values in the second table
Q4= "INSERT INTO item_description(id , price) VALUES (%s,%s)"
#get first 10 rows of the database and get the required values from there


# get column id
mycursor.execute("SELECT itemID FROM Items")
primary_id = []
for x in mycursor:
    primary_id.append(x[0])



for i in range(3):
    mycursor.execute("SELECT link FROM Items WHERE itemID="+str(i))



    for x in mycursor:

        price = get_individual_item((x[0]))
        mycursor.execute(Q4 , (primary_id[i] , price))
        db.commit()
