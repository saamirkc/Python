import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/cr7karkii/Downloads/batsman_season_record.csv')
plt.bar(df['batsman'],df['2015'],label=2015)
plt.bar(df['batsman'],df['2016'],bottom=df['2015'],label=2016)
plt.bar(df['batsman'],df['2017'],bottom=df['2015']+df['2016'],label=2017)
plt.legend()
plt.show()