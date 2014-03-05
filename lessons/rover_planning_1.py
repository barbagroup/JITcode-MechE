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
    right = np.array([[0,1],[-1,0]]) #rotation matrix for turning left 90 degrees
    left = np.array([[0,-1],[1,0]]) #rotation matrix for turning right 90 degrees
    escape = 0
#    plt.figure(figsize=(10, 5))
    while escape == 0:
            maze[position[0],position[1]] = 1
            if (position[0] == target[0]) and (position[1] == target[1]):
                    maze[position[0],position[1]] = 1
                    maze[target[0],target[1]] = 2
                    escape = 1
            next = np.add(position,heading)
            if (maze[next[0],next[1]] ==3) or (maze[next[0],next[1]] == 5):
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
            #plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
            #plt.xticks([]), plt.yticks([])
            #plt.show()
            #print(position, heading)
            mazehist = np.dstack((mazehist,maze))

    fig = plt.figure(figsize=(8,4))

    ims = []
    for i in range(mazehist.shape[2]-1):
        im = plt.imshow(mazehist[:,:,i], cmap=plt.cm.Reds, interpolation='nearest')
        ims.append([im])

    anim = animation.ArtistAnimation(fig, ims, interval=100)

    return anim


    # <codecell>


