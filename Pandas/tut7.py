import numpy as np
import pandas as pd
x=pd.Series([2,3,4,6,8],index=[12,14,5,15,18])
print (x)
y=x
y.iloc[0]=99
print(y)
print(x)
# here change in value of y also results in change in value in x as y=x


y=x.copy()
y.iloc[0]=199
print(y)
print(x)
# here y changes from value 99 to 199 but x remains same i.e 99