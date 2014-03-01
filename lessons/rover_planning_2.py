# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as plt

def student_func(infront):
    if infront == 'wall':
        return 'turn right'
    else:
        return 'go forward'

maze02 = np.array([[5,5,5,5,5,5,5,5,5,5],[5,0,0,0,4,0,3,0,0,5],[5,0,0,3,3,3,3,3,3,5]])
maze35 = np.array([[5,0,0,3,0,0,3,0,3,5],[5,3,0,3,0,0,3,3,0,5],[5,0,0,3,0,0,3,0,0,5]])
maze69 = np.array([[5,0,0,0,0,0,3,3,0,5],[5,0,0,3,0,0,0,1,3,5],[5,0,0,0,0,0,3,0,0,5],[5,5,5,5,5,5,5,5,5,5]])
maze = np.append(maze02,maze35,axis = 0)
maze = np.append(maze,maze69,axis = 0)
pos_0 = np.array([7,7])
position = pos_0
target =  np.array([1,4])
heading = np.array([0,-1]) #facing left
right = np.array([[0,1],[-1,0]]) #rotation matrix for turning left 90 degrees
left = np.array([[0,-1],[1,0]]) #rotation matrix for turning right 90 degrees
escape = 0
plt.figure(figsize=(10, 5))
while escape == 0:
	maze[position[0],position[1]] = 1
	if (position[0] == target[0]) and (position[1] == target[1]):
		maze[position[0],position[1]] = 1
		maze[target[0],target[1]] = 2
		escape = 1
	next = np.add(position,heading)
	if (maze[next[0],next[1]] ==3) or (maze[next[0],next[1]] == 5):
		infront = 'wall'
	else:
		infront = 'who cares'
	command = student_func(infront)
	print(command)
	if command == 'turn right':
		heading = right.dot(heading)
	if command == 'turn left':
		heading = left.dot(heading)
	if command == 'go forward':
		position = position + heading
	if command == 'turn around':
		heading = -heading
	plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
	plt.xticks([]), plt.yticks([])
	plt.draw()
	print(position, heading)
print('made it!')




# <codecell>


