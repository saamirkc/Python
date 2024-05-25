import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

children=[10,20,30,40,50]
color=['red','blue','green','orange','black']
plt.bar(color,children)      #vertical bar
# plt.barh(color,children,color='red')    #horizontal bar
plt.show()