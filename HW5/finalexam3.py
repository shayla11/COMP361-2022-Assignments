#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:36:56 2022

@author: shayla


import re

#p = re.compile(r'^\D*(\d+).*$')
p = re.compile(r'^\height:\')
p1 = re.compile(r'^\D*(\d+)\D+(\$?\d+\.\d{1,2}|\$\d+)\D*$')             
p2 = re.compile(r'^\D*(\$?\d+\.\d{1,2}|\$\d+)\D+(\d+)\D*$')

with open('contribs.txt') as f:
    line_num = 0
    contributions = {}
    for line in f:
        line_num +=1
        m1 = p1.search(line)
        if m1:
            mem, amount = m1.groups()
            if amount[0] == '$': amount = amount[1:]
            contributions[mem] = float(amount)
        else:
            m2 = p2.search(line)
            if m2:
                amount, mem = m2.groups()
                if amount[0] == '$': amount = amount[1:]
                contributions[mem] = float(amount)
            else:
                print('Line {0:d} is ill formed: {1:s}'.format(
                    line_num, line), end="")
#print(contributions)

print("\nmember | Contribution")
print('-'*22)
for mem, contrib in contributions.items():
    print('   {0:2s}  | ${1:5.2f}'.format(mem, contrib))

print("\nContributions total ${0:.2f}.".format(
    sum([v for v in contributions.values()])))
    
import operator
mx = max(contributions.items(), key=operator.itemgetter(1))
print("Member {0:s} contributed the most, ${1:.2f}.".format(mx[0], mx[1]))
"""
import re

p = re.compile(r'^height: ([0-9]+-[0-9].) *name: [a-zA-Z]+ [a-zA-Z]+$')
with open('data.txt') as f:
    for line in f:
        if line.find("-") == -1:
            print("Ill-formed: ", line)
        else:
            dash = line.index("-")
            feet = line[dash-1]
            inches = line[dash+1:dash+3]
            new_inches = re.sub('[!@#$. ]', '', inches)
            
            new_feet = float(feet) + float(inches)/12
            meters = str(round(float(new_feet)/3.281,2))
            print(meters)
            
        
    