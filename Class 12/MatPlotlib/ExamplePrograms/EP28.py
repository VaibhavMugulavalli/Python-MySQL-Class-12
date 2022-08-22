import matplotlib.pyplot as plt
import numpy as np
mu=100
sigma=15
x=mu+sigma*np.random.randn(10000)
plt.hist(x,bins=30,orientation='horizontal')
plt.title("Reasearch data")
plt.show()