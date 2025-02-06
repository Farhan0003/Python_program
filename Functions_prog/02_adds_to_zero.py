def add_to_zero():
    res=[]
    list=[]
    len=int(input("enter the length of list: "))
    for i in range(len):
        num=int(input("enter the number: "))
        res.append(num)
    # print(res)
    
    for i in range(len-2):
        for j in range(i+1,len-1):
            for k in range(j+1,len):
                if res[i]+res[j]+res[k]==0:
                    list.append([res[i],res[j],res[k]])
    print(list)
add_to_zero()

