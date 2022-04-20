from functools import total_ordering
from os import curdir


numbers_to_call = open('input.txt').readline().split(',')

num_lines = len(open('input.txt').readlines())
num_boards = int((num_lines-1) / 6)

boards = [[] for i in range(num_boards)]

with open('input.txt') as file:
    file.readline()
    file.readline()

    
    for i in range(num_boards):
        curr_line = file.readline()
        
        while curr_line != '\n':
            boards[i].append(curr_line.split())
            curr_line = file.readline()


def check_victory(board):
    counter = 0

    for line in board:
        counter = 0
        for number in line:
            if number == 'x':
                counter += 1
        if counter == 5:
            return True
    
    

    for i in range(5):
        counter = 0
        for j in range(5):
            if board[j][i] == 'x':
                counter += 1
        if counter == 5:
            return True
    
    return False
            

def sum_unused(board):
    counter = 0
    for line in board:
        for number in line:
            if number != 'x':
                counter += int(number)
    return counter

my_break = None
final_num = None

total_winning_boards = num_boards
has_won= [0] * num_boards
for n in numbers_to_call:
    for i in range(num_boards):
        for j in range(5):
            for x in range(5):
                if boards[i][j][x] == n:
                    boards[i][j][x] = 'x'
        if check_victory(boards[i]) == True:
            if has_won[i] == 0:
                if sum(has_won) == num_boards - 1:
                    my_break = boards[i]
                    final_num = n
                    board_num = i
                else:
                    has_won[i] = 1

        
        if my_break != None: break
    if my_break != None: break

sum_board = sum_unused(my_break)

final = sum_board * int(final_num)


for board in boards:
    for line in board:
        for number in line:
            print(f'{number} ',end='')
        print()
    print()


print(f'Sum board = {sum_board}, board num = {board_num}, final number = {final_num}, product = {final}')