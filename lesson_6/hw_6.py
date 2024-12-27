# # HW 6.1. Діапазон букв
# input_string = input("Введіть рядок у форматі 'a-c': ")
#
# all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# start, end = input_string.split('-')
#
# start_index = all_letters.index(start)
# end_index = all_letters.index(end) + 1
#
# result = ""
# for i in range(start_index, end_index):
#     result += all_letters[i]

# print(result)
# HW 6.2. Конвертер із числа в дату
# while True:
#     try:
#         seconds = int(input("Введіть кількість секунд (від 1 до 8640000) або введіть 0 і програма завершиться: "))
#
#         # Вихід з циклу, якщо введено число 0
#         if seconds == 0:
#             print("Програма завершена.")
#             break
#
#         if not (1 <= seconds < 8640000):
#             print("Число має бути в діапазоні від 1 до 8640000.")
#         else:
#             days, seconds = divmod(seconds, 24 * 60 * 60)
#             hours, seconds = divmod(seconds, 60 * 60)
#             minutes, seconds = divmod(seconds, 60)
#
#             if days % 10 == 1 and days % 100 != 11:
#                 day_word = "день"
#             elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
#                 day_word = "дні"
#             else:
#                 day_word = "днів"
#
#             formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:
#             {str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
#             print(formatted_time)
#
#     except ValueError:
#         print("Будь ласка, введіть ціле число.")

#HW 6.3. Добуток чисел
while True:
    try:
        number = int(input("Введіть ціле число: "))

        if number < 0:
            print("Будь ласка, введіть додатне число.")
            continue

        while number > 9:
            result = 1
            for dig in str(number):
                result *= int(dig)
            number = result

        print(f"Результат: {number}")

    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

