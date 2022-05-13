#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:28:23 2022

@author: shayla
"""
#Exercise with NumPy
import numpy as np
a1 = np.arange(0, 6)
b1 = np.arange(5, -1, -1)
print(a1, '\n', b1)

#####################################################
c1 = np.zeros((6,6), dtype="bool")

for row in range(0,6):
    for col in range(0,6):
        if a1[row] > b1[col]:
            c1[row,col] = True

c1 = c1.astype(int)
#####################################################
import functools
import operator
d1 = np.array([0,0,0,0,0,0])

for i in range(0,6):
    d1[i] = functools.reduce(operator.add, c1[i])
#####################################################

arr1 = np.array([[2, 3, 1],
                 [1, 2, 3]])
arr2 = np.array([[1, 3, 1],
                 [2, 4, 1],
                 [3,2,5]])

final = np.dot(arr1, np.linalg.inv(arr2))
#####################################################
A = [[ 5 ,  -1],[6  , 9]]
B = [[7],[2]]
X = np.linalg.inv(A).dot(B)
#####################################################
ar1 = np.arange(8).reshape(2,2,2)
ar2 = [[1,2],[2,1]]
res= ar1 + ar2
#####################################################







            
        
            

