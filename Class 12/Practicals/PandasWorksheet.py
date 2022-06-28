import pandas as pd
import numpy as np
#1
Y2021=[2345,3450,5490,3400,2300]
Y2022=[4500,5600,4300,4500,5600]
#2
s21=pd.Series(Y2021,index=["JAN","MAR","MAY","JUL","SEP"])
s22=pd.Series(Y2022,index=["JAN","MAR","MAY","JUL","SEP"])
#3
print(s21)
print(s22)
#4
print("No of elements:",len(s21))
#5
print("ByteSize:",s22.nbytes)
#6
print("Size:",s21.size,'\n',s22.size)
#7
scom21 = s21[:]*0.15
print(scom21)
#8
scom22 = s22[:]*0.20
print(scom22)
#9
print(s21["MAY":"SEP"])
#10
print(s22[1:4])
#11
megasale=pd.Series((s21["MAR":"JUL"]))
print(megasale)
#12
print(f"sum:{sum(megasale)}\nmean:{sum(megasale)/len(megasale)}")
#13
print(max(Y2021))
#14
print(min(Y2022))
#15
s21.index = [1,3,5,7,9]
print(s21)
#16
odd = pd.Series(np.arange(51,150,2))
print(odd)
#17
Even = pd.Series(np.arange(10,101,10))
print(Even)
#18
data = pd.Series(69, index = [chr(x) for x in range(97,122)])
print(data)
#19
print(odd.head(10))
#20
print(odd.head(6))
#21
print(Even.tail(4))
#22
print(Even.head(4))
#23
print(s21[1:1])
print(s21[2])
print(s22[2:4])
print(s22[3].index)
print(s22.values)
s22[0:2]=7000
print(s22)
print(s21[['MAR','MAY']])
print(sobj1=s21+s22)
print(sobj1=s21-s22)
print(sobj1=s21*s22)
print(sobj1=s21/s22)
print(sobj1.add(sobj1))
print(sobj1.sub(sobj1))
print(sobj1.mul(sobj1))
print(sobj1.div(sobj1))
print(sobj1.index)
print(sobj1.dtype)




