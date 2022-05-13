#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:04:52 2022

@author: shayla
"""


def split_dict(x, d):
    d1, d2 = {}, {}
    for key in d:
        if d[key] <= x:
            d1[key] = d[key]
        else:
            d2[key] = d[key]
    tup = (d1, d2) 
    return tup
            


    
d = dict([('a', 2), ('b', 10), ('c', 2), ('d', 9), ('e', 5)])
x = 3
print(split_dict(x, d))
print()

f = open("data.txt", 'r')
s = f.readlines()
f.close()
f1 = open("output1.txt", "w")
f2 = open("output2.txt", "w")

counter = 0
#output first file
for i in s:
    counter = counter + 1
    sl = i.split()
    f1.write("%s %0.2f" % (sl[0], float(sl[1]) + float(sl[2])))
    if counter != len(s):
        f1.write("\n")
f1.close()




    

counter = 0
#output second file
for i in s:
    counter = counter + 1
    sl = i.split()
    f2.write("%s %d" % (sl[0], int(sl[3]) + int(sl[4])))
    if counter != len(s):
        f2.write("\n")
f2.close()

       
#output third file 
p3 = open("values.txt", 'r')

f3 = open("output3.txt", 'w')
t = p3.readlines()
p3.close()
f3.write("{0:<9s} | {1:10s} | {2:10s} | {3:10s} \n".format('Name', 'Measure 1', 'Measure 2', 'Measure 3'))
f3.write("-----------------------------------------------\n")
for i in t:
    spl = i.split()
    f3.write("{:<9s} | {:>+10d} | {:>10.3f} | {:>9.7g} \n".format(spl[0], int(spl[1]), float(spl[2]), float(spl[3])))
    
f3.close()
    



    
