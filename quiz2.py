#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:56:17 2022

@author: shayla
"""

def thresh_list(ls, thresh=0):
    ls = [num for num in ls if num > thresh ] 
    return ls

def intersect_lists(ls1, ls2):
    ls = [num for num in ls2 if num in ls1 and num in ls2]
    return ls

def thresh_dict(d, thresh=0):
    newd = {}
    for key in d:
        if d[key] >= thresh:
            newd[key] = d[key]
    return newd

def his_thresh_dict(d, thresh=0):
    return {key: v for key, v in d.items() if v >= thresh}


            
        
 
    
hi = thresh_list([1,2,3,4,5,6,7], 3)
hello = intersect_lists([1, 3, 5, 7, 2,1], [2, 4 ,1])
heyo = thresh_dict({'a': 2, 'b': 7, 'c': 4, 'd': 8, 'e': 5}, 5)
hey = thresh_dict({'a': -3, 'b': 5, 'c': -4, 'd': 2, 'e': -1, 'f': 0})
happy = his_thresh_dict({'a': -3, 'b': 5, 'c': -4, 'd': 2, 'e': -1, 'f': 0})





