import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,7))
Info=['Gold','Silver','Bronze','Total']
Aus=[80,59,59,198]
Ind=[26,20,20,66]
Eng=[45,45,46,136]
Can=[15,40,27,82]
x=np.arange(len(Info))
plt.bar(Info,Aus,width=0.15)
plt.bar(x+0.15,Ind,width=0.15)
plt.bar(x+0.30,Eng,width=0.15)
plt.bar(x+0.45,Can,width=0.15)
plt.show()
