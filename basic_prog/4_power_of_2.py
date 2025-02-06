number=int(input("Enter the Number: "))
if(number<=31):
    for i in range(1,number+1):
        print(2**i)
else:
    print("Overflow")

