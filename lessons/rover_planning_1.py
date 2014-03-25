def maze_update(maze, Rover):
    mazehist = np.dstack((mazehist,maze))
    
def hazard(front,maze):
    if (maze[front[0],front[1]] ==3) or (maze[front[0],front[1]] == 5):
        return 'hazard'
    else:
        return 'safe'
def gorover(student_func):
    '''
    student_func should be defined in the iPython notebook namespace and provide directions as text strings, either
    'turn right'
    'turn left'
    'turn around'
    'go forward'
    '''

    import numpy as np
    from numpy.random import random_integers as rand
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    maze02 = np.array([[5,5,5,5,5,5,5,5,5,5],[5,0,0,0,4,0,3,0,0,5],[5,0,0,3,3,3,3,3,3,5]])
    maze35 = np.array([[5,0,0,3,0,0,3,0,3,5],[5,3,0,3,0,0,3,3,0,5],[5,0,0,3,0,0,3,0,0,5]])
    maze69 = np.array([[5,0,0,0,0,0,3,3,0,5],[5,0,0,3,0,0,0,1,3,5],[5,3,0,0,0,0,3,0,0,5],[5,5,5,5,5,5,5,5,5,5]])
    maze = np.append(maze02,maze35,axis = 0)
    maze = np.append(maze,maze69,axis = 0)
    mazehist = maze.copy()

    position = np.array([7,7])
    target =  np.array([1,4])
    heading = np.array([0,-1]) #facing left
    right = np.array([[0,1],[-1,0]]) #rotation matrix for turning right 90 degrees
    left = np.array([[0,-1],[1,0]]) #rotation matrix for turning left 90 degrees
    escape = 0
    numpasses = 0
    while escape == 0:
                        numpasses = numpasses +1
                        maze[position[0],position[1]] = 1
                        if (position[0] == target[0]) and (position[1] == target[1]):
                                        maze[position[0],position[1]] = 1
                                        maze[target[0],target[1]] = 2
                                        escape = 1
                        front = np.add(position,heading)
                        if (maze[front[0],front[1]] ==3) or (maze[front[0],front[1]] == 5):
                                        infront = 'hazard'
                        else:
                                        infront = 'who cares'
                        command = student_func(infront)
                        if command == 'turn right':
                                        heading = right.dot(heading)
                        if command == 'turn left':
                                        heading = left.dot(heading)
                        if command == 'go forward':
                                        position = position + heading
                        if command == 'turn around':
                                        heading = -heading
                        if numpasses == 100:	
                                break
                        mazehist = np.dstack((mazehist,maze))

    fig = plt.figure(figsize=(8,4))

    ims = []
    for i in range(mazehist.shape[2]-1):
        im = plt.imshow(mazehist[:,:,i], cmap=plt.cm.Reds, interpolation='nearest')
        ims.append([im])

    anim = animation.ArtistAnimation(fig, ims, interval=100)

    return anim

    # <codecell>

def goroveragain(student_func):
    '''
    student_func should be defined in the iPython notebook namespace and provide directions as text strings, either
    'turn right'
    'turn left'
    'turn around'
    'go forward'
    '''
    from numpy.random import random_integers as rand
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    maze02 = np.array([[5,5,5,5,5,5,5,5,5,5],[5,0,0,0,4,0,3,0,0,5],[5,0,0,3,3,3,3,3,3,5]])
    maze35 = np.array([[5,0,0,3,0,0,3,0,3,5],[5,3,0,3,0,0,3,3,0,5],[5,0,0,3,0,0,3,0,0,5]])
    maze69 = np.array([[5,0,0,0,0,0,3,3,0,5],[5,0,0,3,0,0,0,1,3,5],[5,0,0,0,0,0,3,0,0,5],[5,5,5,5,5,5,5,5,5,5]])
    maze = np.append(maze02,maze35,axis = 0)
    maze = np.append(maze,maze69,axis = 0)
    mazehist = maze.copy()

    position = np.array([7,7])
    target =  np.array([1,4])
    heading = np.array([0,-1]) #facing left
    right = np.array([[0,1],[-1,0]]) #rotation matrix for turning right 90 degrees
    left = np.array([[0,-1],[1,0]]) #rotation matrix for turning left 90 degrees
    escape = 0
    numpasses = 0
    while escape == 0:
                        numpasses = numpasses +1
                        maze[position[0],position[1]] = 1
                        if (position[0] == target[0]) and (position[1] == target[1]):
                                        maze[position[0],position[1]] = 1
                                        maze[target[0],target[1]] = 2
                                        escape = 1
                        front = np.add(position,heading)
                        left_block = np.add(position,left.dot(heading))
                        if (maze[front[0],front[1]] ==3) or (maze[front[0],front[1]] == 5):
                            if (maze[left_block[0],left_block[1]] ==3) or (maze[left_block[0],left_block[1]] == 5):
                                        infront = 'hazard'
                                        toleft = 'hazard'
                            else:
                                        infront = 'hazard'
                                        toleft = 'who cares'
                        else:
                            if (maze[left_block[0],left_block[1]] ==3) or (maze[left_block[0],left_block[1]] == 5):
                                        infront = 'who cares'
                                        toleft = 'hazard'
                            else:
                                        infront = 'who cares'
                                        toleft = 'who cares'
                        command = student_func(infront,toleft)
                        if command == 'turn right':
                                        heading = right.dot(heading)
                        if command == 'turn left':
                                        heading = left.dot(heading)
                                        position = position + heading
                        if command == 'go forward':
                                        position = position + heading
                        if command == 'turn around':
                                        heading = -heading
                        if numpasses == 100:    
                                break
                        mazehist = np.dstack((mazehist,maze))

    fig = plt.figure(figsize=(8,4))

    ims = []
    for i in range(mazehist.shape[2]-1):
        im = plt.imshow(mazehist[:,:,i], cmap=plt.cm.Reds, interpolation='nearest')
        ims.append([im])

    anim = animation.ArtistAnimation(fig, ims, interval=100)

    return anim

    # <codecell>



