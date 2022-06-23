import mysql.connector
from Ebay_Search_Bar import get_dictionary_ebay
from Amazon_Search_Bar import get_dictionary_amazon


db = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd="rootroot" ,
    database = "ecommercelist"

)

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE ecommercelist")
# mycursor.execute("DROP TABLE Items")
# mycursor.execute("CREATE TABLE Items(search_phrase VARCHAR(50) , name VARCHAR(300) , link VARCHAR(1000) , website VARCHAR(50) , itemID int PRIMARY KEY AUTO_INCREMENT )")

# mycursor.execute("DESCRIBE Items")
#
# for x in mycursor:
#     print(x)
#for a specific thing create two tables , one for stuff from amazon , one for stuff from ebay


# after succesfully executing
mycursor.execute("SELECT * FROM Items")
for x in mycursor:
    print(x)


def store_in_database(dictionary_value , search_phrase , website):

    for key , value in dictionary_value.items():
        mycursor.execute("INSERT INTO Items (search_phrase , name , link , website) VALUES (%s , %s , %s , %s)" ,
                         (search_phrase , key , value , website) )
        db.commit()








