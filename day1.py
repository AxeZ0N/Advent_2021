myinput = []

with open('input.txt') as file:
    for line in file:
        myinput.append(int(line))

compare = 0
count = 0

for x in myinput:
    if x > compare and not x == myinput[0]:
        count +=1
        print(f'{x} increase +')
    else:
        print(f'{x} decrease')
    compare = x

print(count)

compare = 0
count = 0

for x in range(len(myinput)):
    a = sum(myinput[x:x+3])
    if a > compare and not x == 0:
        count +=1
        print(f'{myinput[x]} increase +')
    else:
        print(f'{myinput[x]} decrease')
    compare = a
    
print(count)