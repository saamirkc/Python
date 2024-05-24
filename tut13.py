# def pow(a,b):
#     result=1
#     while(b>0):
#         result=result*a
#         b-=1
#     return result
# print(pow(4,3))


def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(3,4))


