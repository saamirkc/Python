try:
    value=10/0
    number=int(input("Enter the number : "))
    print (number)

except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print ("Invalid input")
