import numpy as np
import pandas as pd
x=np.array([1,3,5,6,7,2])
print(pd.Series(x))
print(pd.Series(np.linspace(start=1,stop=2,num=10)))