### get input data:
testdata = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
file = 'input/day02_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList_clean = [str(x.strip()) for x in inputList]
    finally:
        reader.close()

movements = inputList_clean

### calculate distance
dist_h = 0
dist_v = 0
for movement in movements:
    dir = movement.split(" ")[0]
    dist = movement.split(" ")[1]
    if dir == 'forward': 
        dist_h += int(dist)
    else:
        if dir == 'up':
            dist_v -= int(dist)
        else:
            dist_v += int(dist)


print (f'h: {dist_h}')
print (f'v: {dist_v}')
print (f'mult: {dist_h * dist_v}')

