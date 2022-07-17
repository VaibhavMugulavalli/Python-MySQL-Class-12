import pandas as pd
dict={'Name':['Anil Kubmle','Shane Warne','Sachin Tendulkar','MS Dhoni','Lasith Malinga'],'No of matches played':[271,194,664,341,220],'Average Score':[50,33,120,122,25]}
df=pd.DataFrame(dict,index=[True,False,True,False,True])
print(df)
print(df.loc[True])
print(df.loc[False])