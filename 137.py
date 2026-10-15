# find common num in list

numbrs1=[1, 2, 3, 4, 5, 6]
numbrs2=[4, 5, 6, 7, 8, 9]
common_numbers = [num for num in numbrs1 if num in numbrs2]
print(common_numbers)