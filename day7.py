import re
myinput = []

with open('input.txt') as file:
    for line in file:

        myinput.append([int(x) for x in re.findall('\d+',line)])

fuel = 10000000000
tfuel = 10000000000

avg = int(round(sum(myinput[0]) / len(myinput[0])))

# for i in range(10000):
#     fuel = tfuel if tfuel < fuel else fuel
#     tfuel = 0
#     for sub in range(len(myinput[0])):
#         sub_pos = myinput[0][sub]
#         base_fuel = abs(sub_pos - i)
#         tfuel += sum(range(base_fuel+1))

tfuel = 0
for sub in range(len(myinput[0])):
    sub_pos = myinput[0][sub]
    base_fuel = abs(sub_pos - (avg+1))
    tfuel += sum(range(base_fuel+1))

print(tfuel)
