import pandas as pd
import numpy as np
section=['A','B','C','D',]
contri=[6700,5600,5000,5200]
s11=pd.Series(data=contri,index=section)
section1=['A','B','C','D','E']
contri1=np.array([6700,5600,5000,5200,np.NaN])
s12=pd.Series(data=contri1*2,index=section1,dtype=np.float32)
print("Attribute name \t\t Object s11 \t Object s12")
print("_______    \t\t_____\t____")
print("Data type(.dtype)    :\t",s11.dtype,'\t\t',s12.dtype)
print("Shape(.shape)    :\t",s11.shape,'\t\t',s12.shape)
print("No of Bytes(.nbytes)    :\t",s11.nbytes,'\t\t',s12.nbytes)
print("No of Dimensions(.ndim)    :\t",s11.ndim,'\t\t',s12.ndim)
print("Item size(.itemsize)    :\t",s11.itemsize,'\t\t',s12.itemsize)
print("Has NaNs(.hasnans)    :\t",s11.hanans,'\t\t',s12.hasnans)
print("Empty?(.empty)    :\t",s11.empty,'\t\t',s12.empty)