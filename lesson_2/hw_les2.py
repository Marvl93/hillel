# Homework 2.1
number = int(input("Введіть 4-значне число: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10

print(n1)
print(n2)
print(n3)
print(n4)

print(f"{n1}-{n2}-{n3}-{n4}")
numbers_multiplication = (n1 * n2) ** n3 + n4
print(f"The multiplication of the numbers: {numbers_multiplication}")
print(divmod(n1, n4))
print(type(number))

# Homework 2.2
number = int(input("Введіть 5-значне число: "))

n1 = number // 10000
n2 = number % 10000 // 1000
n3 = number % 1000 // 100
n4 = number % 100 // 10
n5 = number % 10

print(f"А ти знав, що навпаки буде: \n{n5}\n{n4}\n{n3}\n{n2}\n{n1}")
result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print("Або:", result)