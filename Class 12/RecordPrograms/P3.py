import pandas as pd
li=[]
ele=''
n=int(input("Enter number of areas you want in the series:"))

for i in range(n):
    ele=input("Enter Area:")
    li.append(ele)

s3=pd.Series(li)
s3.sort_values()
print("Smallest three areas",s3.tail)
print("Largest three areas",s3.head)