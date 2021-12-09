testdata = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
testdata = [testdata[0].split(" | ")]

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

digitdict = {
    "0" : "abcefg",
    "1" : "cf",
    "2" : "acdeg",
    "3" : "acdfg",
    "4" : "bcdf",
    "5" : "abdfg",
    "6" : "abdefg",
    "7" : "acf",
    "8" : "abcdefg",
    "9" : "abcdfg"
    }

# 0 = abcefg
# 1 = cf
# 2 = acdeg
# 3 = acdfg
# 4 = bcdf
# 5 = abdfg
# 6 = abdefg
# 7 = acf
# 8 = abcdefg
# 9 = abcdfg

# eval:
# 1 (2) -> cf
# 7 (3) -> a
# 4 (4) -> bcdf
# 8 (7) -> all
# 9 (6) -> e, g (len(6) must contain bcdf(exclude 0) and not cf(exclude 6))
# 6 (6) -> c, f (len(6) must contain c||f)
# 3 (5) -> d (len(5) must contain c&&f)
# 4 (4) -> b 

def eval_patterns(patternlist):
    # print("patternlist: ", patternlist)
    for pattern in patternlist:
        if len(pattern) == 2:
            cf = list(pattern)
        elif len(pattern) == 3:
            acf = list(pattern)
        elif len(pattern) == 4:
            bcdf = list(pattern)
        elif len(pattern) == 7:
            abcdefg = list(pattern)
    # return [cf, acf, bcdf, abcdefg]
    for pattern in patternlist:
        # find 0 and 6 and 9
        if len(pattern) == 6:
            if not set(bcdf).issubset(set(pattern)) and not set(cf).issubset(set(pattern)):
                abdefg = list(pattern)
                # print("6: ", abdefg)
            elif set(bcdf).issubset(set(pattern)):
                abcdfg = list(pattern)
                # print("9: ", abcdfg)
            elif not set(bcdf).issubset(set(pattern)) and set(cf).issubset(set(pattern)):
                abcefg = list(pattern)
                # print("0: ", abcefg)
        # find 3
        elif len(pattern) == 5:
            if set(cf).issubset(set(pattern)):
                acdfg = list(pattern)
                # print("3: ", acdfg)
    
    a = list(set(acf) - set(cf))[0]
    e = list(set(abcdefg) - set(abcdfg))[0]
    g = list(set(abcdfg) - set(acf) - set(bcdf))[0]
    c = list(set(cf) - set(abdefg))[0]
    f = list(set(cf) - set(c))[0]
    d = list(set(acdfg) - set(acf) -set(g))[0]
    b = list(set(bcdf) -set(cf) - set(d))[0]
    # print("a: ", a)
    # print("e: ", e)
    # print("g: ", g)
    # print("c: ", c)
    # print("f: ", f)
    # print("d: ", d)
    # print("b: ", b)
    return {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g}

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def mapConnections(digitlist, mappingdict):
    digits = []
    for digit in digitlist:
        digitstring = []
        for segment in digit:
            digitstring.append(getKeysByValue(mappingdict, segment))
        # flatten list
        digitstring = ''.join(sorted([item for sublist in digitstring for item in sublist]))
        dig = getKeysByValue(digitdict, digitstring)
        # print(f'segments for digit: {digitstring} - {dig}')
        digits.append(dig)
    digits = ''.join([item for sublist in digits for item in sublist])
    # print("digits: ", digits)
    return int(digits)

patterns = [x[0].split(" ") for x in data]
output = [x[1].split(" ") for x in data]
# print("patterns: ", patterns)
# print("outputs: ", output)


results= []

for line in range(len(output)):
    mappingdict = eval_patterns(patterns[line])
    # print(mappingdict)
    num_out = mapConnections(output[line], mappingdict)
    print(f'line: {line} - {num_out}')
    results.append(num_out)

print("results: ", results)
print(sum(results))


