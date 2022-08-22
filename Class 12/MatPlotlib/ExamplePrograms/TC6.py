from turtle import color
import matplotlib.pyplot as plt
x=['RCB','CSK','MI','DC']
RCB=[200,170,158,140]
CSK=[180,166,178,200]
MI=[200,203,150,145]
SRH=[140,158,122,176]
plt.bar(RCB,x,color='r')
plt.bar(CSK,x,color='y')
plt.bar(MI,x,color='b')
plt.bar(SRH,x,color='orange')
plt.show()