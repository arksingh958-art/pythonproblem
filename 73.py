# power  using loops 

base = int (input ( " enter  a base  "))

power = int ( input(" enter a power: "))

result = 1

for i in range (power):
    result= result * base
    print( " answer=" , result)

