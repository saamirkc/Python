import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/cr7karkii/Downloads/gayle-175.csv')
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%')
plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=[0.1,0,0,0,0,0],shadow=True)
plt.show()