import re

myinput = []
grid = [[0 for i in range(1000)] for j in range(1000)]

myinput=[]

with open('input.txt') as file:
    for line in file:

        temp_nums = [x for x in re.findall('\d+',line)]
        myinput.append(temp_nums)

    for i in range(len(myinput)):
        y1, x1, y2, x2 = [int(x) for x in myinput[i]]
        
        # if not x1 == x2:
        #     if not y1 == y2:  #uncomment for part 1
        #         continue

        grid[x1][y1] += 1
        while not x1 == x2 or not y1 == y2:

            if not x1 == x2:
                x1 = x1+1 if x1 < x2 else x1-1

            if not y1 == y2:
                y1 = y1+1 if y1 < y2 else y1-1

            grid[x1][y1] += 1

counter = 0

for line in grid:
    for item in line:
        counter = counter + 1 if item >= 2 else counter

print(counter)