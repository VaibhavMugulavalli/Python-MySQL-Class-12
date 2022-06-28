#Q5
import pandas as pd 
import numpy as np
#a
lst=[]
for i in range(65,91):
    lst.append(chr(i))
EngAlph=pd.Series(lst)
print(EngAlph)
#b
Vowels=pd.Series(0,index=['a','e','i','o','u'])
print(Vowels)
#c
dict1={1:"Rohit",2:"Rahul",3:"Ramesh",4:"Romit",5:"RadhaKrishnan"}
Friends=pd.Series(dict1)
print(Friends)
#d
MTseries=pd.Series()
print(MTseries)
#e
A1=np.array([31,29,31,30,31,30,31,31,30,31,30,31])
MonthDays=pd.Series(A1,index=[1,2,3,4,5,6,7,8,9,10,11,12])
print(MonthDays)

#Q6
#a
Vowels=pd.Series(10,index=['a','e','i','o','u'])
print(Vowels)
#b
print(Vowels/2)
#c
Vowels1=pd.Series([2,5,6,3,8],index=['a','e','i','o','u'])
print(Vowels1)
#d
Vowels3=Vowels+Vowels1
print(Vowels3)
#e
print("Multiplication:",Vowels*Vowels1)
print("Division:",Vowels/Vowels1)
print("Diffrence:",Vowels-Vowels1)
#f
Vowels4=Vowels1.index=['A','E','I','O','U']
print(Vowels4)

#Q7
#a
print("EngAlph:",'\n',"Dimensions:",EngAlph.ndim,'\n',"Shape:",EngAlph.shape,'\n',"Values:",EngAlph)
print("Vowels:",'\n',"Dimensions:",Vowels.ndim,'\n',"Shape:",Vowels.shape,'\n',"Values:",Vowels)
print("Friends:",'\n',"Dimensions:",Friends.ndim,'\n',"Shape:",Friends.shape,'\n',"Values:",Friends)
print("MTseries:",'\n',"Dimensions:",MTseries.ndim,'\n',"Shape:",MTseries.shape,'\n',"Values:",MTseries)
print("MonthDays:",'\n',"Dimensions:",MonthDays.ndim,'\n',"Shape:",MonthDays.shape,'\n',"Values:",MonthDays)
#b
SeriesEmpty=pd.Series(MTseries)
print(SeriesEmpty)
#c

