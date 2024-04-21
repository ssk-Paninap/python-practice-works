import mysql.connector
mydb = mysql.connector.connect (host = "localhost", username = "root", password = "", database = "")

c1 = mydb.cursor()

# sqlform = "insert into ijn (name,rarity) values (%s, %s)"

# ijn = [("Akagi", "SSR"), ("Noshiro", "SSR"), ("Taihou", "SSR"), ("Unzen", "UR")]

# c1.executemany(sqlform,ijn)

insertForm = "insert into royal_navy (name,rarity) values (%s, %s)"
hms = [("Implacable", "UR"), ("Scylla", "SSR"), ("Formidable", "SSR")]

c1.executemany(insertForm,hms)
c1.execute("select * FROM royal_navy")

for i in c1 :
    print (i)

mydb.commit()
