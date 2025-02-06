year=int(input("Enter the Year: "))
year1=str(year)
if(len(year1)>=4):
    if(year%4==0 or year%100==0 and year%400==0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} has less than 4 digits")