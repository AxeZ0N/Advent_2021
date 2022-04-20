
myinput = []
mycounter = [0,0,0,0,0,0,0,0]

with open('input.txt') as file:
    for line in file:

        first, second = line.split('|')
        myinput.append(second.split())

    for item in myinput:
        for word in item:
            mycounter[len(word)] += 1


print(myinput)
print(mycounter)

sum = 0

for i in range(9):
    if i == 2 or i == 4 or i == 3 or i == 7:
        sum += mycounter[i]

print(sum)