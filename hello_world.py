print("hello")

print("lol\" das")

s = """
    nice printing
    heheehe
"""

sentence = r"ceva\something\works...asdad"

print(s)
print(sentence)

s = "{0} are {1} mere".format("Ana", 32)

print(s)

print(F'For only {49:.2f} you will get {s}')

l = [1, 2, 3, "Ana", [1, 2, 3]]

print(l)


my_list = [0, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9]
print(my_list[2:])
print(my_list[-2:])

my_second_list = [12, 13]
# my_list.append(my_second_list)

my_list.extend(my_second_list)
print(my_list)

coord = (1, 2, 3)
print(coord[2])

d = dict()
b = {}

d[1] = '1'
print(d)
f = d
d[1] = '2'
print(f)

d = {
    1: 'Ana',
    2: 'are',
    3: 'Mere'
}

print(d.items())

for key, value in d.items():
    print("{} -> {}".format(key, value))


print(my_list)
my_set = set(my_list)
print(my_set)