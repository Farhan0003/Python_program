import random
number=int(input("Enter how many times you want to flip the coin: "))
head_count=0
tail_count=0
for i in range(1,number+1):
    
    num=random.random()
    if(num>0.5):
        head_count +=1
    else:
        tail_count +=1
print(f"Head percentage is: {(head_count/number)*100}%")
print(f"Tail percentage is: {(tail_count/number)*100}%")