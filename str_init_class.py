'''
class named Arithmetic which has the functions for 
                        addition,subtraction and multiplication
'''
class Arithmetic:
    #__init__ means initialize (we can initialize variables here)
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    #__str__ is a dunder method which shows a string representation of what will be shown 
    def __str__(self):
        return f"{self.n1} ({self.n2})"
    
    def addNum(self):
        return self.n1 + self.n2
    
    def subNum(self):
        return self.n1 - self.n2
    
    def prodNum(self):
        return self.n1 * self.n2
    
axe = Arithmetic(23,32)

print(axe.prodNum())
