import mysql.connector

mydb = mysql.connector.connect (host = "localhost", username = "root", password = "032303")

mycursor = mydb.cursor()

mycursor.execute ("CREATE DATABASE azur_lane;")
mycursor.execute ("show databases;")

for i in mycursor:
    print(i)
