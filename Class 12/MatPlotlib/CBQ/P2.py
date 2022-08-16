import matplotlib.pyplot as plt
days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
ThumbsUp=[330,300,450,150,400,650,425]
Maaza=[515,400,500,350,300,500,375]
Bindu=[450,560,610,505,490,500,415]
plt.plot(days,ThumbsUp,color='b')
plt.plot(days,Maaza,color='r')
plt.plot(days,Bindu,color='g')
plt.show()