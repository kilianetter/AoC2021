import numpy as np
testdata = [3,4,3,1,2]

file = 'input/day06_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = inputList[0].split(",")
        inputList = [int(x.strip()) for x in inputList]
    finally:
        reader.close()

realdata = inputList
print(realdata)


school = np.array(testdata)


for day in range(1,81):
    spawners = np.where(school == 0)
    for spawner in spawners:
        school[spawner] = 7
    new_fish = np.array([8 for _ in range(0, np.size(spawners))])
    print(f'day# {day}: adding {np.size(new_fish)}')
    school = school-1
    school = np.append(school, new_fish)

print(f'after day {day}: {school}')
print("size:", np.size(school))