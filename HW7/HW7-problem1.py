#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:53:59 2022

@author: shayla
"""

import matplotlib.pyplot as plt
import numpy as np


#Problem 1
def rectified_linear(x):
    return np.array([max(0,i) for i in x])


x = np.linspace(0, 2, 50)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x,np.sin(2*np.pi*x))
axs[0, 0].set_title(r'$sin(2\pi x)$')
axs[0, 0].axhline(linewidth=1, color="k") # black = k
axs[0, 0].grid()


axs[0, 1].plot(x, 0.4*np.sin(8*np.pi*x), 'tab:blue')
axs[0, 1].set_title(r'$0.4 sin(8\pi x)$')
axs[0, 1].axhline(linewidth=1, color="k") # black = k
axs[0, 1].grid()

axs[1, 0].plot(x, np.sin(2*np.pi*x) + 0.4*np.sin(8*np.pi*x), 'r')
axs[1, 0].set_title(r'$ sin(2\pi x)\ +\ 0.4 sin(8\pi x)$')
axs[1, 0].axhline(linewidth=1, color="k") # black = k
axs[1, 0].grid()

axs[1, 1].plot(x, np.sin(2*np.pi*x) + rectified_linear(0.4*np.sin(8*np.pi*x)), 'r')
axs[1, 1].set_title(r'$ sin(2\pi x)\ +\ ReL(0.4 sin(8\pi x))$')
axs[1, 1].axhline(linewidth=1, color="k") # black = k
axs[1, 1].grid()

fig.tight_layout()
plt.savefig('subplot problem 1')



