import numpy as np
import time

data = np.loadtxt('input.txt')
goal = 2020

# Day 1
def twoSum(data):
    for i, n in enumerate(data):
        for r in data[i:]:
            if r == goal - n:
                partial_sol = [n, r]
                return partial_sol
                    
def twoSum_optimized(data):
    # Make only 1 pass:
    remains = []
    for n in data:
        remain = goal - n
        if remain not in remains:
            remains.append(n)
        else:
            return [n, remain]

    return []




t=time.time()
partial_sol = twoSum(data)
print('Time twoSum', time.time()-t)
print('Sol Day 1.1 is:', partial_sol[0]*partial_sol[1])

t = time.time()
partial_sol_optim = twoSum_optimized(data)
print('Time twoSumOptim', time.time()-t)
print('Sol Day 1.1 optimized is:', partial_sol_optim[0]*partial_sol_optim[1])

# Day 1.2:


def threeSum(data):
    for i, n in enumerate(data):
        goal1 = goal - n
        for j, m in enumerate(data[i:]):
            for o in data[j:]:
                if o == goal1 - m:
                    partial_sol = [n, o, m]
                    return partial_sol


partial_sol = threeSum(data)
print('Sol Day 1.2 is:', partial_sol[0]*partial_sol[1]*partial_sol[2])
