"""
This code are just functions for adding numbers & appending to a dictionary 
"""
import statistics
myList = []
myDict = {"a": 23,"b":87,"c":90,"d":13,"e":3}

def addNums(a,b):
    return a + b
    
num1 = myDict["a"]
num2 = myDict["e"]

num3 = myDict["b"]
num4 = myDict["d"]

tot = addNums(num1,num2)
tot2 = addNums(num3,num4)

print (f"Sum of {num1} & {num2} is : {tot}")
print (f"Sum of {num3} & {num4} is : {tot2}")

def addVal(x):
    return myList.append(x)
    
addVal(tot)
addVal(tot2)

print(f"{myList} are all the values in the list")
print(f"{sum(myList)} is the sum of all the items")




