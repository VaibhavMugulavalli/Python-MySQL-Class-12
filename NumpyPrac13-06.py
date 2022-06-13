#Q1
import numpy as np
a1=np.array([1,2,3,4,5,6,7,8,9])
print(a1)
#Q2
import numpy as np
a=np.zeros(5,dtype=int)
print(a)
#Q3
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18.19,20],dtype=int)
print(a[0:-1:2])
#Q4
import numpy as np
a=np.arange(0,12,dtype=int)
print("1D array is:",a)
print("2D array is:",a.reshape(4,3))
#Q5
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
#Q6
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a.dtype)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.ndim)
#Q7
import numpy as np
a=np.array([1,2,3,])
b=np.array([4,5,6])
c=np.concatenate((a,b),axis=0)
print(c)
#Q8
import numpy as np
a=np.arange(1,10,1)
print("With step diffrence of 1:",a)
b=np.arange(1,10,2)
print("With step diffrence of 2:",b)
#Q9
from re import A
import numpy as np
a=np.linspace(1,4,num=8)
print("Having 8 elements:",a)
b=np.linspace(1,4,num=4)
print("Having 4 elements:",b)
#Q10
import numpy as np
#(i)
a=np.zeros(10,dtype=int)
print("1D array is:",a)
print("2d array is:",a.reshape(2,5))
#(ii)
b=np.ones(6,dtype=int)
print("1D array is:",b)
print("2D array is:",b.reshape(2,3))
#(iii)
#Q11
import numpy as np 
a=np.array([1,2,3])
b=np.array([4,5,6])
print("Adittion:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
#Q12
import numpy as np
array1=np.arange(10,dtype=int)
print("Addition:",array1+array1)
print("Subtraction:",array1-array1)
print("Multiplication:",array1*array1)
print("Division:",array1/array1)

