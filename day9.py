def left(i,j):
    return arr[i][j-1]

def right(i,j):
    return arr[i][j+1]

def up(i,j):
    return arr[i-1][j]

def down(i,j):
    return arr[i+1][j]

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

lowestPos = []




for i in range(rows):
    for j in range(cols):

        currRow = i
        currCol = j
        currHgt = arr[currRow][currCol]

        if currRow != 0:
            upNbr = up(currRow,currCol)
        else:
            upNbr = 99

        if currRow != rows-1:
            downNbr = down(currRow,currCol)
        else:
            downNbr = 99

        if currCol != 0:
            leftNbr = left(currRow,currCol)
        else:
            leftNbr = 99

        if currCol != cols-1:
            rightNbr = right(currRow,currCol)
        else:
            rightNbr = 99

        if upNbr > currHgt:
            if downNbr > currHgt:
                if leftNbr > currHgt:
                    if rightNbr > currHgt:
                        lowestPos.append((currRow,currCol))


total = 0

for i in range(rows):
    for j in range(cols):
        if (i,j) in lowestPos:
            total = total + 1 + arr[i][j]

print(total)