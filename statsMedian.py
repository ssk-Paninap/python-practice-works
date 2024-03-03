import statistics

def getMedian(a):
    return statistics.median(list(a))
myTupols = (21,32,45,65,23,65,23)
x = getMedian(myTupols)
print(f"{x} is the Median" )   
