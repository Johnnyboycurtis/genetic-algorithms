#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:26:08 2018

@author: jn107154
"""

import matplotlib.pyplot as plt
import numpy as np

F = lambda x: np.sin(2*x)

plt.ion()       # something about plotting
x = np.linspace(0, 1, 200)
plt.plot(x, F(x))


for i in range(100):
    if 'ax' in globals(): ax.remove()
    newx = np.random.choice(x, size = 10)
    ax = plt.scatter(newx, F(newx))
    plt.pause(0.05)

plt.ioff()
plt.show()

