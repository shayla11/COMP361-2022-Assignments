#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:14:44 2022

@author: shayla
"""

'''
Write a Python script that has a global variable increment with value 5 and defines a function
add_increment() that is passed a list ls of integers and returns a list identical to ls but with
each element incremented by increment. Type the global variable, the argument to function
add_increment() (a list of integers), and the return value of add_increment(). Submit this
script. You should also run Mypy on it, but you need not submit anything relating to that. 
'''



def add_increment(ls):
    for i in range(len(ls)):
        ls[i] += increment
        
increment = 5
num_list = [1,2,3,4,5]

add_increment(num_list)