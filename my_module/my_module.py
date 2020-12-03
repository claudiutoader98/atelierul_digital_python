def my_sum(n):
    if n <= 1:
        return n
    return n + my_sum(n - 1)


def my_even_sum(n):
    if n <= 2:
        return n
    if n % 2 == 1:
        return my_even_sum(n - 1)
    return n + my_even_sum(n - 2)


def my_odd_sum(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return my_odd_sum(n - 1)
    return n + my_odd_sum(n - 2)
