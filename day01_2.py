### get input data:
testdata = [199, 200, 208, 210, 200, 207 ,240, 269, 260, 263]
file = 'input/day01_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList_clean = [int(x.strip()) for x in inputList]
    finally:
        reader.close()

depth = inputList_clean


### calculate number of depth increases
depthsums =[]
for i in range(len(depth)-2): 
    depthsums.append(depth[i] + depth[i+1] + depth[i+2])

depth = depthsums
result = sum([1 for i in range(len(depth)) if depth[i] > depth[i-1]])
print(result)