import numpy as np
import pandas as pd
x=np.array([5,10,15,20,25])
y=pd.Series(x)
print(y)
y.index=[1,2,0,3,4]
print(y)

# y=pd.Series([5,10,15,20,25])
# print(y)
# y.index=[1,2,0,3,4]
# print(y)
print(y[0])
print(y.iloc[0])
print(y.loc[0])