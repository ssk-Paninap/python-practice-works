import math
import statistics

numCont =[]

while True:
    userInput = float(input("Input values for the list: "))
    
    numCont.append(math.floor(userInput))
    print(f"{userInput} was added to the list")
    
    askQ = input("Would you like to add again? y/n: ")
    
    if askQ != 'y':
        break
getMed = statistics.median(numCont)
total = sum(numCont)
print(f"the sum of the values {numCont} is {total} and median is {getMed}")

