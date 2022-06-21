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