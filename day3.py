from os import altsep


f=0

with open('input.txt') as file:
    for line in file:
        b = len(line)
        f += 1
        file.close()
        break

b-=1

my_input = []

one_positions = [0] * b
zero_positions = [0] * b

with open('input.txt') as file:
    for line in file:
        my_input.append(str(line))
        for bit in range(b):
            if str(line)[bit] == '1':
                one_positions[bit] += 1
            else:
                zero_positions[bit] += 1


print(one_positions)
print(zero_positions)

gamma = ''
epsilon = ''

for x in range(b):
    if one_positions[x] > zero_positions[x]:
        gamma+=('1')
        epsilon+=('0')
    else:
        gamma+=('0')
        epsilon+=('1')

print(gamma)
print(epsilon)

gamma1 = int(gamma, 2)
epsilon1 = int(epsilon, 2)

part_2a_list = my_input.copy()

# print('OXYGEN')
curr_pos = 0
while len(part_2a_list) > 1:
    zero_count = 0
    one_count = 0
    # print(part_2a_list)

    for item in part_2a_list:
        match item[curr_pos]:
            case '1' : one_count +=1
            case '0' : zero_count +=1
    
    majority = '1' if one_count >= zero_count else '0'
    i=0
    # print(f'bit = line[{curr_pos}], majority = {majority}')
    while i < len(part_2a_list):
        test_value = part_2a_list[i]
        # print(f'line: [{str(test_value).strip()}]', end='')
        if test_value[curr_pos] != majority:
            # print(' ***REMOVING***',end='')
            part_2a_list.remove(test_value)
            i-=1
    
        # print()
        i+=1
    curr_pos+=1
        
oxygen = part_2a_list[0]

part_2b_list = my_input.copy()

print('\nCO2\n')

# print(part_2b_list)

curr_pos = 0
while len(part_2b_list) > 1:
    zero_count = 0
    one_count = 0
    # print(part_2b_list)

    for item in part_2b_list:
        match item[curr_pos]:
            case '1' : one_count +=1
            case '0' : zero_count +=1
    
    majority = '0' if zero_count <= one_count else '1'
    i=0
    # print(f'bit = line[{curr_pos}], majority = {majority}')
    while i < len(part_2b_list):
        test_value = part_2b_list[i]
        # print(f'\t\tline: [{str(test_value).strip()}]', end='')
        if test_value[curr_pos] != majority:
            # print(' ***REMOVING***',end='')
            part_2b_list.remove(test_value)
            i-=1
    
        # print()
        i+=1
    curr_pos+=1
        
co2 = part_2b_list[0]

oxygen1 = int(oxygen,2)
co21 = int(co2,2)

print(f'\nOxygen = {oxygen1}, CO2 = {co21}, Product = {oxygen1 * co21}\n')


