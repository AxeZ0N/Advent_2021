import re

myinput = []

with open('input.txt') as file:
    for line in file:

        myinput.append([int(x) for x in re.findall('\d+',line)])
        

counter = 80
# print(f't-19 {myinput}')

while counter > 0:
    for number in range(len(myinput[0])):
        myinput[0][number] -= 1

        if myinput[0][number] < 0:
            myinput[0].append(8)
            myinput[0][number] = 6
    # print(f't-{counter} {myinput}') 
    counter -= 1

    if counter % 10 == 0:
        print(f'    working:{counter} remaining')

total = 0

for item in myinput[0]:
    total += 1

print(total)

