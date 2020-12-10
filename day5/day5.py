import numpy as np

data = np.loadtxt('input',dtype=str)
max_rows = 127
max_cols = 7
max_seat_id = 0

def get_row(info):
    row = [0,max_rows]
    for e in info:
        if e == 'F':
            row[1]=np.floor((row[1]-row[0])/2+row[0])
        else:
            row[0] = np.ceil((row[1]-row[0])/2+row[0])
    return row[0]

def get_col(info):
    col= [0, max_cols]
    for e in info:
        if e == 'L':
            col[1] = np.floor((col[1]-col[0])/2+col[0])
        else:
            col[0] = np.ceil((col[1]-col[0])/2+col[0])
    return col[0]


occupied_seats = []    
for board in data:
   row = get_row(board[0:7])
   col = get_col(board[7::])
   seat_id = row*8 + col
   occupied_seats.append(seat_id)

   if seat_id > max_seat_id:
       max_seat_id = seat_id

print('Max seat id is', max_seat_id)

print('All non occupied seats are', set(np.arange(0,max_seat_id)) - set(occupied_seats))
