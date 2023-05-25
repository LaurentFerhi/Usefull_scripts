# -*- coding: utf-8 -*-
"""
Random walk for fatigue load signal generation
"""

__author__ = 'Laurent FERHI'
__date__ = '2023-05-24'
__version__ = '0.1'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def random_walk(start,end,length,maxStep,tolerance,floorAvg,maxiter=500):
    
    minGap = np.inf # gap at link between forward and backward
    best_res = [] # to store best result
    iteration = 0 # keep track of iterations
    
    while minGap > tolerance and iteration < maxiter:
    
        ys = start
        ye = end

        forward, backward = [],[]

        # build signal from both ends
        for k in range(length//2):
            forward.append(ys)
            backward.append(ye)
            
            # if signal average < floor Avg, push random choice to be > 0
            if np.mean(forward) < floorAvg:
                ys+=np.random.uniform(0,maxStep)
            else:
                ys+=np.random.uniform(-maxStep,maxStep)
                
            if np.mean(backward) < floorAvg:
                ye+=np.random.uniform(0,maxStep)
            else:
                ye+=np.random.uniform(-maxStep,maxStep)

        l = forward + backward[::-1] # join the 2 halves

        # gap at link between forward and backward lists
        gap = max([np.abs(l[i]-l[i-1]) for i in range(1,len(l))])
        
        if gap < minGap:
            best_res = l
            minGap = gap
            
        iteration +=1
    
    return np.array(best_res)

if __name__ == "__main__":
    
    
    for _ in range(5):
    
        fat_signal = random_walk(
            start=0,end=0,length=500,maxStep=10,tolerance=20,floorAvg=10
            )
        
        fig,ax = plt.subplots(figsize=(12,4))
        plt.plot(fat_signal)
