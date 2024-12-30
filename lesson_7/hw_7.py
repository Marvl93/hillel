#7.1. Вітання
#
# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

#7.2. Модифікувати рядок

# def correct_sentence(text):
#     sentences = text.split(". ")
#     corrected_sentences = []
#     for sentence in sentences:
#         sentence = sentence.strip()
#         if sentence:
#             sentence = sentence[0].upper() + sentence[1:]
#             if not sentence.endswith("."):
#                 sentence += "."
#             corrected_sentences.append(sentence)
#     return " ".join(corrected_sentences)
#
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

# 7.3. Пошук підрядка

# def second_index(text, some_str):
#     first_index = text.find(some_str)
#     if first_index == -1:
#         return None
#     second_index = text.find(some_str, first_index + 1)
#     return second_index if second_index != -1 else None
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

# 7.4. Пошук спільних елементів

def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}  # Числа, кратні 3
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}  # Числа, кратні 5
    common = {x for x in multiples_of_3 if x in multiples_of_5}
    return common


result = common_elements()
print(result)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ok")
