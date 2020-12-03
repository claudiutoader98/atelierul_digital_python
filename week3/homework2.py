from my_module.my_module import *

def my_function(*args, **kwargs):
    my_sum = 0
    for x in args:
        if type(x) == int or type(x) == float:
            my_sum += x

    return my_sum


def read_from_keyboard():
    value = input("Enter a value = ")
    try:
        number = int(value)
        return number
    except ValueError:
        return 0


if __name__ == '__main__':
    print(f"{my_function(1, 5, -3, 'abc', [12, 56, 'cad'])}")
    print(f"{my_function(2, 4, 'abc', param_1=2)}")
    print(f"Your input: {read_from_keyboard()}")
    print(f"Sum 0 -> n: {my_sum(5)}")
    print(f"Sum even 0 -> n: {my_even_sum(5)}")
    print(f"Sum odd 0 -> n: {my_odd_sum(5)}")
