import math
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))



delta=(num2*num2) - (4*num1*num3)


root1=((-num2 + math.sqrt(delta))/(2*num1))
root2=((-num2 - math.sqrt(delta))/(2*num1))

print(f"first square root is: {root1}")
print(f"second square root is: {root2}")
