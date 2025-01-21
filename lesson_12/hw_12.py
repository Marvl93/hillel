# ДЗ 12.2. Корзина для покупок
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f'{self.name}: {self.description} {self.dimensions}, price: {self.price}'
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f'{self.name} {self.surname}\n{self.numberphone}'
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         all_products = ""
#         for product, count in self.products.items():
#             all_products += f"\n{product.name} - {count} pcs."
#         return f"User: {self.user}\nItems:{all_products}"
#
#     @property
#     def get_total(self):
#         all_sum = 0
#         for product, count in self.products.items():
#             all_sum += (product.price * count)
#         return all_sum
#
#
# lemon = Item('lemon', 5, "yellow", "small")
# apple = Item('apple', 2, "red", "middle")
# print(lemon)
# print(apple)
#
# buyer = User("Ivan", "Ivanov", "Phone: 2341232324")
# print(buyer)
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# print(f"Total price: {cart.get_total}")
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total == 60, "Всього 60"
# assert cart.get_total == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
# # assert cart.get_total == 40
# print(f"Total price: {cart.get_total}")


# ДЗ 12.1. Очистити текст від html-тегів

import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ''
    tag = False

    for char in html:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            cleaned_text += char

    # Розбиваємо текст на рядки і видаляємо порожні рядки або ті, що містять лише пробіли
    cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]

    # Об'єднуємо очищені рядки в один текст
    cleaned_text = '\n'.join(cleaned_lines)
    # Записуємо в файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)


delete_html_tags('draft.html')
