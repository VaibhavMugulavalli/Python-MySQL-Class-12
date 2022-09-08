import pandas as pd
import matplotlib.pyplot as pl
li=[78,72,69,81,63,67,65,75,79,74,71,83,71,79,80,69]
while True:
    print(" 0.Exit\n 1. Create a simple Histogram from the above data\n 2. Create a Horizontal histogram from the above data\n 3. Create a step type of Histogram from the above data\n 4. Create a cumulative histogram from the above data.")
    ch=eval(input("enter choice"))
    if ch==0:
        print("end of program")
    elif ch==1:
        pl.hist(li,bins=10)
        pl.title("simple histogram")
        pl.show()
    elif ch==2:
        pl.hist(li,bins=10,orientation='horizontal')
        pl.title("Horizontal histogram")
        pl.show()
    elif ch==3:
        pl.hist(li,bins=10,histtype='step')
        pl.title("step histogram")
        pl.show()
    elif ch==4:
        pl.hist(li,bins=10,cumulative=True)
        pl.title("Cumulative histogram")
        pl.show()
