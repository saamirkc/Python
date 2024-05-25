import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
batsman=pd.read_csv('/home/cr7karkii/Downloads/sharma-kohli.csv')
print(batsman)
plt.plot(batsman['index'],batsman['V Kohli'],color='#3364FF',marker='D')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#33FFE3',linestyle='dashdot',marker='.')
plt.title('Virat Kohli VS Rohit Sharma Ipl Carrer Comparision')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.show()

