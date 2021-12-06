testdata = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
    ]

file = 'input/day05_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList_clean = [str(x.strip()) for x in inputList]
    finally:
        reader.close()
realdata = inputList_clean


linemap = realdata

# manage data
lines = []
minx, maxx, miny, maxy = ([] for _ in range(4)) 
for line in linemap:
    begin, end = line.split(" -> ")
    x1, y1 = begin.split(",")
    x2, y2 = end.split(",")

    line = [( int(x1),int(y1) ), ( int(x2),int(y2) )]
    lines.append(line)

print(f'{len(lines)} lines over all')

def getSlope(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    try:
        slope = dx/dy
        return int(slope)
    except:
        return 0

def isNotDiagonal(line, mode):
    # consider only vertical and horizontal lines
    result = False
    # horizontal
    if line[0][0] == line[1][0] and mode == "h":
        #print(f'vertical: {line}')
        result= True
    #vertical
    if line[0][1] == line[1][1] and mode == "v":
        #print(f'horizontal: {line}')
        result= True
    if abs(getSlope(line[0], line[1])) == 1 and mode == "d":
        print(f'diagonal(slope={getSlope(line[0], line[1])}): {line}')
        result= True
    return result

# min max coord
minx = min([min([value[0][0],value[1][0]]) for value in lines])
maxx = max([max([value[0][0],value[1][0]]) for value in lines])
miny = min([min([value[0][1],value[1][1]]) for value in lines])
maxy = max([max([value[0][1],value[1][1]]) for value in lines])
print("minx ", minx, " - maxx ", maxx)
print("miny ", miny, " - maxy ", maxy)


h = [line for line in lines if isNotDiagonal(line, mode="h")]
v = [line for line in lines if isNotDiagonal(line, mode="v")]
d = [line for line in lines if isNotDiagonal(line, mode="d")]
lines = h + v + d

print(f'{len(lines)} lines left')
print(f'horizontal: {len(h)} - vertical: {len(v)} - diagonal: {len(d)}')


import numpy as np
from numpy.lib.function_base import diff

matrix = np.zeros((maxy+1, maxx+1), dtype=int)
print(f'shape: {matrix.shape}')

def swap_xy(p1, p2):
    t1 = p1
    p1 = p2
    p2 = t1
    return p1, p2

def plot(lines, matrix):
    for line in lines:
        print("x1", line[0][0], " x2 ", line[1][0])
        print("y1", line[0][1], " y2 ", line[1][1])
        # plot horizontal
        if line[0][1] == line[1][1]:
            y = line[0][1]
            x1, x2 = line[0][0], line[1][0]
            if x1 > x2:
                x1, x2 = swap_xy(x1,x2)
            print(f'plotting on row {y}')
            for x in range(x1,x2+1):
                matrix[y,x] +=1
        # plot vertical
        elif line[0][0] == line[1][0]:
            x = line[0][0]
            y1, y2 = line[0][1], line[1][1]
            if y1 > y2:
                y1, y2 = swap_xy(y1,y2)
            print(f'plotting on col {x}')
            for y in range(y1,y2+1):
                matrix[y,x] +=1
        else:

            x1, x2 = line[0][0], line[1][0]
            # if x1 > x2:
            #     x1, x2 = swap_xy(x1,x2)
            y1, y2 = line[0][1], line[1][1]
            # if y1 > y2:
            #     y1, y2 = swap_xy(y1,y2)
            print(f'plotting diagonal from {x1} {y1} to {x2} {y2}')
            s = getSlope(line[0], line[1])
            i=0
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                for x in range(min(x1,x2), max(x1,x2)+1,1):
                    y = range(min(y1,y2), max(y1,y2)+1)[i]
                    matrix[y,x] +=1
                    i+=1
            else:
                for x in range(min(x1,x2), max(x1,x2)+1, 1):
                    y = range(max(y1,y2), min(y1,y2)-1, -1)[i]
                    matrix[y,x] +=1
                    i+=1
    return matrix


ventmap = plot(lines, matrix)

ventcount = np.count_nonzero(ventmap >=2)
print(ventcount)

in_low = np.amin(ventmap)
in_high = np.amax(ventmap)
out_low = 0
out_high = 255
for i in range(len(ventmap)):
    ventmap[i] = (ventmap[i] - in_low) * ((out_high - out_low)/(in_high-in_low)) + out_low



from PIL import Image as im
data = im.fromarray(ventmap.astype(np.uint8))
data.show()
# saving the final output 
# as a PNG file
data.save('ventmap.png', 'PNG')