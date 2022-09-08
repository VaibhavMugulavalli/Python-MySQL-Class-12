import pandas as pd
import numpy as np
#1
df=pd.read_csv("P19_csv.csv")
print("Dataframe from CSV\n",df)
#2
print("First 2 entries\n",df.head(2))
#3
print("Last 2 entries\n",df.tail(2))
#4
df1=pd.read_csv("P19_csv.csv",header=None)
print("Data without header\n",df1)
#5
df=pd.read_csv("P19_csv.csv",names=["Sname","Standard","English","IP","Math"],skiprows=1)
print("Change of column Names\n",df2)
#6
df.replace(90, np.nan)
print("Replace 90 with NaN \n",df)
print("final data frame\n",df)
#P20 
df.loc[len(df.index)] = ['Amy',5,67, 89, 93]
df.loc[len(df.index)] = ['Ved',5,78,85,89]
df.loc[len(df.index)] = ['Hary',5,67,81,88]
df["Total"]=df["English"]+df["IP"]+df["Math"]
df["avrage"]=df["Total"]/3
df.to_csv("studentreport.csv")
print(df)
