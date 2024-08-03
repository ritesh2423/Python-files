def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if(((num1+num2)>=num3) and ((num2+num3)>=num1) and ((num3+num1)>=num2)):
        return success
    else:
        return failure
    

print(form_triangle(4,5,6))