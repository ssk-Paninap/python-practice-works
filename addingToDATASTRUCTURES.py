cont = () #TUPLE
cont1 = [] #List
cont2 = set() #an empty set but if not empty curly braces
cont3 = {} #Dict

val1 = input("Add any text to be included in the array: ")

cont = cont + (val1,) #to add stuff in tuple

cont1.append(val1) #add stuff in list
cont1 += ["stuff","another stuff"] #another way sa list

cont2.add(val1) #add stuff in set

cont3["stuff"] = val1 #add stuff in dict

print(cont)
print(cont1)
print(cont2)
print(cont3)

#if a newly created set has first to not have any value then
#parenthesis should be used even if it will have many contents in the future 
#but if a set will be created alongside many values the curly brace is to be used

