import numpy as np
import pandas as pd

df1=pd.DataFrame({
    'city':['newyork','chicago','orlando','baltimore'],
    'temperature':[21,14,35,28]
})

df2=pd.DataFrame({
    'city':['newyork','chicago','sandiego'],
    'humidity':[65,68,71]
})

print(pd.merge(df1,df2,on='city',how='inner'))
print(pd.merge(df1,df2,on='city',how='left'))
print(pd.merge(df1,df2,on='city',how='right'))
print(pd.merge(df1,df2,on='city',how='outer'))