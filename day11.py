def north(i,j):
    return (i,j-1)

def east(i,j):
    return (i,j+1)

def south(i,j):
    return (i-1,j)

def west(i,j):
    return (i+1,j)

def neast(i,j):
    return (i-1,j+1)

def seast(i,j):
    return (i+1,j+1)

def swest(i,j):
    return (i+1,j-1)

def nwest(i,j):
    return (i-1,j-1)

def checkNum(a):
    i,j = a[0],a[1]

    if i > rows - 1 or i < 0 or j < 0 or j > cols - 1:
        return

    if arr[i][j] == 'F':
        # print(f'arr[{i}][{j}] = {arr[i][j]}')
        return
    
    arr[i][j] += 1

    if arr[i][j] > 9:
        arr[i][j] = 'F'
        checkNear((i,j))
    else:
        return

def checkNear(a):
    i,j = a[0], a[1]
    checkNum(nwest(i,j));   checkNum(north(i,j));   checkNum(neast(i,j))
    checkNum(west(i,j));                            checkNum(east(i,j))
    checkNum(swest(i,j));   checkNum(south(i,j));   checkNum(seast(i,j))

def resetFlashes():
    counter = 0
    i,j = -1,-1
    for line in arr:
        i+=1
        j=-1
        for num in line:
            j+=1
            if num == 'F':
                arr[i][j] = 0
                counter+=1

    return counter

input = open('./input.txt').read().splitlines()

cols = len(input[0])
rows = len(input)

arr = [[0 for i in range(cols)] for j in range(rows)]

i,j = 0,0

for line in input:
    for num in line:
        arr[i][j] = int(num)
        j+=1
    i+=1
    j=0

counter = 0
step = 0
flag = 0
while step < 1000:
    i,j = 0,0
    for line in arr:
        for num in line:
            checkNum((i,j))
            j+=1
        i+=1
        j=0

    flashes = resetFlashes()
    counter += flashes
    if flashes == (rows * cols) and flag != 1:
        flag = 1
        print(f'Synced at step: {step+1}')
    step+=1
    if step == 100:print(counter)

# for line in arr:print(line)
