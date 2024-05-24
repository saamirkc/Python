import numpy as np
import pandas as pd
df=pd.DataFrame({'name':['john','bob','mary'],'age':[20,21,23]})
print (df)

df1=pd.DataFrame([
    ['john',39],
    ['sam',22],
    ['vam',25]
],columns=['name','age'])
print (df1)