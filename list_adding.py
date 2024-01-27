userNum = input("Input three numbers separated by comma: ")
numCut = userNum.split(',')
nums = [int(num) for num in numCut]
allSum = sum(nums)

print(f"The sum of three numbers: {allSum}")
