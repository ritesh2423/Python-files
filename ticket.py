def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    cost_of_adult=no_of_adults*37550.0
    cost_of_children=no_of_children*(37550.0/3)
    total_cost=cost_of_adult+cost_of_children
    total_after_tax_charges=total_cost*(7/100)+total_cost
    discount=total_after_tax_charges-total_after_tax_charges*(10/100)
    total_ticket_cost=discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,0)
print("Total Ticket Cost:",total_ticket_cost)





a = -10
b = -200
c = 2000
d = 4000
if( a*b >=d):
    if(d>c):
        if(d%c!=0):
            print(11)
        else:
            print(22)
else:
    if(b/a >0):
        if(a<b or d%c!=0):
          print(33)
        else:
          print(44)