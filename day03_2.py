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

o2 = ''
co2 = ''


def keep(list, index, high):
    newlist = []
    if high == True:
        value = '1'
    else:
        value = '0'
    for item in list:
        if item[index] == value:
            newlist.append(item)
        else:
            pass
    return newlist

report_o2 = report
### Report O2
for i in range(len(report_o2[0])):
    gen = True
    digit = 0
    for reading in report_o2:
        digit += int(reading[i])
    if gen == True:
        if digit >= (len(report_o2)/2):
            high = True
        else:
            high = False
    else:
        if digit >= (len(report_o2)/2):
            high = False
        else:
            high = True
    report_o2 = keep(report_o2, i, high)
    if len(report_o2) == 1:
        break
o2 = report_o2[0]
print(o2)

report_co2 = report

### Report CO2
for i in range(len(report_co2[0])):
    gen = False
    digit = 0
    for reading in report_co2:
        digit += int(reading[i])
    if gen == True:
        if digit >= (len(report_co2)/2):
            high = True
        else:
            high = False
    else:
        if digit >= (len(report_co2)/2):
            high = False
        else:
            high = True
    report_co2 = keep(report_co2, i, high)
    if len(report_co2) == 1:
        break
co2 = report_co2[0]


print (f'gamma: 0b{o2} - {int(o2, base=2)}')
print (f'epsilon: 0b{co2} - {int(co2, base=2)}')
lifesupport = int(o2, base=2) * int(co2, base=2)
print(f'consumption: {lifesupport}')