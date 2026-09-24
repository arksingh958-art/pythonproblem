# profit loss calculate karo

cp = float(input("enter  cost price"))
sp = float (input(" enter a selling price"))

if sp>cp:
    profit= sp - cp
    print("profit:" , profit)
elif cp > sp:
    loss = cp - sp
    print("loss:", loss)
else:
    print(" no profit, no lose")