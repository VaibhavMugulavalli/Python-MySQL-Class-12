from matplotlib.lines import _LineStyle
import matplotlib.pyplot as plt
height=[121.9,124.5,129.5,134.6,139.7,147.3,152.4, 157.5,162.6]
weight=[19.7,21.3,23.5,25.9,28.5,32.1,35.7,39.6,43.2]
plt.plot(weight,height,'g',marker='*',markersize=10,linewidth=2)
plt.xlabel("Weight in Kg")
plt.ylabel("Height in cm")
plt.show()