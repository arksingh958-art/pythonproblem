# salary tax calcculations

salry = float (input(" enter a anual salry"))

if  salry <=  30000:
    tax = 0
elif salry <= 70000:
    tax = 0.5 
elif salry <= 100000:
    tax = ( 30000 * 0.05) + ( salry - 70000)*0.20
else: (30000 * 0.05) + (70000 * 0.20) + ( salry- 100000)*0.30
print("tax=", tax)
print(" anual after tax=" , salry - tax)