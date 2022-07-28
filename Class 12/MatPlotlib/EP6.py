import matplotlib.pyplot as plt
import numpy as np
A=np.arange(1,20,1.25)
B=np.log(A)
plt.plot(A,B,'ro')
plt.xlabel("Random Values")
plt.ylabel("Logarithmic Values")
plt.show()