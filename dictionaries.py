uname = input ("Type your username taht you want: ")
vals = {"Name":"Paninap","Age":20}
vals ["Username"] = uname
print(vals)



bigD = {
    1:{"Name":"Paninap", "Age":20, "Favorite Language": "Javascript"},
    2:{"Name":"User2","Age":"Unknown","Favorite Lnaguage":"NA"}
}
print (bigD[1])
addName = input("Add a third person Name: ")
addAge = input("Add a third person Age: ")
addFav = input("Add a third person Favorite Language: ")


bigD[3] = {"Name":addName,"Age":addAge, "Favorite Language":addFav}

print (bigD)
