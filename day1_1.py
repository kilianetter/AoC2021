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

print(len(depth))

### calculate number of depth increases 
counter = 0
for i in range(len(depth)):
     if depth[i] > depth[i-1]:
         counter +=1
# this should yield the same result
result = sum([1 for i in range(len(depth)) if depth[i] > depth[i-1]])

print(result)
print(counter)
