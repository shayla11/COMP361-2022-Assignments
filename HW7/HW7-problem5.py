#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:06:05 2022

@author: shayla
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=10)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    
    theta = np.linspace(0, 4, 1000) 
    x = np.sin(2 * np.pi * (theta[0:4] - .01 * i))
    y = np.cos(2 * np.pi * (theta[0:4] - .01 * i))
    
    line.set_data(x, y)
    return line, 

anim = FuncAnimation(fig, animate, init_func=init,
               frames=200, interval=20, blit=True)
writergif = animation.PillowWriter(fps=30) 
anim.save('problem5.gif', writer=writergif)









