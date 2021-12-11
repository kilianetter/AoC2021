import numpy as np

testdata = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

file = 'input/day10_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = [str(x.strip()) for x in inputList]
        # inputList = [str(x.strip()) for x in inputList]
        inputList = inputList
    finally:
        reader.close()

realdata = inputList

print(realdata)
print([len(line) for line in testdata])

subsystem = realdata

# carry over all lines with even len
# completeLines = [line for line in subsystem if len(line) %2 == 0 ]
# print(completeLines)


class Chonk:

    def __init__(self, lineList):
        self.openChunksDict = {"(": 0, "[": 0, "{": 0, "<": 0}
        self.closeChunksDict = {")": 0, "]": 0, "}": 0, ">": 0}
        self.oppositesList = [("(",")"), ("[","]"),("{","}"), ("<",">")]
        self.opencnt = 0
        self.closecnt = 0
        self.lineList = lineList
        self.score = 0

    def resetDict(self):
        self.openChunksDict = {"(": 0, "[": 0, "{": 0, "<": 0}
        self.closeChunksDict = {")": 0, "]": 0, "}": 0, ">": 0}
        self.opencnt = 0
        self.closecnt = 0
        self.score = 0

    def countOpenClose(self, line):
        for char in line:
            if char == "(" or char == "[" or char == "{" or char == "<":
                self.openChunksDict[char] += 1
            elif char == ")" or char == "]" or char == "}" or char == ">":
                self.closeChunksDict[char] += 1
        for key, val in self.openChunksDict.items():
            self.opencnt += val
        for  key, val in self.closeChunksDict.items():
            self.closecnt += val
        counter = [self.opencnt, self.closecnt]
        # print("")
        # print(line)
        # print(self.opencnt, self.closecnt)
        # print("open: ", self.openChunksDict)
        # print("close: ", self.closeChunksDict)
        self.resetDict()
        return counter


    def isComplete(self, line):
        if len(line) %2 != 0:
            return False
        else:
            counter = self.countOpenClose(line)
            if counter[0] != counter[1]:
                return False
            else:
                return True

    def isCorrupt(self, line):
        charList = [char for char in line]
        openChunk = []
        index = 0
        for char in charList:
            if char in ["(", "[", "{", "<"]:
                openChunk.append(char)
            elif char == ")":
                if openChunk[-1] != '(':
                    print(f'{char} at index {index}')
                    self.score += 3
                    return char
                else: openChunk.pop()
            elif char == "]":
                if openChunk[-1] != '[':
                    print(f'{char} at index {index}')
                    self.score += 57
                    return char
                else: openChunk.pop()
            elif char == "}":
                if openChunk[-1] != '{':
                    print(f'{char} at index {index}')
                    self.score += 1197
                    return char
                else: openChunk.pop()
            elif char == ">":
                if openChunk[-1] != '<':
                    print(f'{char} at index {index}')
                    self.score += 25137
                    return char
                else: openChunk.pop()
            index +=1
        return 0
    
    def returnLines(self, mode = "complete"):
        if mode == "complete":
            return [line for line in self.lineList if self.isComplete(line)]
        elif mode == "corrupt":
            return [line for line in self.lineList if self.isCorrupt(line)]
        elif mode == "all":
            return [line for line in self.lineList]

    def scoreCorrupt(self):
        corruptChars = [line for line in self.lineList if self.isCorrupt(line)]
        print(corruptChars)
        return self.score

c= Chonk(subsystem)
# print(c.returnLines(mode="corrupt"))
print(c.scoreCorrupt())
