# #ДЗ 9.1. Визначити популярність певних слів у тексті
# def popular_words(text, words, index=0, word_count=None):
#     if word_count is None:
#         word_count = {word: 0 for word in words}
#
#     if index >= len(text):
#         return word_count
#
#     text_words = text.lower().split()
#
#     current_word = text_words[index] if index < len(text_words) else None
#     if current_word in word_count:
#         word_count[current_word] += 1
#
#     return popular_words(text, words, index + 1, word_count)
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {
#     'i': 4,
#     'was': 3,
#     'three': 0,
#     'near': 0
# }, 'Test1'
#
# print('OK')

# ДЗ 9.2. Різниця між числами

def difference(*args):
    # Якщо аргументів немає, повертаємо 0
    if not args:
        return 0
    # Різниця макс мін
    result = max(args) - min(args)
    return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')