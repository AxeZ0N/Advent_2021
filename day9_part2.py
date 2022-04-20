class Node:
    def __init__(self, value):
        self.value = value
    
def checkNode(Node, size):
    if Node in seen or Node.value == 9:
        return size
    else:
        seen.append(Node)

def move(node, direction):
    match direction:
        case 'right': return 1


input = open('./input.txt').read().splitlines()

cols = len(input[0])
rows = len(input)

arr = [[0 for i in range(cols)] for j in range(rows)]


i,j = 0,0

for line in input:
    for num in line:
        arr[i][j] = Node(int(num))
        j+=1
    i+=1
    j=0

seen = []

for line in arr:
    for node in line:
        print(node.value, end='')
    print()