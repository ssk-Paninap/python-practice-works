#creating an empty list for containing all input values from user
inputCont = []
#created a loop whre this is supposed to continually add values to the list until user stops it
while True:
    x = float(input(f"Input value for the list: "))
    inputCont.append(math.floor(x))
    
    userAns = input("Do you wanna add again? y/n: ")
    """
    Condition where if user did not put y then the program ends
    """
    if userAns != 'y':
        break
"""
Display all the values user added after the user stop adding values

long commments para maganda tingnan HAHAHAHAHHAHA
"""
print(inputCont)
