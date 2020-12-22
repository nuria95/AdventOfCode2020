import numpy as np
import math
import matplotlib.pyplot as plt
input_file = open('day13/input', 'r')
schedule = input_file.read().splitlines()

earliest_time = int(schedule[0])
buses_ids = [int(i) for i in schedule[1].split(',') if i != 'x']

# Get time in the last trip (earliest_time % ids) and then substract total time to
# get time left to arrival


def compute_waiting_times(first_depart_time):
    return np.abs([first_depart_time % ids - ids for ids in buses_ids])


def prime_factors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i:  # not divisible
            i += 1
        else:  # divisible
            n = n//i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return factors


# Part 1
wait_times = compute_waiting_times(earliest_time)
print('Solution Part1: ', np.min(wait_times) * buses_ids[np.argmin(wait_times)])


#  # Part 2 Brute Force approach:
# goal_wait_times = [i for i in range(
#     len(schedule[1].split(','))) if schedule[1].split(',')[i] != 'x']
# future_schedules = buses_ids.copy()

# t = buses_ids[0]

# while not all([(t + wait) % bus_id == 0 for wait, bus_id in zip(goal_wait_times[:], buses_ids[:])]):
#     # future_schedules = [i+j for i,j in zip(future_schedules, buses_ids)]
#     t += buses_ids[0]

# print(t)

# # Part 2 optimized:

# Bus periods are all prime. If I have some solution t
# for the first n buses, any increment of the products of all previous periods
# is the next smallest solution for buses up to n.
# I keep incrementing until I find a solution that works for bus n+1 as well.

def part2():
    goal_wait_times = [i for i in range(
        len(schedule[1].split(','))) if schedule[1].split(',')[i] != 'x']
    t = buses_ids[0]
    n = 1  # num buses solved

    # wait times from bust 0 to n+1
    current_wait_times = compute_waiting_times(t).tolist()[1:n+1]
    # Start with increments of size bus 0 id.
    increment = math.prod(buses_ids[0:n])
    while True:
        # Do not use compute_wait times function because there are
        # waiting times of bus_id > bus_id in some cases.
        if all([(t + wait) % bus_id == 0 for wait, bus_id in zip(goal_wait_times[:n+1], buses_ids[:n+1])]):
            n += 1
            increment = math.prod(buses_ids[0:n])
            if n == len(buses_ids):
                return t
        t = t + increment


t = part2()
print('Solution Part 2: ', t)
