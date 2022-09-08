import pandas as pd
import matplotlib.pyplot as pl
df1=pd.DataFrame({'Australia':{"gold":67,"silver":57,"bronze":54,"total":178},"England":{"gold":57,"silver":66,"bronze":53,"total":176},"Canada":{"gold":26,"silver":32,"bronze":34,"total":92},"India":{"gold":22,"silver":16,"bronze":23,"total":61}})
print(df1)
while True:
    print("enter 1 for horizontal bar chart","enter 2 for vertical bar chart ","enter 3 for multipel bar chart ","enter 0 to exit")
    ch=eval(input("enter choice "))
    if ch==0:
        print("End of Program")
        break
    elif ch==1:
        print("vertical bar chart for medal tally of Australia")
        df1["Australia"].plot(kind="bar",color=["gold","silver","brown","k"])
        pl.xlabel("Medal type")
        pl.ylabel("Number of Medals")
        pl.title("Medal tally of Australia")
        pl.show()
    elif ch==2:
        print("Horizontal bar chart for medal tally of India")
        df1["India"].plot(kind="barh",color=["gold","silver","brown","k"])
        pl.xlabel("Medal type")
        pl.ylabel("Number of Medals")
        pl.title("Medal tally of India")
        pl.show()
    elif ch==3:
        print("Multiple bar chart of top 4 countries in CWG")
        df1.plot(kind="bar",color=["green","blue","red","orange"])
        pl.xlabel("Medal type")
        pl.ylabel("Number of Medals")
        pl.title("Medal tally of CWG")
        pl.show()
