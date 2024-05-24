import numpy as np
import pandas as pd
x= pd.Series([1,2,3,4,5])
y=pd.Series([50])
print(x+y)

z=pd.Series([20,30,35,40,45])
print(x+z)
a=pd.Series([20,30,35,40,45],index=(4,3,2,1,0))
print(x+a)