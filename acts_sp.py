
# Act 1
a = 10
b = 50
c =89

xsum = a + b + c
diff = a - b - c
prod = a * b * c
ave = (a + b + c)/3

print("the sum is :",xsum)
print ("the difference is :",diff)
print ("the product is :",prod)
print ("the average is :",ave)

# Act 2

a = int (input ("Num 1: "))
b = int (input ("Num 2: "))


if a > b :
    print (f"{a} is greater than {b}")
    print (f"{b} is lower than {a}")
elif b > a:
    print (f"b = {b} is greater than a: {a}")
    print (f"{a} is lower than {b}")
elif a == b :
    print(f"both values are equal to each other {a}, {b}")
else :
    print ("invalid")


#Act 3
a = int(input("type Year:"))

if a % 4 == 0 :
    print("Leap year")

elif a % 4 != 0 :
    print ("not")
    
else :
    print ("invalid")
    

#Act 4
print ("n n^2 n^3")
for i in range (0,6):
    print ( i**1, i**2, i **3)
        
        
        
        



