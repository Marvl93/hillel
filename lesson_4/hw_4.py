#HW 4.1
# lst = [0, 1, 0, 12, 3]
#
# non_zero_elements = [num for num in lst if num != 0]
# zero_count = lst.count(0)
# result = non_zero_elements + [0] * zero_count
#
# print(result)
#
# lst = [1, 0, 13, 0, 0, 0, 5]
# non_zero_elements = [num for num in lst if num != 0] #отбираем не нулевые значение в переменную
# zero_count = lst.count(0) #перебираем и записываем нули
# result = non_zero_elements + [0] * zero_count #к списку цифр без 0 мы прибавляем нули столько сколько их было в строке
# print(result)
#
# lst = [0]
# non_zero_elements = [num for num in lst if num != 0]
# zero_count = lst.count(0)
# result = non_zero_elements + [0] * zero_count
# print(result)
#
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# non_zero_elements = [num for num in lst if num != 0]
# zero_count = lst.count(0)
# result = non_zero_elements + [0] * zero_count
# print(result)


# HW 4.2. Знайти суму елементів із парними індексами
#
# lst = [0, 1, 7, 2, 4, 8]
#
# index_sum = sum(lst[i] for i in range(0, len(lst), 2))
#
# result = index_sum * lst[-1]
#
# print(result)

# ДЗ 4.3. Список із 3 елементів

import random

numbers = [random.randint(1, 100) for num in range(random.randint(3, 10))]
print("Исходный список:", numbers)

# Создаем новый список из 3 элементов: первого, третьего и второго с конца
new_list = [numbers[0], numbers[2], numbers[-2]]

print("Новый список:", new_list)
