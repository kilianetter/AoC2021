import numpy as np

testdata = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
    ]

file = 'input/day09_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = [str(x.strip()) for x in inputList]
        # inputList = [str(x.strip()) for x in inputList]
        inputList = inputList
    finally:
        reader.close()
realdata = inputList


heightmap = realdata
for y in range(len(heightmap)):
    heightmap[y] = [int(x) for x in heightmap[y]]

heightmap = np.array(heightmap)

shpy, shpx = heightmap.shape

print(heightmap)
print(shpy, shpx)

slopes = []
for y in range(0,shpy):
    for x in range(0,shpx):
        N = False
        S = False
        W = False
        E = False
        pos = heightmap[y,x]
        
        if y-1 < 0 or y-1 > shpy:
            up = np.nan
            N = True
        else:
            up = heightmap[y-1,x]
            if (pos-up) < 0:
                N = True
        
        if y+1 < 0 or y+1 >= shpy:
            down = np.nan
            S = True
        else:
            down = heightmap[y+1,x]
            if (pos-down) < 0:
                S = True

        if x-1 < 0 or x-1 > shpx:
            left = np.nan
            W = True
        else:
            left = heightmap[y,x-1]
            if (pos-left) < 0:
                W = True

        if x+1 < 0 or x+1 >= shpx:
            right = np.nan
            E = True
        else:
            right = heightmap[y,x+1]
            if (pos-right) < 0:
                E = True

        mat = np.array([[0,N,0],[W,0,E],[0,S,0]])
        # print(x,y)
        # print(mat)
        slopes.append(sum(sum(mat)))


slopes = np.array(slopes)
lp = np.where(slopes == 4)
counter = np.size(lp)
print(f'there are {counter} depressions')
print(f'at {lp}')

# risk = [1+heightmap.flatten()[p] for p in lp]
risk = sum(1+heightmap.flatten()[lp])
print(risk)