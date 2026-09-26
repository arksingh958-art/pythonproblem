# electricity bill calculate karo

units= int(input(" enter a elctricity units:"))

if units<=100:
    bill= units*5
elif units<=200:
    bill= (100 * 5) +((units -100)* 7)
else:
    bill=(100*5) + (100 * 7)+((units-200)*10)
    print("electricity bill=" , bill)