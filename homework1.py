my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

my_list_sorted = sorted(my_list)

print("my_list: ", my_list)
print("my_list_sorted", my_list_sorted)

my_list_descendent = my_list[:]
my_list_descendent.sort(reverse=True)

print("\nmy_list: ", my_list)
print("my_list_decendent: ", my_list_descendent)

print("\nmy_list even index: ", my_list[::2])
print("my_list odd index: ", my_list[1::2])

print("\nmultiple of 3: ", [x for x in my_list if x % 3 == 0])


