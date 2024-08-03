a=int(input())
choice="yes"
sum=4
while(choice=="yes"):
    sum+=a
    if(sum%4==0):
        print("number is divisible by 4")
        choice=input("do you want to continue")
    else:
        print("number is not divided by 4")
        break
    a=int(input("enter new number"))
    