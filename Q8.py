import pandas as pd
PriceData=[23000,34500,56000,45000]
Item=['TV','FRIDGE','OVEN','LAPTOP']
s=pd.Series(PriceData,index=Item)
print(s)