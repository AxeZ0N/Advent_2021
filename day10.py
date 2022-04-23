input = open('./input.txt').read().splitlines()

cols = len(input[0])
rows = len(input)

arr = [0 for i in range(cols)]

closers = ')]}>'
syms = str('(){}[]<>')

fixedStrings = []

myCount = 0.0

for line in input:
    i = -1
    stack = []
    for c in line:
        i += 1
        if i == len(line) - 1:
            print('Incomplete')
            fixedString = ""
            if c not in closers:
                stack.append(c)
            else:
                stack.pop()
            while stack:
                closerNeeded = syms[syms.index(stack.pop()) + 1]
                fixedString += closerNeeded
            fixedStrings.append(fixedString)
            break
        if len(stack) == 0:
            stack.append(c)
        else:
            myOpener = stack.pop()
            if c in closers:
                if c == syms[syms.index(myOpener) + 1]:
                    continue
                else: 
                    # print(f'Wrong: Expected: {syms[syms.index(myOpener) + 1]}, Got: {c}')
                    input[input.index(line)] = ''
                    match c:
                        case ')': myCount += 3
                        case ']': myCount += 57
                        case '}': myCount += 1197
                        case '>': myCount += 25137
                    break
            else:
                stack.append(myOpener)
                stack.append(c)
    # print('Correct')

totalCounts = []
day1 = sum(totalCounts)
print(day1)

for item in fixedStrings:
    myCount = 0.0
    for c in item:
        myCount = myCount * 5
        match c:
            case ')': myCount += 1
            case ']': myCount += 2
            case '}': myCount += 3
            case '>': myCount += 4

    totalCounts.append(myCount)

totalCounts.sort()

half = len(totalCounts)
half = half -  1
half = int(half / 2)
print(half)
print(totalCounts[half])