import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/cr7karkii/Downloads/batter.csv')
# print (df)
df=df.head(50)
print (df)

plt.scatter(df['avg'],df['strike_rate'])
plt.title('Top 50 Batsman')
plt.xlabel('Average')
plt.ylabel('Strike_rate')
plt.show()
