import matplotlib.pyplot as plt
import numpy as np
nfib=[0,-1,-1,-2,-3,-5,-8,-13,-21,-31,0,1,1,2,3,5,8,13,21,34]
plt.plot(range(-10,10),nfib,'mo',markersize=5,markeredgecolor='k',linestyle='solid')
plt.grid(True)
plt.show()