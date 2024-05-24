import numpy as np
import pandas as pd
# ages = pd.Series(
#     data = [42, 43, 14, 18, 1],
#     index = ['peter', 'lois', 'chris', 'meg', 'stewie']
# )
ages = pd.Series( [42, 43, 14, 18, 1],index = ['peter', 'lois', 'chris', 'meg', 'stewie'])
print (ages)
genders = pd.Series(
    data = ['female', 'female', 'male', 'male', 'male'],
    index = ['lois', 'meg', 'chris', 'peter', 'stewie'],
    dtype = 'string'
)
print(genders)

mask=(ages>18)&(genders=='male')
print (mask)
print(mask.loc[mask])
