import random

current_money=int(input("Enter the current Money: "))
goal=int(input("Enter the goal Money: "))
win=0
loose= 0
loop=0

while current_money>0 and current_money<goal:
    loop +=1
    value=random.random()
    if current_money==goal and current_money==0:
        break
    else:
        if(value>=0.5):
            win += 1
            current_money+=1
        else:
            loose += 1
            current_money -= 1
    
    
win_percentage = (win/loop)*100 
loose_percentage= (loose/loop)*100 

print(f"how many times you played:{loop}")
print(f"your goal is {goal} and  your balance is {current_money}")
print(f"the number of win is: {win}")
print(f"win percentage is:{win_percentage}")
print(f"loose percentage is:{loose_percentage}")