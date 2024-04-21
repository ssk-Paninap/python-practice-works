import mysql.connector
mydb = mysql.connector.connect (host = "localhost", username = "root", password = "", database = "bbl")
lm = mydb.cursor()

#creation ng DB
lm.execute("create table russ (ship_id int primary key auto_increment, name varchar(50), rarity varchar(100))")

#insert area pattern lang s = string, i = int
inserting = "INSERT INTO russ (name, rarity) values (%s, %s)"
russians = [("item", "wee"), ("item 2", "wee"), ("item 3", "sd"), ("item 4", "ui")]

lm.executemany(inserting,russians)
lm.execute("Select * from russ")
gett = lm.fetchall()

for i in gett:
    print (i)
    
mydb.commit()
