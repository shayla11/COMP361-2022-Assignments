#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:45:51 2022

@author: shayla
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(.4,50,50)

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

ax1.plot(np.log(x))
ax1.set_title('log(x)')
ax1.grid()
ax1.plot(0)
ax1.axhline(y=0)

ax2.plot(1-(np.log(x)))
ax2.set_title('1-log(x)')
ax2.grid()
ax2.plot(0)
ax2.axhline(y=0)

plt.xlim(0, 10)





