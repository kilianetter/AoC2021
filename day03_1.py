testdata = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
file = 'input/day03_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList_clean = [str(x.strip()) for x in inputList]
    finally:
        reader.close()
realdata = inputList_clean

report = realdata

gamma = ''
epsilon = ''

for i in range(len(report[0])):
    digit = 0
    for reading in report:
        digit += int(reading[i])
    if digit > (len(report)/2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print (f'gamma: 0b{gamma} - {int(gamma, base=2)}')
print (f'epsilon: 0b{epsilon} - {int(epsilon, base=2)}')
power = int(gamma, base=2) * int(epsilon, base=2)
print(f'consumption: {power}')