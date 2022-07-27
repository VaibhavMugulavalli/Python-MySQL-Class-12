import matplotlib.pyplot as plt
import numpy as np
ar2=[1,7,21,35,35,21,7,1]
s2=np.sin(ar2)
c2=np.cos(ar2)
t2=np.tan(ar2)
plt.figure(figsize=(15,7))
plt.plot(ar2,s2,'c')
plt.plot(ar2,c2,'r')
plt.plot(ar2,t2,'k')
plt.xlabel("Array Value")
plt.ylabel("Sine,Cosine and Tangent values")
plt.show