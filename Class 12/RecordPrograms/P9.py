import pandas as pd
a1 = [['Sana',26,'HR',80000,'Manager'],['Sana',26,'HR',80000,'Manager'],['Payal',32,'IT',200000,'Manager'],['Vidhya',26,'HR',67000,'Assistant'],['Manal',40,'IT',500000,'Team Leader']]
df1 = pd.DataFrame(a1,columns = ['Name','Age','Department','Monthly Salary','Profession'])
print(df1)
print(df1['Department'])
print(df1.loc[2])
df1.iat[3,1] = 34
print("Index:\n",df1.index)
print("Columns:\n",df1.columns)
print("Axes:\n",df1.axes)
print("DataTypes:\n",df1.dtypes)
print("Size:\n",df1.size)
print("Shape:\n",df1.shape)
print("Values:\n",df1.values)
print("Empty?:\n",df1.empty)
print("No.of Dimensions:\n",df1.ndim)
print("Transpose:\n",df1.T)
