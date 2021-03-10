#!/usr/bin/env python3

import numpy as np
import random

def fill_matrix():
    
    array = np.empty((10,10),dtype=np.float32)
    
    rows = array.shape[0]
    columns = array.shape[1]
    
    for i in range(0,rows):
        for j in range(0,columns):
            array[i,j] = random.randint(0,40)
    
    print(array)

if __name__ == "__main__":
    fill_matrix()