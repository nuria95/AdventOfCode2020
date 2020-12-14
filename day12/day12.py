import time
from math import sin, cos, pi, atan2
input_file = open('input', 'r')
instructions = input_file.read().splitlines()
vertic_actions = ['N', 'S']
horiz_actions = ['W', 'E']
ang_actions = ['L', 'R']

# Part 1:
def get_pose_part1(pose):
    # Coordinate 0 is rows = 'y axis', coordinate 1 is cols = 'x axis'
    for i in instructions:
        action = i[0]
        value = int(i[1:])
        if action in horiz_actions:
            pose[1] += value * (-1 if action == 'W' else 1)
        
        elif action in vertic_actions:
            pose[0] += value * (-1 if action == 'S' else 1)
        
        elif action in ang_actions:
            # + angle counterclockwise
            pose[2] += value * (1 if action == 'L' else -1) 
            if abs(pose[2])>=360:
                pose[2] = pose[2]%360
            if pose[2]<0:
                pose[2] = pose[2]+360

        elif action == 'F':
            angle_rads = pose[2]*pi/180 
            pose[0] += int(sin(angle_rads)*value)
            pose[1] += int(cos(angle_rads)*value)
            
    return pose

t0=time.time()
initial_pose = [0, 0, 0]  # ['X,Y,ANGLE counterclockwise +]
pose = get_pose_part1(initial_pose)
print('Manhattan distance is:', abs(pose[0])+ abs(pose[1]))
print((time.time()-t0)*1000, ' ms')


# Part 2:
def get_pose_part2(pose, waypoint):
    # Coordinate 0 is rows = 'y axis', coordinate 1 is cols = 'x axis'
    for i in instructions:
        action = i[0]
        value = int(i[1:])
        if action in horiz_actions:
            waypoint[1] += value * (-1 if action == 'W' else 1)

        elif action in vertic_actions:
            waypoint[0] += value * (-1 if action == 'S' else 1)

        elif action in ang_actions:
            # Rotate vector waypoint by angle: + counterclockwise
            angle_rads = value * pi/180 * (-1 if action == 'R' else 1)
            # Default x_ in axis frame is coordinate 1 (not 0) here.
            x_ = cos(angle_rads)*waypoint[1] - sin(angle_rads)*waypoint[0]
            y_ = sin(angle_rads)*waypoint[1] + cos(angle_rads)*waypoint[0]
            
            waypoint[0]=y_
            waypoint[1]=x_

        elif action == 'F':
            pose[0]+=waypoint[0]*value
            pose[1] += waypoint[1]*value
    return pose

waypoint = [1,10] # [x,y]
pose = [0,0,0]
t0 = time.time()
initial_pose = [0, 0, 0]  # ['X,Y,ANGLE]
pose = get_pose_part2(initial_pose, waypoint)
print('Manhattan distance is:', abs(pose[0]) + abs(pose[1]))
print((time.time()-t0)*1000, ' ms')
