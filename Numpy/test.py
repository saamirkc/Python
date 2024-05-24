prices=[]
n=100
# for i in range(n):
#     prices.append(100+i/100)
# print(prices[:5])
import numpy as np
prices=100+np.arange(n)/100
print(prices[:5])