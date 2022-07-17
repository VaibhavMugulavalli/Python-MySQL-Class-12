import pandas as pd
import numpy as np
population = {'2018':list(np.random.randint(100000,1000000,4)),'2019':list(np.random.randint(100000,1000000,4)),'2020':list(np.random.randint(100000,1000000,4)),'2021':list(np.random.randint(100000,1000000,4))}
df1 = pd.DataFrame(population,index = ['Mumbai','Delhi','Kolkata','Chennai'])
print(df1)
avg2018 = sum(df1['2018'])/4
avg2019 = sum(df1['2019'])/4
avg2020 = sum(df1['2020'])/4
avg2021 = sum(df1['2021'])/4
avg = pd.Series([avg2018,avg2019,avg2020,avg2021],index = [2018,2019,2020,2021])
print("Average Population Per Year:",avg)
print("First Two Rows:",df1.head(2))
print("Last Two Rows:",df1.tail(2))
