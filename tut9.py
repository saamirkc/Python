def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
    
print (max_num(2,32,7))




# from math import *
# num1=input("enter first no.")
# num2=input("enter second no.")
# num3=input("enter third no.")
# result=max(num3,max(num1,num2))
# print(result)
