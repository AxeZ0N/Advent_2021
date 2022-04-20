import re
from math import ceil

myinput = []

with open('input.txt') as file:
    for line in file:

        myinput.append([int(x) for x in re.findall('\d+',line)])
        

list_ages = [0,0,0,0,0,0,0,0,0]

for i in range(len(myinput[0])):
    list_ages[myinput[0][i]] += 1
counter = 0

while counter < 256:
    
    print(list_ages)

    temp = list_ages[0]
    list_ages[0] = list_ages[1]
    list_ages[1] = list_ages[2]
    list_ages[2] = list_ages[3]
    list_ages[3] = list_ages[4]
    list_ages[4] = list_ages[5]
    list_ages[5] = list_ages[6]
    list_ages[6] = list_ages[7] + temp
    list_ages[7] = list_ages[8]
    list_ages[8] = temp

    counter += 1

print(sum(list_ages))



