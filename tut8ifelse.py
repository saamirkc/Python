# is_Male=True
# if is_Male:
#     print("You are  male")
# else:
#     print("YOu are not male")


is_Male=True
is_Tall=True
if is_Male and is_Tall:
    print("You are tall male")
elif is_Male and not(is_Tall):
    print("You are short male")
elif not(is_Male) and is_Tall:
    print("You are not male but you are tall")
else:
    print("You are neither male nor tall")