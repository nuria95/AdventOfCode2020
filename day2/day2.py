import numpy as np
import re

data = np.loadtxt('input', delimiter='\n', dtype=np.str)

       
def count_valid_policy1(data):
    valid_pw = 0
    for i in range(len(data)):
        line = data[i]
        policy, pw = line.split(':')[0], line.split(':')[1]

        lower_bound, upper_bound, letter = \
        (int(re.split('-| ', policy)[0]), 
        int(re.split('-| ', policy)[1]),
        re.split('-| ', policy)[2])

        if lower_bound <= pw.count(letter) <= upper_bound:
            valid_pw +=1

    return valid_pw

print('Num valid pw is', count_valid_policy1(data))


def count_valid_policy2(data):
    valid_pw = 0
    for i in range(len(data)):
        line = data[i]
        policy, pw = line.split(':')[0], line.split(':')[1]

        pos1, pos2, letter = \
            (int(re.split('-| ', policy)[0]),
             int(re.split('-| ', policy)[1]),
             re.split('-| ', policy)[2])

        if (pw[pos1] == letter and not pw[pos2] == letter) or \
            (not pw[pos1] == letter and pw[pos2] == letter):
            valid_pw += 1

    return valid_pw


print('Num valid pw is', count_valid_policy2(data))
