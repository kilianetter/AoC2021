import numpy as np

testdata = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
    ]
testdata2 = [
    "11111",
    "19991",
    "19191",
    "19991",
    "11111"
    ]

file = 'input/day11_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = [str(x.strip()) for x in inputList]
        # inputList = [str(x.strip()) for x in inputList]
        realdata = inputList
    finally:
        reader.close()


octofield = realdata
octofield = np.array([[int(octo) for octo in line] for line in octofield])

print("step: 0 - inital state")
print(octofield)

# all direct neigbours including diagonals
# NW,N,NE,W,E,SW,S,SE
neighbors = [
    (-1,-1),
    (-1,0),
    (-1,+1),
    (0,-1),
    (0,+1),
    (+1,-1),
    (+1,0),
    (+1,+1),     
]

shpy = np.shape(octofield)[0]-1
shpx = np.shape(octofield)[1]-1

def isValidOcto(y, x, field):
    return (x >= 0 and x <= shpx and
            y >= 0 and y <= shpy) and field[y,x] != 0

flashes = []

def flash(field):
    # print("func input field")
    print(field)
    flashing = np.where(field > 9)
    field[flashing] = 0
    # field_before = np.copy(field)
    flashing = [(flashing[0][i], flashing[1][i]) for i in range(np.shape(flashing)[1])]
    print(flashing, " have flashed")
    if len(flashing)>0:
        flashes.append(flashing)
    # print("flashcoord: ", flashing)
    for octoy,octox in flashing:
        #increase neighbour energy level
        # print("checking neighbor to: ", octoy, octox)
        for n in neighbors:
            y, x = n
            nx = octox + x
            ny = octoy + y
            # print(n, ny,nx)
            # print(isValidOcto(ny,nx, field))
            if isValidOcto(ny,nx, field):
                # print("adding 1 to neighbor ", ny,nx)
                field[ny,nx] += 1

    if len(flashing)>0:
        # print("recursion occured!")
        field = flash(field)
        return field
    else:
        return field


for step in range(1,196):
    octofield +=1
    octofield = flash(octofield)
    print("end of step ", step, ":")
    print(octofield)
    print("\n=============================================")

print("\n result: ") 
print(octofield)
print(flashes)
foo = sum([len(f) for f in flashes])
print(foo)




