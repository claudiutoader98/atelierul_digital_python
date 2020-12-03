class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f'animal: {self.name}: {self.age}'


class Cat(Animal):
    def speak(self):
        print('Meow meow')

    def __str__(self):
        return f'cat - {self.name}: {self.age}'


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def speak(self):
        print("Hello")

    def get_friends(self):
        return ', '.join(self.friends)

    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def get_age_diff(self, other):
        diff = self.age - other.age
        print(f'years difference {abs(diff)}')

    def __str__(self):
        return f'Person - {self.name}: {self.age}'

    def __sub__(self, other):
        return abs(self.age - other.age)


class Rabbit(Animal):
    # class variable
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __str__(self):
        return f'Rabbit: {self.rid}'

    def __eq__(self, other):
        same_parents = (self.parent1.get_rid() == other.parent1.get_rid()
                        and self.parent2.get_rid() == other.parent2.get_rid())

        opposite_parents = (self.parent1.get_rid() == other.parent2.get_rid()
                            and self.parent2.get_rid() == other.parent1.get_rid())

        return same_parents or opposite_parents


r1 = Rabbit(10)
r2 = Rabbit(20)

print(r1.get_rid())
print(r2.get_rid())

r3 = Rabbit(30)
r4 = Rabbit(40)

r5 = r1 + r2
r55 = r2 + r1

r6 = r3 + r4
r66 = r4 + r3

print(r5)
print(r6)

print(f'Parent 1 is {r5.get_parent1()}')
print(f'Parent 2 is {r5.get_parent2()}')

print(f'Parent 1 is {r6.get_parent1()}')
print(f'Parent 2 is {r6.get_parent2()}')

print(r5 == r55)

# dog = Animal(4)
# print(dog)
# dog.set_name('Azorel')
# dog.set_age(10)
# print(dog)
#
# tom = Cat(4)
# print(tom)
# tom.set_name('Tom')
# print(tom)
#
# ion = Person('Ion', 30)
# ana = Person('Ana', 21)
# vasile = Person('Vasile', 100)
#
# print(ion)
# print(ana)
#
# ana.add_friend('Ion')
# ana.add_friend('Vasile')
# ana.add_friend('Maria')
# ana.add_friend('Maria')
#
# print(ana.get_friends())
# ion.speak()
#
# ion.get_age_diff(ana)
#
# print(ion - ana)
# print(ion - vasile)
