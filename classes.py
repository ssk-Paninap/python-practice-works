class Adder():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def addNum(self):
        return self.num1 + self.num2
    
tot = Adder(21,23)
print(tot.addNum())
