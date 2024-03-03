#function to get mean of a given
def getMean(a):
    return statistics.mean(list(a))

#application of the function
myset = (5,5,7,3,7,4,8,9)
x = getMean(myset)
print(f"{x} is the mean of the following given: {myset}")
