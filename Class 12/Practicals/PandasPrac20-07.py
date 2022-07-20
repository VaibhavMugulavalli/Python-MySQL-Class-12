import pandas as pd
#Q1
temp2=pd.Series([38,32,35,31,36,33,34],index=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
print(temp2)
#Q2
s=pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
lst=['F','G','H','I','J']
print(s)
s.index=(lst)
print(s)
#Q3
s1=pd.Series([6700,5600,5000,5200],index=[1,2,3,4])
print("Original output:",s1)
s1=pd.Series([6700,5600,8000,5200],index=[1,5,3,4])
print("Change output:",s1)
#Q4
items=pd.DataFrame({'ItemID':['PC01','LC05','PC03','PC06','LC03'],'ItemName':['Personal Computer','Laptop','Personal Computer','Personal Computer','Laptop'],'Manufacturer':['ABC','ABC','XYZ','COMP','PQR'],'Price':[35000,35000,32000,37000,57000]})
print(items)
#Q5
#a
items.index=['PC1','LC5','PC3','PC6','LC3']
#b
items.loc[len(items.index)] = ['LC09','Laptop','ABC',33000] 
print(items)
#c
items.columns=['ID','INAME','VENDOR','COST']
#d
items.drop(labels=['PC1'],axis=0,inplace=True)
print(items)
#e
items.drop(labels=['INAME'],axis=1,inplace=True)
print(items)
#f
print(items.loc['PC3'])
#g
print(items.loc['VENDOR','COST'])
#h
print(items.loc['PC3':'LC3'])
#i
print(items.head(2))
#j
print(items.tail(3))

#Q6
print("Index:",items.index)
print("Columns:",items.columns)
print("Axes:",items.axes)
print("DataTypes:",items.dtypes)
print("Size:",items.size)
print("Shape:",items.shape)
print("Values:",items.values)
print("Empty?:",items.empty)
print("No of Dimensions:",items.ndim)
print("Transpose:",items.T)