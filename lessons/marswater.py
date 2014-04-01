import numpy as np
import random

def iswater():
    my_list = [1] * 24 + [0] * 76
    array = np.zeros((15,15))
    howmuch = np.zeros((15,15))
    for x in range(0,len(array)):
        for y in range(0,len(array)):
            array[x,y] = random.choice(my_list)
    for x in range(0,len(array)):
        for y in range(0,len(array)):
            if array[x,y] == 1:
                howmuch[x,y] = random.random()*3
            else:
                howmuch[x,y] = 0
    return howmuch
    
