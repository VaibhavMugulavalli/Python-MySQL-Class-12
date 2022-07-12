import pandas as pd 
import numpy as np
dict={'Ram':150,'Rahul':145,'Rohit':122,'Raghav':130,'Ramith':160,'Romith':125,'Rakul':130,'Roman':90,'Raygan':95,'Rakshit':160,'Roshan':85,'Raj':160,'Ruthu':130,'Rancho':160,'Rafthar':100,'Rajath':150,'Rakshita':130,'Romeo':110,'Ramesh':160,'Suresh':160}
sales=pd.Series(dict)
sales.sort_values()
print(sales)
print("Lowest sales:",sales.head(2))
print("Higest sales:",sales.tail(2))
