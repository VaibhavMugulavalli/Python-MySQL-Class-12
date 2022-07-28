import matplotlib.pyplot as plt
import numpy as np
A=np.arange(1,20,1.25)
B=np.log(A)
C=np.log10(A)
plt.plot(A,B,'ro')
plt.plot(A,C,'b^')
plt.show()