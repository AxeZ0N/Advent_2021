def checkNode(node, size):                          #takes in (i,j), size
    i,j = node[0], node[1]                          #throws index error if not in array
                                                    #otherwise adds node to seen
    try:
        if node in seen or arr[i][j] == 9 or i < 0 or j < 0 or i > rows-1 or j > cols-1:          #checks RDLU recursively, size+1 at end
            return size
        else:
            seen.append(node)
            size = size + 1

    except IndexError:
        return size

    size = checkNode(move(node, 'right'), size)
    size = checkNode(move(node, 'down'), size)
    # checkNode(move(node, 'left'), size)
    # checkNode(move(node, 'up'), size)
    return size

def move(node, direction):                              #takes in (i,j), "RDLU"e
    i,j = node[0], node[1]                              #value error is for completeness

    try:
        match direction:
            case 'right': return (i,j+1)
            case 'down': return (i+1,j)
            case 'left': return (i,j-1)
            case 'up': return (i-1,j)
            case _: return ValueError
    except ValueError:
        return "Not a direction"



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

seen = []

print(checkNode((0,0), 0))