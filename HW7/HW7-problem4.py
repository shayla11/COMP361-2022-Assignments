#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:32:43 2022

@author: shayla
"""

import math
import matplotlib.pyplot as plt

def update_lists(x,y,z,m,x1,y1,z1,m1):
    x.append(x1)
    y.append(y1)
    z.append(z1)
    m.append(m1)
    
x0, x1 ,y0, y1,z0, z1, m0, m1 = [], [], [], [], [], [], [], []

with open("data.txt") as file:
    for line in file:
        tokens = line.strip().split()
        x,y,z,m = [float(i) for i in tokens[:-1]]
        if tokens[-1] == "0":
            update_lists(x0,y0,z0,m0,x,y,z,m)
        elif tokens[-1] == "1":
            update_lists(x1,y1,z1,m1,x,y,z,m)
        else:
            print("Ill-formed line: " + line.strip())
            
m0 = [math.pi*i**2 for i in m0]
m1 = [math.pi*i**2 for i in m1]

ax = plt.axes(projection="3d")
ax.scatter(x0,y0,marker="^", s=m0, color='r' )
ax.scatter(x1,y1,marker="o", s=m0, color='b' )
plt.title("A 3D scatter plot")
plt.savefig("scatter plot problem 4")
plt.show()


            
