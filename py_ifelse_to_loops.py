for i in range (1,11):
    for j in range (1,11):
        ans = i * j 
        print (f"{ans}", end = " ")
    print("\n")
    

age = input("Type age: ")
newAge = int(age)
print (type(newAge))

if newAge >= 18 and newAge <= 59:
    print ("You are old enough")
    
elif newAge >= 60 :
    print("Too old")
    
else :
    print("either you're a kid or a dumbass")
    

def ageClass (a):
    if a < 18 :
        print("please leave this program")
    else : 
        print("continue with your journey")

ageClass(newAge)

b = "hello guys"

print (b[6:10])

print (b[:6])


num1 = int("21") #casting making this a data type to another
num2 = int(33.45)
num3 = float(3) #casting an int into a float to become 3.0
print (f"This are the results {num1}, {num2} and {num3}")

val1 = 21

if val1 % 2 == 0 :
    print(f"{val1} is an even number")
    
elif val1 % 2 != 0:
    print (f"{val1} is an odd number")
    
else:
    print(f"invalid {val1} is not a number")


    