import random

num =int(input("Enter how many dintict number you want: "))
list=[]



while len(list)<num:
    value=random.randint(1,100)
    if value not in list:
        list.append(value)
    

print(list)