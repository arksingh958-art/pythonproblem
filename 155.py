# remove duolicate using set
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
my_set = set(my_list)
my_list_without_duplicates = list(my_set)
print(my_list_without_duplicates)