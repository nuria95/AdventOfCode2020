import numpy as np

data = np.sort(np.loadtxt('input'))
# Add voltage of outlet
data = np.insert(data, 0, 0)
# Add voltage of your device
data = np.insert(data, len(data), data[-1]+3)


def compute_differences(data, step):
    data_substract = data[step::]

    data_substract = np.concatenate(
        (data_substract,
         np.zeros((len(data)-len(data_substract)),)))
    differences = data_substract - data
    # Do not report boundary values
    return differences[:-step]

differences = compute_differences(data, step=1)
print('Solution Day10.1', len(
    differences[differences == 1])*len(differences[differences == 3]))


# Day 2:
last_element = data[-1]

# dictionary: {'adpater_value': number of different paths to connect to it}
dict_tree = {0:1}

for adapter in data[1:]: # we already added the 0 element before entering the loop
    # Add entry in dict_tree
    dict_tree[adapter]=0

    # See with which adapters I can connect and add number of valid paths:
    if adapter - 1 in dict_tree:
        dict_tree[adapter] += dict_tree[adapter-1]

    if adapter - 2 in dict_tree:
        dict_tree[adapter] += dict_tree[adapter-2]

    if adapter - 3 in dict_tree: 
        dict_tree[adapter] += dict_tree[adapter-3]

num_combinations = dict_tree[last_element]
print('Solution Day 10.2 Num combinations', num_combinations)
