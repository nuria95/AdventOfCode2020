import numpy as np
# a='#'
# print(type(a))

data = np.loadtxt('input', delimiter = '\t', comments=None,dtype=str)
len_line = len(data[0])

def countTrees(num_right, num_down):
    col = 0
    numtrees = 0
    for row in range(num_down,len(data),num_down):
        
        col += num_right
       
        if col > len_line-1:
            col = col % len_line
      
        if data[row][col] =='#':
            numtrees +=1
    return numtrees

print('Num trees Day3.1:  ', countTrees(num_right=3, num_down=1))


num_steps = [[1,1],[3,1],[5,1],[7,1],[1,2]]
num_trees = 1
for num_right, num_down in num_steps:
    num_trees *= countTrees(num_right, num_down)

print('Num trees Day3.2:     ',num_trees)
