import pandas as pd
Grades={'StudentNames':['Sharad','Mansi','Kanika','Ramesh','AnkitA','Pranay'],'UT1':[57,86,92,52,93,98],'HalfYearly':[83,67,78,84,75,79],'UT2':[49,87,45,55,87,88],'Annual':[89,90,66,78,69,96]}
df=pd.DataFrame(Grades,index=[1,2,3,4,5,6])
print(df)
print("1.Rowwise()",'\n',"2.Row wise series object(iterrows())",'\n',"3.Column wise()")
x=int(input("Enter option:"))
if x==1:
    print(df.loc[0:6])
elif x==2:
    for x,y in df.iterrows():
        print(x)
        print(y)
elif x==3:
    print(df.iloc[:,0:5])
else:
    print("Error 404")