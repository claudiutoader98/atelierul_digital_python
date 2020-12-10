class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __add__(self, other):
        denominator = lcm(self.denominator, other.denominator)
        return Fraction(self.numerator * (denominator / self.denominator) +
                        other.numerator * (denominator / other.denominator),
                        denominator)

    def __sub__(self, other):
        denominator = lcm(self.denominator, other.denominator)
        return Fraction(self.numerator * (denominator/self.denominator) -
                        other.numerator * (denominator/other.denominator),
                        denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)

    def __str__(self):
        return (f"""
    {self.numerator} 
   ---
    {self.denominator}""")


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f'f1 + f2 => {f1.__add__(f2)}')
print(f'f2 - f1 => {f2.__sub__(f1)}')
print(f'f1 inverse => {f1.inverse()}')

