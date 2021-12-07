import numpy as np
import collections
testdata = [3,4,3,1,2]

file = 'input/day06_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = inputList[0].split(",")
        inputList = [int(x.strip()) for x in inputList]
    finally:
        reader.close()

realdata = inputList


school = np.array(realdata)

schoolCount = np.array([0 for _ in range(0,10)])

for i in school:
    schoolCount[i] +=1

schoolCount = np.array(schoolCount, dtype=np.int64)

for day in range(1,257):
    print("Day ", day)
    if schoolCount[0] > 0:
        schoolCount[9] += schoolCount[0]
        schoolCount[7] += schoolCount[0]
        schoolCount[0] = 0
    # shift positions
    schoolCount = np.roll(schoolCount,-1)

print(f'after day {day}: {schoolCount}')
print("size:", np.sum(schoolCount))