import pandas as pd
Grades={'StudentNames':['Sharad','Mansi','Kanika','Ramesh','AnkitA','Pranay'],'UT1':[57,86,92,52,93,98],'HalfYearly':[83,67,78,84,75,79],'UT2':[49,87,45,55,87,88],'Annual':[89,90,66,78,69,96]}
df1=pd.DataFrame(Grades,index=[1,2,3,4,5,6])
print(df1)
df1.rename({'Ut1':'Term1','HalfYearly':'Term2','Ut2':'Term3','Annual':'Term4'},axis='column')
print(df1)
