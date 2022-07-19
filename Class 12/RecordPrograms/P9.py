import pandas as pd
a1 = [['Sana',26,'HR',80000,'Manager'],['Sana',26,'HR',80000,'Manager'],['Payal',32,'IT',200000,'Manager'],['Vidhya',26,'HR',67000,'Assistant'],['Manal',40,'IT',500000,'Team Leader']]
df1 = pd.DataFrame(a1,columns = ['Name','Age','Department','Monthly Salary','Profession'])
print(df1)
print(df1['(i)Department'])
print('(ii)',df1.loc[2])
df1.iat[3,1] = 34
print("Index:",df1.index)
print("Columns:",df1.columns)
print("Axes:",df1.axes)
print("DataTypes:",df1.dtypes)
print("Size:",df1.size)
print("Shape:",df1.shape)
print("Values:",df1.values)
print("Empty?:",df1.empty)
print("No.of Dimensions:",df1.ndim)
print("Transpose:",df1.T)
