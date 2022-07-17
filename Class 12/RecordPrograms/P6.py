from typing import Final
import pandas as pd
dict={'Ram':150,'Rahul':145,'Rohit':122,'Raghav':130,'Ramith':160,'Romith':125,'Rakul':130,'Roman':90,'Raygan':95,'Rakshit':160,'Roshan':85,'Raj':160,'Ruthu':130,'Rancho':160,'Rafthar':100,'Rajath':150,'Rakshita':130,'Romeo':110,'Ramesh':160,'Suresh':160}
sales=pd.Series(dict)
print("Before Update:",sales)
updatedindex=[160,155,132,140,170,135,140,100,105,170,95,170,140,170,110,160,140,120,170,170]
sales.index=updatedindex
Final=sales.reset_index()
print(Final)
