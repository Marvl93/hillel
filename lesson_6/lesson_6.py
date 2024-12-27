# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.

# import string
# import keyword
#
# test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
#              'get_Value', '3m', 'm3', 'assert', 'assert_exception', 'some_super_puper__value']
#
# for test_variable in test_data:
#     if len(test_variable) > 0:
#         if test_variable in keyword.kwlist:
#             print(f"Error! Found {test_variable} is keyword!")
#         elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0:
#             is_correct = True
#             for symbol in string.punctuation.replace("_", ""):
#                 if symbol in test_variable:
#                     is_correct = False
#                     print(f"Error! Found {test_variable} in variable name!")
#                     break
#
#             first_underscore_index = test_variable.find("_")
#             if first_underscore_index != -1:
#                 second_underscore_index = test_variable.find("_", first_underscore_index + 1)
#                 if second_underscore_index != -1 and second_underscore_index - first_underscore_index == 1:
#                     is_correct = False
#                     print(f"Error! Found double '_' in {test_variable} variable name!")
#
#             if is_correct:
#                 print(f"Keyword {test_variable} is correct!")
#         else:
#             print(f"Error! Found {test_variable} in variable name!")
#     else:
#         print("Incorrect variable length!")

##############
# Кортеж (tuple) – константний (immutable) список
# можна працювати як зі звичайним списком,
# тільки не можна нічого міняти (функції, які змінюють колекцію - відсутні в кортежі)
# crud -> create, read, update, delete (у кортежі можна робити лише read)

# info = ("test1", 123)
# print(info)
# print(type(info))
#
# info = "test2", 1234, 123445
# print(info)
# print(type(info))
# #
# print(info[0])
#
# # info[0] = 123  # TypeError: 'tuple' object does not support item assignment
#
# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

####
# import copy
#
# info = "test2", 1234, 123445
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)
# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

###########
# for num in 1, 3, 4, 5, 6, "Hello", 7:
#     print(num)
#
# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)
#
# for _ in range(5):
#     print("Hello")
# #
# # # таку змінну створювати не можна так як оскільки її складно читати та зрозуміти
# _ = "Vasya"
# print(_)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

#####
# # v1
# numbers = []
#
# for number in range(10):
#     if number % 2 == 0:
#         numbers.append(number)
#
# # v2
# numbers = [number for number in range(10) if number % 2 == 0]
#
# print(numbers)

######
# dict -> словник, колекція key: value

# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     2: "qwerty",  # дублювати ключі не можна!
# }
#
# print(users)
# print(type(users))
# print(users[1])  # [1] -> це не індекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])
#
# users_list = [
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# ]
#
# users_dict = dict(users_list)
# print(users_dict)
#
# users_list = list(users_dict)
# print(users_list)

###########
##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# print(users["+33333333"])
# users["+33333333"] = "Petya"
# print(users["+33333333"])
#
# users["+4444444"] = "Test"
# print(users["+4444444"])
#
# print(users)
#
# for key in users:
#     print(users[key], end=" ")
#
# print()
# #
# for key in users.keys():
#     print(key, end=" ")
#
# print()
# print(users.keys())
# print(list(users.keys()))
# #
# for value in users.values():
#     print(value, end=" ")
#
# print()
# print(users.values())
#
# print()
# for key, value in users.items():
#     print(f"key: {key} value: {value}")
#
# print()
# print(users.items())

#####
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# # print(users["+33333333"])
# print(users.get("+333333331", "key not exists"))
#
# # del users["+55555555"]
# deleted_value = users.pop("+555555551", "key not exists")
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

##
# users_1 = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# #
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)
#
# users_2 = {
#     "+11111111": "eeeeeee",
#     "+44444": "qqqqqq",
#     "+12341234": "wwwwwww"
# }
# #
# users_1.update(users_2)
# print(users_1)
# print(users_2)

################
# json
# users = {
#     "Vasya": {
#         "phone": "123123",
#         "email": "qwerty1@gmail.com",
#         "hobbies": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "1345555",
#         "email": "aqwfafdbsdb@gmail.com",
#         "hobby": "uerhukjshbdjbkhdf",
#         "add_data": {
#             1: "test-1",
#             2: "test-2",
#         }
#     }
# }

# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])
# #
# print(users.get("Vasya").get("hobbies")[1])
# print(users.get("Petya").get("add_data").get(2))
##
# v1
# key = input("Enter key: ")
# if key in users:
#     print(users[key])
# else:
#     print("Nothing found!")

# v2
# key = input("Enter key: ").strip().lower()
# for curr_key in users.keys():
#     if curr_key.lower() == key:
#         print(users[curr_key])
#         break
# else:
#     print("Nothing found!")