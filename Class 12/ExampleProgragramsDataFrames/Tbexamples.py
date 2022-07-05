import pandas as pd
#21
dict1={'Section':['A','B','C','D'],'Contri':[6700,5600,5000,5200]}
df1=pd.DataFrame(dict1)
print(df1)
#22
sales={'yr1':{'Otr1':34500,'Otr2':56000,'Qtr3':47000,'Qtr4':49000},'yr2':{'Otr1':44900,'Otr2':46100,'Qtr3':57000,'Qtr4':59000}}
dfsales=pd.DataFrame(sales)
print(dfsales)

#23
#indexlables=A,B,Q3,Q4,Qtr1,Qtr2,Qtr4
#column name df3=1,2

#24
zoneA={'Target':56000,'Sales':58000}
zoneB={'Target':70000,'Sales':68000}
zoneC={'Target':75000,'Sales':78000}
zoneD={'Target':60000,'Sales':71000}
sales=[zoneA,zoneB,zoneC,zoneD]
salesdf=pd.DataFrame(sales,index=['zoneA','zoneB','zoneC','zoneD'])
print(salesdf)

#25

list2=[[25,45,60],[34,67,89],[88,90,56]]
df2=pd.DataFrame(list2,index=['row1','row2','row3'])
print(df2)

#26

Target=[56000,70000,75000,60000]
Sales=[58000,68000,78000,61000]
ZoneSales=[Target,Sales]
zsalesdf=pd.DataFrame(ZoneSales,columns=['ZoneA','ZoneB','ZoneC','ZoneD'],index=['Target','Sales'])
print(zsalesdf)

#27
#   0 1
#0 11 12
#1 13 14
#2 15 16

#28
import numpy as np
arr1=np.array([[101,113,124],[130,140,200],[115,216,217]])
dtf3=pd.DataFrame(arr1)
print(dtf3)

#29
staff=pd.Series([20,36,44])
salaries=pd.Series([279000,396800,563000])
avg=salaries/staff
org={'people':staff,'Amount':salaries,'Average':avg}
dtf5=pd.DataFrame(org)
print(dtf5)
