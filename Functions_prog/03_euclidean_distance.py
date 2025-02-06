import math
def eucilidean():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    num3=int(input("Enter the third number: "))
    num4=int(input("Enter the fourth number: "))

    euclidean_distance=math.sqrt(((num1-num2)**2)+((num3-num4)**2))
    print(euclidean_distance)
eucilidean()