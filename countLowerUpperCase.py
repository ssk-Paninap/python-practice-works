def countUpLow(string):
    caseL = 0
    caseUP = 0
    
    for char in string:
        if char.isupper():
            caseUP +=1
        elif char.islower():
            caseL += 1
            
    return f"Lower case is {caseL} and uppercase is {caseUP}"
        
word = input("type a word with upper and lowercase: ")

counted = countUpLow(word)
print (counted)
