import copy

print('Memory savers!!')

my_lambda = lambda x, y: x + y

my_sum = my_lambda(2, 3)

print(my_sum)

print(id(my_lambda))
print(id(lambda: 1))
print(id(my_lambda))
print(id(lambda: 3))

players = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'rank': 3
    },
{
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1
    },
{
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 2
    },
]

print(players)
sorted_players = sorted(players, key=lambda player: player['rank'], reverse=True)
print(sorted_players)


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_3'] = True if updated_player['rank'] <= 3 else False

    return updated_player


top_players = list(map(check_top_3_player, players))
print(top_players)


def filter_all_mcdonalds(player):
    if player['last_name'] == 'McDonald':
        return True
    return False


# all_mcdonalds = list(filter(filter_all_mcdonalds, players))
all_mcdonalds = list(filter(lambda player: player['last_name'] == 'McDonald', players))
print(all_mcdonalds)

letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]
for l, n in zip(letters, numbers):
    print(f'{l} - {n}')


my_numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for nr in my_numbers:
    squared_numbers.append(nr ** 2)
print(squared_numbers)

squared_numbers = [nr ** 2 for nr in my_numbers]
squared_even_numbers = [nr ** 2 for nr in my_numbers if nr % 2 == 0]

print(squared_numbers)
print(squared_even_numbers)
