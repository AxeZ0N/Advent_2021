

X = 0
Y = 0
aim = 0

my_input = []

with open('input.txt') as file:
    for line in file:
        direction,value = line.split()
        match direction:
            case 'forward':
                X += (int(value))
                Y += (int(value) * aim)
            case 'backward':
                X -= (int(value) * aim)
            case 'up':  aim -= int(value)
            case 'down':  aim += int(value)



print(f'X final = {X}, Y final = {Y}\nProduct = {X*Y}')
        