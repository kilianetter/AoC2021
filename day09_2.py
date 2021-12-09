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

ridges = np.where(heightmap == 9)
basins = np.where(heightmap != 9)

heightmap[basins] = 0
heightmap[ridges] = 1

print(heightmap)

basinlist = []


### Depth First Search 
# adapted from source: 
# https://www.geeksforgeeks.org/find-number-of-islands/
# refer to:
# https://en.wikipedia.org/wiki/Depth-first_search
# takes boolean matrix of basins (0) and ridges (1)
# delineates and counts basins
class Graph():

    # todo:
    # so many things....
    # get shape from array / matrix
    # setable basin/ridge value

    def __init__(self, row, col, zmap):
        self.COLS = col
        self.ROWS = row
        self.zmap = zmap
        self.basin = []
        self.basinlist = []

        print(row, col)
        print(zmap)

    # returns true if cell is valid
    # i.e. not visited, or out of bounds
    # lastly basins are indicated by zero values
    def isSafeToVisit(self, y, x, visited):
        return (x >= 0 and x < shpx and 
                y >= 0 and y < shpy and 
                not visited[y,x] and self.zmap[y,x] == 0)

    # recursively check neighbors in xnbr ynbr
    def checkNeighbors(self, y,x, visited):
        ynbr = [-1, 1, 0, 0]
        xnbr = [0, 0, -1 ,1]
        visited[y,x] = True
        for i in range(4):
            if self.isSafeToVisit(y + ynbr[i], x + xnbr[i], visited):
                self.basin.append(self.checkNeighbors(y + ynbr[i], x + xnbr[i], visited))
        return (y, x)

    def findBasins(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = np.array([[False for x in range(self.COLS)]for y in range(self.ROWS)])
  
        # traverse through the all cells of zmap
        for y in range(0,self.ROWS):
            for x in range(0,self.COLS):
                # If a cell with value 0 is not visited yet, 
                # then new basin found
                self.basin = []
                if visited[y,x] == False and self.zmap[y,x] == 0:
                    print(f'visiting {y}, {x}')
                    # Visit all cells in this island 
                    self.basin.append(self.checkNeighbors(y, x, visited))
                    self.basinlist.append(self.basin)
                    print(f'found basin at {y}, {x} with size {len(self.basin)}')
    def getBasinList(self):
        self.findBasins()
        return self.basinlist 


g = Graph(shpy, shpx, heightmap)
basList = g.getBasinList()
basinSizes = np.array(sorted([len(basin) for basin in basList], reverse=True))
# result:
print(np.prod(basinSizes[0:3]))