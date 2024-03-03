import statistics
#function to get median of a given (will be converted to list if it is a tuple)
def getMedian(a):
    #return the median
    return statistics.median(list(a))
#Example
myTupols = (21,32,45,65,23,65,23)
x = getMedian(myTupols)
#displaying the Median
print(f"{x} is the Median" )   
