from locale import currency
import pandas as pd
Country={'Country':['India','USA','Russia','China','UK','France','Pakistan','Germany','Italy','Malaysia'],'National Animals':['Bengal Tiger','Bald Eagle','Brown Bear','Giant Panda','Unicorn','Rooster','Markhor','Eagle','Wolf','Malayan Tiger'],'National Bird':['Peakock','Bald Eagle','Double Headed Eagle','Red Crowned Crane','Robin','Rooster','Chukar','Eagle','Sparrow','Hornbill'],'Currency':['Ruppee','Dollar','Rouble','Yuan','Sterling Pound','Euro','Pakistani Ruppee','Euro','Euro','Ringgit']}
df=pd.DataFrame(Country)
print(df)
print("Acessing row using .loc:",'\n',df.loc[0:9])
print("Acessing column using .iloc:",'\n',df.iloc[:,0:4])