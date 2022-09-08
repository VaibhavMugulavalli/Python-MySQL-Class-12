import pandas as pd
import matplotlib.pyplot as pl
pd1=pd.DataFrame({"week1":[5000,5900,6500,3500,4000],'week2':[4000,3000,5000,5500,3000],"week3":[4000,5800,5000,2500,3000]})
while True:
    print("enter 1 for solid line graph","enter 2 for solid line graph","enter 3 to exit")
    ch=int(input("enter choice"))
    if ch==1:
        pl.plot(pd1['week1'],color='red',label="week1")
        pl.plot(pd1['week2'],color='blue',label="week2")
        pl.plot(pd1['week3'],color='brown',label="week3")
        pl.legend()
        pl.xlabel("Days")
        pl.ylabel("Sales in Rs")
        pl.title("mela sales report")
        pl.show()
    elif ch==2:
        pl.plot(pd1['week1'],color='red',marker="*",markersize=10,linewidth=4,linestyle="dashed",label="week1")
        pl.plot(pd1['week2'],color='blue',marker="*",markersize=10,linewidth=4,linestyle="dashed",label="week2")
        pl.plot(pd1['week3'],color='brown',marker="*",markersize=10,linewidth=4,linestyle="dashed",label="week3")
        pl.legend()
        pl.xlabel("Days")
        pl.ylabel("Sales in Rs")
        pl.title("Mela sales report")
        pl.show()
    elif ch==3:
        break
