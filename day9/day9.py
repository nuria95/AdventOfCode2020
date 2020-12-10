import numpy as np

data = np.loadtxt('input')
preamble_length = 25


def twoSum(data, goal):
    # Make only 1 pass:
    remains = []
    for n in data:
        remain = goal - n
        if remain not in remains:
            remains.append(n)
        else:
            return [n, remain]
    return None

def get_first_wrong(data):
    for i in range(len(data)-preamble_length):
        preamble = data[i:i+preamble_length]
        goal = data[i+preamble_length]
        if twoSum(preamble, goal) is None:
            return goal, i+preamble_length
        
    return []
print('First wrong number is', get_first_wrong(data)[0])

goal_wrong, index_wrong = get_first_wrong(data)

def window_creator(goal, index):
    for start in range(index):
        end = 3 # must be >2 by definition of wrong_number
        window = data[start:start+end]
        while np.sum(window) < goal:
            end +=1
            window = data[start:start+end]
            
        if np.sum(window)==goal:
            # Window is the continugous. Return sum of both min and max
            return np.sort(window)[0]+np.sort(window)[-1]
    
    return []
        
            
print('Result Day 2 is', window_creator(goal_wrong, index_wrong))
        







