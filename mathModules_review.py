import math
import statistics

numCont =[]
"""
1. Created a loop where in it will continouly ask user for values until user ended it
2. Appends all the values entered by user to the numCont list and uses floor to remove the decimal
"""
while True:
    userInput = float(input("Input values for the list: "))
    
    numCont.append(math.floor(userInput))
    print(f"{userInput} was added to the list")
    
    askQ = input("Would you like to add again? y/n: ")
    
    if askQ != 'y':
        break
"""
Getting the median with the help of statistic library and getting sum of all the values 
entered by user. 
displaying the output of all three (entered values, median, and sum)
"""
getMed = statistics.median(numCont)
total = sum(numCont)
print(f"the sum of the values {numCont} is {total} and median is {getMed}")

