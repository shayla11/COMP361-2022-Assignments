#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:16:23 2022

@author: shayla
"""

import matplotlib.pyplot as plt

f = open("ints.txt")

numbers = [int(i) for i in f.readlines()]
f.close()

max_num = max(numbers)
freq = {}

for i in numbers:
    freq[i] = freq.get(i,0)+1
for i in range(max_num+1):
    if i not in freq:
        raise Exception((f'No elements {i}, with max = {max_num}'))
        
items = sorted(freq.items())

vals = [i[1] for i in items]
max_ind = vals.index(max(vals))

explode=[0]*(max_num+1)
explode[max_ind] = .1
fig,ax = plt.subplots()
ax.pie(vals, labels=list(range(0, max_num+1)), shadow=True, autopct='%1.1f%%', explode=explode)
plt.title('Relative frequencies of the numbers')
plt.savefig('pie problem 3')
plt.show()
