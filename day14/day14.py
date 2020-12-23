import numpy as np
import itertools
input_file = open('day14/input', 'r')
instructions = input_file.read().splitlines()



num_bits = 36
def decimal_to_bits(n):
    """
        : adds formatting options for this variable(otherwise it would represent decimal n)
        0numbits formats the number to eight digits zero-padded on the left
        b converts the number to its binary representation

    """
    return f'{n:0{num_bits}b}'

def bits_to_decimal(s):
    return int(s, 2)

def apply_mask(n, mask):
    for i, val in enumerate(mask):
        if val == 'X':
            pass
        else:
            n[int(i)]=val
    return bits_to_decimal(''.join(n))

def floating_to_addresses(n):
    floating_indexes = np.where(np.array(n) == 'X')[0].tolist()
    for comb in itertools.product('01', repeat=len(floating_indexes)):
        temp_n = n.copy()
        for i, index in enumerate(floating_indexes):
            temp_n[index]=comb[i]
        yield bits_to_decimal(''.join(temp_n))



def apply_mask_part2(n, mask):
    for i, val in enumerate(mask):
        if val == '0':
            pass
        else:
            n[int(i)] = val
    
    new_addresses = []
    new_addresses.append(list(floating_to_addresses(n)))
    return new_addresses


# # Part 1:
memory = {}
for instr in instructions:
    
    if instr.split()[0] == 'mask':
        mask = [char for char in instr.split()[-1]]
        
    else:
       
        address, value = int(instr.split()[0][4:-1]), int(instr.split()[2])
        binary = [char for char in decimal_to_bits(value)]
        masked_decimal = apply_mask(binary, mask)
        memory[address]=masked_decimal

total = 0      
for values in memory.values():
    
    total+=values

print('Part1:', total)

# # Part 2:
memory = {}
for instr in instructions:

    if instr.split()[0] == 'mask':
        mask = [char for char in instr.split()[-1]]

    else:

        address, value = int(instr.split()[0][4:-1]), int(instr.split()[2])
        binary = [char for char in decimal_to_bits(address)]
        new_addresses = apply_mask_part2(binary, mask)[0]
        for ad in new_addresses:
            memory[ad] = value

total = 0
for values in memory.values():

    total += values

print('Part2:',total)


       
