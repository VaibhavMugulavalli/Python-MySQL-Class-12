import pandas as pd
#a
cricket={'Name':['Anil Kubmle','Shane Warne','Sachin Tendulkar','MS Dhoni','Lasith Malinga'],'No of matches played':[271,194,664,341,220],'Average Score':[50,33,120,122,25]}
df1=pd.DataFrame(cricket)
print(df1)
#b
Items={'Product':['Rice','Wheat','Oil','Soap','Toothpaste'],'Cost Price':[55,120,200,50,40],'Sale Price':[60,125,220,55,45],'Discount':[2,5,'NA',2,'NA']}
df2=pd.DataFrame(Items)
print(df2)
#c
stud=pd.Series(['a','Shyam','Mohan','Rahul','Rohit','Ramesh','Ram'])
Result=pd.DataFrame({'Name':stud,'Percentage':[90,95,92,90,93,92]},index=[1,2,3,4,5,6])
print(Result)
#d
Places=pd.Series(['b','TajMahal','Summer Palce','Qutb Minar','Charminar','Red Fort','Gol Gumbaz'])
Monuments=pd.DataFrame({'Name':Places,'Year':[1632,1791,1981,1591,1638,1659],'Maker':['Shah Jahan','Tipu Sultan','Qutab-ud-din Aibak','Muḥammad Qulī Quṭb Shah','Shah Jahan','Adil Shahi']},index=[1,2,3,4,5,6])
print(Monuments)