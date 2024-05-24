import numpy as np
arr=np.array([2,3,4,5,6,8,9,10,12,14])
print(arr[2::3])   # The slicing syntax arr[start:stop:step] allows you to extract
                  #elements from a NumPy array starting at index start, stopping
                  #before index stop, and taking steps of size step between elements.
                #   but here  2 indicates start index and :: indicates stop is ommitted
                # and 3 indicates the steps