number=int(input("Enter the number: "))
list=[]
count=0
for i in range(1,number+1):
    if(number%i==0):
        list.append(i)
print(list)
for i in list:
    
    count=0
    for j in range(1,i+1):
        if(i==1):
            pass
        else:
            if(i%j==0):
                count=count+1
    if(count==2):
        print(f"{i} is prime factor")

        