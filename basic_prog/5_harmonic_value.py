n=int(input("Till what number you want the harmonic value: "))
count=0
for i in range(1,n+1):
    count +=(1/i)

print(count)