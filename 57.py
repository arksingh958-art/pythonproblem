# character alphabet / digit / special character 
ch = input(" enter your character ")

if ch.isalpha():
    print("alphabet")
elif ch.isdigit():
    print("digit")
else:
    print("special character")
    