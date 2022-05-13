#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:04:11 2022

@author: shayla
"""
import numpy as np

#A = np.arange(16).reshape(4,4)

#A[A%2==0] = -1

#A = np.arange(9).reshape(3,3)
#v = np.array([2, 4, 6])
#A+v

"""
from pandas import DataFrame

data = np.array([[70, 72, 68], [190, 180, 202]])

df = DataFrame(data, index=['Height', 'Weight'],columns=['Al', 'Ed', 'Jo'])

print(df)
df['mean'] = df.mean(axis=1)

df['std'] = df.std(axis=1)
print(df)
"""

class Car(object):
    def __init__(self, gas, mpg):
        self.gas = gas
        self.mpg = mpg
    def __str__(self):
        return "A car with {0:d} mpg".format(self.mpg)
    def travel(self, miles):
        if (self.gas * self.mpg)-miles < 0:
            raise Exception("Not enough gas")
        self.gas -= (miles/self.mpg)


if __name__ == '__main__':
    car1 = Car(15, 17)
    print(car1)
    car1.travel(150)
    print(f'Gas remaining: {car1.gas:.2f} gallons')
    try:
        car1.travel(120)
    except Exception as detail:
        print(detail)


