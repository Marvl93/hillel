# #Homework 3.1
#
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# user_select = int(input("1. + \n2. -\n3. /\n4. *\nSelect your choice: "))
#
# match user_select:
#     case 1:
#         print(number1+number2)
#     case 2:
#         print(number1-number2)
#     case 3:
#         print(number1/number2) if number2 != 0 else print("Error")
#     case 4:
#         print(number1*number2)
#     case _:
#         print("Invalid input please try again")

# #Homework 3.2
# numbers = [77, 9, 15, 22, 33, 45, 200]
# numbers.insert(0, numbers[-1])
# numbers.pop()  # удаляет последнее число в списке
# print(numbers)
# numbers.sort()  # cортирует от меньшего к большему (это я для себя, в не домашки)
# print(numbers)

# Homework 3.3
num = [1, 2, 3, 4, 5, 6]
part1 = num[:len(num)//2]
part2 = num[len(num)//2:]
print(num)
print(part1, part2)
result = [part1, part2]
print(num,'==>', result)

num2 = [1, 2, 3, 4, 5]
part1_1 = num2[:len(num2)//2]
part2_1 = num2[len(num2)//2:]
print(part1_1, part2_1)
result2 = [part1_1, part2_1]
print(num2, '==>', result2)

num3 = [1,2,3]
part1_2 = num3[len(num3)//4:]
part2_2 = num3[:len(num3)//1]
print(part1_2, part2_2)
result3 = [part1_2, part2_2]
print(num3, '==>', result3)
