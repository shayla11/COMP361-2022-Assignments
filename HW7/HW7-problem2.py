#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:59:01 2022

@author: shayla
"""

import matplotlib.pyplot as plt
import numpy as np

line = np.random.normal(2, .5, 1000)
plt.hist(line, 50, histtype='step')
plt.title("Average distances walked per day, Greensboro Residents")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.savefig("hist problem 2")
