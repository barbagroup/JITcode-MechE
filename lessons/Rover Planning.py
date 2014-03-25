# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from numpy.random import random_integers as rand
import matplotlib.pyplot as plt

def student_func(maze, position, heading):
    "dummy; the student's premade function will need to go here."
    infront = maze[position[0]+heading[0],position[1]+heading[1]]
    been_here = maze[position[0],position[1]]
    if infront == 3 :
        if been_here == 0:
            return 'turn right' 
        if been_here == 1:
            return 'turn left'
        else :
            return'turn right'
    else:
        return 'go forward'
def maze_gen(width=81, height=51, complexity=.75, density=.75):
    "example maze generation (adapted) from wikipedia.  works nicely and complexity/density can be changed."
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=int)
    # Fill borders
    Z[0, :] = Z[-1, :] = 3
    Z[:, 0] = Z[:, -1] = 3
    # Make isles
    for i in range(density):
        #make "seeds" around which to make the walls
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 3
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 3
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 3
                    x, y = x_, y_
    return Z
 
size = [50,50]
position = np.array([rand(1,size[1]-1), rand(1,size[0]-1)]) #start at a random position.  may be better to make this a fixed position, 
target =  np.array([rand(1,size[1]-1), rand(1,size[0]-1)])
heading = np.array([0,-1]) #facing up
right = np.array([[0,1],[-1,0]]) #rotation matrix for turning left 90 degrees
left = np.array([[0,-1],[1,0]]) #rotation matrix for turning right 90 degrees
maze = maze_gen(size[0],size[1], complexity=.2, density=.2) #build our maze (dummy for now, we might want more "directions" in the maze)
#make sure position is not interfering with maze wall
while maze[position[0],position[1]] == 3:
    position = np.array([rand(1,size[1]-1), rand(1,size[0]-1)]) #start at a random position.  may be better to make this a fixed position, or find a place in the existing grid
# make sure targe is not interfering with maze wall
while maze[target[0],target[1]] ==3:
    target =  np.array([rand(1,size[1]-1), rand(1,size[0]-1)])
escape = 0
while escape == 0:
    command = student_func(maze, position, heading)
    if command == 'turn right':
        heading = right.dot(heading)
    if command == 'turn left':
        heading = left.dot(heading)
    if command == 'go forward':
        if maze[position[0],position[1]] == 0:
            maze[position[0],position[1]] = 1
        elif maze[position[0],position[1]] == 1:
            maze[position[0],position[1]] = 2
        else :
            maze[position[0],position[1]] = 1
        position = position + heading
        if position.all == target.all:
            maze[position[0],position[1]] = 1
            maze[target[0],target[1]] = 2
            escape = 1
            #mark cell#
    if command == 'turn around':
        heading = -heading
    plt.figure(figsize=(10, 5))
    plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()
    print(position, heading)
print('done')

plt.figure(figsize=(10, 5))
plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
plt.xticks([]), plt.yticks([])
plt.show()



# <codecell>


