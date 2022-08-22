import matplotlib.pyplot as plt
import numpy as np
mu=100
sigma=15
x=mu+sigma*np.random.randn(10000)
y=mu+30*np.random.randn(10000)
plt.hist([x,y],bins=100,histtype='barstacked')
plt.title("Reasearch data")
plt.show()