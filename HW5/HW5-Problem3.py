#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:27:25 2022

@author: shayla
"""
import re

def f(matchobj):
    return str(int(matchobj.groups()[1]) + int(matchobj.groups()[2]))
    
def change_the_ouput(input_file, output_file):
    p = re.compile(r'\(((\d+), (\d+))\)')
    with open(input_file, "r") as infi, open(output_file, "w") as oufi:
        oufi.write("The combined scores of Team 1 and Team 2\n")
        infi.readline()
        for line in infi:
                oufi.write(p.sub(f, line))
            
        
change_the_ouput("scores.txt", "scores_output.txt")