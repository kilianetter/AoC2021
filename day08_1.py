testdata = [16,1,2,0,4,2,7,1,2,14]

file = 'input/day08_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = [x.strip().split(" | ") for x in inputList]
        # inputList = [str(x.strip()) for x in inputList]
        inputList = inputList
    finally:
        reader.close()
realdata = inputList

data = realdata

output = [x[1].split(" ") for x in data]
out_len = [int(len(x)) for line in output for x in line]


foo = [out_len.count(i) for i in [2,3,4,7]]
print(sum(foo))
