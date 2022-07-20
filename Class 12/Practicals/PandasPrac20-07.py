import pandas as pd
#Q1
temp2=pd.Series([38,32,35,31,36,33,34],index=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
print(temp2)
#Q2
s=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
lst=['F','G','H','I','J']
s1.reset_index
print(s1)
#Q3
s1=pd.Series([6700,5600,5000,5200],index=[1,2,3,4])
print("Original output:",s1)
s1[5600]=[5800]
print("Change output:",s1)
#Q4
A1=[['PC01','Personal Computer','ABC',35000],['LC05','Laptop','ABC',35000],['PC03','Personal Computer','XYZ',32000],['PC06','Personal Computer','COMP','37000'],['LC03','Laptop','PQR',57000]]