import numpy as np
import time
data = np.loadtxt('day11/input', dtype=str)
seat_map = list(map(list, data))


def pad_map(data):
    padded_map = []
    num_rows = len(seat_map)
    num_cols = len(seat_map[0])
    
    padded_map.append(['N']*(num_cols+2))
    for row in data:
        row.insert(0,'N')
        row.append('N')
        padded_map.append(row)
    padded_map.append(['N']*(num_cols+2))
    return padded_map  

def get_neighbors(seat_map, row, col ):
    neighs = []
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if not (c == col and r == row):
                neighs.append(seat_map[r][c])
    return neighs


def get_neighbors_part2(seat_map, row, col):
    num_rows, num_cols = len(seat_map), len(seat_map[0])
    neighs = []
    directions = [[i, j] for i in [0, 1, -1]
                  for j in [0, 1, -1] if not (i == j and i == 0)]
    
    for dire in directions:
        nr, nc = dire
        r = nr
        c = nc
        while (0 <= (row+r) <= num_rows) and (0 <= (col+c) <= num_cols) and \
        seat_map[row+r][col+c] == '.':
            r+=nr
            c+=nc
        if seat_map[row+r][col+c] != '.':
            neighs.append(seat_map[row+r][col+c])
    return neighs
    
# Part1:
t0 = time.time()
seat_map = pad_map(seat_map)
# !! seat_map.copy() doesnt copy lists inside of list!
new_seat_map = [seat_map[x].copy() for x in range(len(seat_map))]

def convergence_part1(seat_map, new_seat_map):
    
    equal_maps = False
    num_iters = 0
    while not equal_maps:
        num_iters +=1
        seat_map = [new_seat_map[x].copy() for x in range(len(new_seat_map))]
        for row in range(1,len(seat_map)-1):
            for col in range(1,len(seat_map[0])-1):
                if seat_map[row][col] == '.':
                    continue
                neighbors = get_neighbors(seat_map, row, col)
                if seat_map[row][col]=='L':
                    if neighbors.count('#') == 0:
                        new_seat_map[row][col]='#'
                elif seat_map[row][col]=='#':
                    if neighbors.count('#') >=4:
                        new_seat_map[row][col] = 'L'
        
        equal_maps = (seat_map == new_seat_map)
    return seat_map
    

seat_map = convergence_part1(seat_map, new_seat_map)
print('Num of occupied seats after convergence',
np.sum([seat_map[i].count('#') for i in range(len(seat_map))]))       
t1 = time.time()
print((t1-t0)*1000, ' ms')


# Part2:
t0 = time.time()
seat_map = list(map(list, data))
seat_map = pad_map(seat_map)
# !! seat_map.copy() doesnt copy lists inside of list!
new_seat_map = [seat_map[x].copy() for x in range(len(seat_map))]

def convergence_part2(seat_map, new_seat_map):
    num_rows=len(seat_map)
    num_cols=len(seat_map[0])
    equal_maps = False
    while not equal_maps:
        seat_map = [new_seat_map[x].copy() for x in range(len(new_seat_map))]
        for row in range(1, len(seat_map)-1):
            for col in range(1, len(seat_map[0])-1):
                if seat_map[row][col] == '.':
                    continue
                neighbors = get_neighbors_part2(seat_map, row, col)
                if seat_map[row][col] == 'L':
                    if neighbors.count('#') == 0:
                        new_seat_map[row][col] = '#'
                elif seat_map[row][col] == '#':
                    if neighbors.count('#') >= 5:
                        new_seat_map[row][col] = 'L'

        equal_maps = (seat_map == new_seat_map)
    return seat_map

seat_map = convergence_part2(new_seat_map, seat_map)
print('Num of occupied seats after convergence',
       np.sum([seat_map[i].count('#') for i in range(len(seat_map))]))
t1 = time.time()
print((t1-t0)*1000, ' ms')
