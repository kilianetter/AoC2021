testdata = [16,1,2,0,4,2,7,1,2,14]

file = 'input/day07_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = inputList[0].split(",")
        inputList = [int(x.strip()) for x in inputList]
    finally:
        reader.close()
realdata = inputList


positions = realdata

def moveit(positions, target):
    # check if valid position
    dist = 0
    fuel = 0
    for pos in positions:
        n = abs(int(pos) - int(target))
        # Gauss'sche Summenformel
        fuel += (n*(n+1)) / 2
        dist += n
    return dist, fuel

fuel_arr = []
dist_arr = []

for pos in range(min(positions),max(positions)+1):
    dist, fuel = moveit(positions, pos)#
    dist_arr.append(dist)
    fuel_arr.append(fuel)

# print(positions)
# print(dist_arr)
# print(fuel_arr)

print("distance: ", min(dist_arr))
print("fuel: ", min(fuel_arr))