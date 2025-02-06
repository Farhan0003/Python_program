def array2d():
    rows=int(input("Enter the rows: "))
    col=int(input("Enter the column: "))
    res=[]
    for i in range(rows):
        list=[]
        for j in range(col):
            number=int(input("Enter the number: "))
            list.append(number)
        res.append(list)
    print(res)
array2d()