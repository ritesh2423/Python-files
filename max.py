def find_max(num1, num2):
    max_num=-1
    list=[]
    for i in range(num1,num2):
        a=str(i)
        sum=0
        for j in a:
            sum=+int(j)
        if(sum%3==0):
            list.append(i)
        if(len(a)==2):
            list.append(i)
        if(i%5==0):
            list.append(i)
    if(len(list)==0):
        max_num
    else:
        list.sort(reverse=True)
        print(list)
        return list[0]

max_num=find_max(-20,-15)
print(max_num)