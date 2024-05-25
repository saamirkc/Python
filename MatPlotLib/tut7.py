import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
children=[10,15,20,15,25]
color=['red red red red red red ','green green green green','blue blue blue','orange orange orange','pink pink pink']
plt.bar(color,children)
plt.xticks(rotation='vertical')
plt.show()