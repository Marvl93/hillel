# # #Homework 5.2. Модифікувати калькулятор
# while True:
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#
#     user_select = int(input("1. + \n2. -\n3. /\n4. *\nSelect your choice: "))
#
#     match user_select:
#         case 1:
#             print(number1+number2)
#         case 2:
#             print(number1-number2)
#         case 3:
#             print(number1/number2) if number2 != 0 else print("Error")
#         case 4:
#             print(number1*number2)
#         case _:
#             print("Invalid input please try again")
#
#     user_input = input("Enter 'n' to exit the program or any key to continue: ")
#     if user_input == "n":
#         print("Exit from program...")
#         break
#
# Homework 5.3. hashtag
# input_string = (input("Enter your words: "))
#
# clean_string = ""
# for char in input_string:
#     if char.isalnum() or char.isspace():
#         clean_string += char
#
# words = clean_string.split()
#
# hashtag = "#"
# for word in words:
#     hashtag += word[0].upper() + word[1:].lower()
#
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#
# print(hashtag)
