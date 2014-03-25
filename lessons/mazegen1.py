import numpy as np	
import matplotlib.pyplot as plt

maze02 = np.array([[5,5,5,5,5,5,5,5,5,5],[5,0,0,0,4,0,3,0,0,5],[5,0,0,3,3,3,3,3,3,5]])
maze35 = np.array([[5,0,0,3,0,0,3,0,3,5],[5,3,0,3,0,0,3,3,0,5],[5,0,0,3,0,0,3,0,0,5]])
maze69 = np.array([[5,0,0,0,0,0,3,3,0,5],[5,0,0,3,0,0,0,1,3,5],[5,3,0,0,0,0,3,0,0,5],[5,5,5,5,5,5,5,5,5,5]])
maze = np.append(maze02,maze35,axis = 0)
maze = np.append(maze,maze69,axis = 0)
plt.figure(figsize=(10, 5))
plt.imshow(maze, cmap=plt.cm.Reds, interpolation='nearest')
plt.xticks([]), plt.yticks([])
plt.show()