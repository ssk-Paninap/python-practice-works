#import the mysql connector in python
import mysql.connector
#input creadentials based on your presented inputs
mydb = mysql.connector.connect (host = "localhost", username = "root", password = "your pass")

mycursor = mydb.cursor()

mycursor.execute ("CREATE DATABASE name;")
mycursor.execute ("show databases;")

#iterate and print all databases 
for i in mycursor:
    print(i)
