import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/cr7karkii/Downloads/batsman_season_record.csv')
print (df)
# plt.bar(df['batsman'],df['2015'])
# plt.bar(df['batsman'],df['2016'])

print(np.arange(df.shape[0]))  #df.shape indicate (rows,columns) in this case (5,4)
                     #df.shape[0] indicates number of rows which is 5 and df.shape[1]
                    # indicates number of columns which is 4
                    #np.arange gives value from 0 to end excludinf last number so
                    #np.arange(df.shape[0]) gives 0 to 4 as 5 is last no.

plt.bar(np.arange(df.shape[0])-0.2,df['2015'],width=0.2)
plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2)
plt.bar(np.arange(df.shape[0])+0.2,df['2017'],width=0.2)
plt.xticks(np.arange(df.shape[0]),df['batsman'])  #replacing 0 1 2 3 4 with respective batsman
plt.show()