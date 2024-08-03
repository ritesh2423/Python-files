def cost(type,quantity,distance):
    if(type=="N" and quantity>0 and distance>0):
        tprice=quantity*150
        if(distance<=3):
            return tprice
        elif(distance>3 and distance<=6):
            return tprice+(distance*3)
        else:
            return tprice+9+(distance-3)*6
    elif(type=="V" and quantity>0 and distance>0):
        tprice=120*quantity
        if(distance<=3):
            return tprice
        elif(distance>3 and distance<=6):
            return tprice+(distance*3)
        else:
            return tprice+9+(distance-3)*6
    else:
        return -1
    

bill=cost("N",4,12)
print(bill)