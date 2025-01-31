# ДЗ 15.1. Клас «Прямокутник

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return NotImplemented
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             total_area = self.get_square() + other.get_square()
#             new_width = int(total_area ** 0.5)
#             while total_area % new_width != 0:
#                 new_width -= 1
#             new_height = total_area // new_width
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)) and n > 0:
#             new_area = self.get_square() * n
#             new_width = int(new_area ** 0.5)
#             while new_area % new_width != 0:
#                 new_width -= 1
#             new_height = new_area // new_width
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height})"
#
# # Test cases
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'


#ДЗ 15.2. Клас «Правильний дріб»

from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        result = Fraction(self.a * other.a, self.b * other.b)
        result.simplify()
        return result

    def __add__(self, other):
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'  # Исправлено на 7/6
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'  # Упрощение 6/18 -> 1/3
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'  # Упрощение 3/18 -> 1/6

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')

