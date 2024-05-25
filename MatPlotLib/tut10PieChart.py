import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=[34,89,50,49,33,56]
subject=['english','maths','applied','ect','edc','dl']
plt.pie(data,labels=subject)
plt.show()