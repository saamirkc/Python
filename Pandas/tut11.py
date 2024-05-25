import numpy as np
import pandas as pd

df=pd.DataFrame ({
    'a':[2,3,4,5],
    'b':['fox','rabbit','hound','rabbit']
})
print (df)
df['c']=[2,3,4,5]
print (df)
df.loc[df.b=='rabbit' ,'f']=0
print (df)
