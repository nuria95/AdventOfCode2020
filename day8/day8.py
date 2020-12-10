import numpy as np


def instr_code(data):
    command = 0
    accumulator = 0
    done_commands = []
    final_code_reached = False
    while command not in done_commands:
        try:
            instr = data[command]
        except IndexError:
            final_code_reached = True
            break
        action, number = instr[0], int(instr[1])
        if action == 'nop':
            done_commands.append(command)
            command +=1

        if action == 'acc':
            done_commands.append(command)
            command +=1
            accumulator +=number
        
        if action == 'jmp':
            done_commands.append(command)
            command += number
    return accumulator, final_code_reached

def find_indeces(data):
    # Find indeces that I can change
    indices = [i for i, x in enumerate(data) if "nop" in x or  'jmp' in x]
    return indices


data = np.loadtxt('input', dtype=str)
# Day 8.1:
print('Value of accumulator Day8.1', instr_code(data)[0])

# Day 8.2:
indeces = find_indeces(data)
accumulator, final_code_reached = instr_code(data)

i=0
words = set(['jmp','nop'])
while not final_code_reached:
    temp_data = data.copy()
    # Change jmp to nop or inverse:
    temp_data[indeces[i]][0] = list(words-set([data[indeces[i]][0]]))[0]
    accumulator, final_code_reached = instr_code(temp_data)
    i+=1
    

print('Value of accumulator Day8.2', accumulator)
