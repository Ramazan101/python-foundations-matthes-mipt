# # Задача 1
# # Создай функцию square(number), которая возвращает квадрат числа.
#
# def square(number):
#     # square_n = number ** 2
#     return number ** 2
# print(square(2))
#
#
# # Задача 2
# # Создай функцию is_even(number), которая возвращает True,
# # если число чётное, и False, если нечётное.
#
#
# def is_oven(number):
#     if number % 2 == 0:
#         return "True"
#     else:
#         return "False"
# print(is_oven(2))
# # Задача 3
# # Создай функцию max_number(a, b), которая возвращает большее число.
#
# def max_number(a, b):
#     return max(a, b)
# print(max_number(1, 3))
# # Задача 4
# # Создай функцию get_full_name(first_name, last_name).
#
# def get_full_name(first_name=str, last_name=str, middle_name=None):
#     if middle_name:
#         return first_name, last_name, middle_name
#     return first_name, last_name
#     return first_name, last_name
# n = list(get_full_name("Ramazan", "Ryskulov",))
# print(n)
# # Задача 5
# # Создай функцию calculate_discount(price, discount),
# # которая возвращает цену после скидки.
#
# def calculate_discount(price=int, discount=int):
#     pass
#
# # Задача 6
# # Создай функцию check_password(password).
# # Если длина пароля >= 8, вернуть "Надёжный",
# # иначе "Слабый".
# def check_password(password=str):
#     if len(password) > 8:
#         return "Your password is confident!"
#     else:
#         return "Your password is not confident!"
# print(check_password("adminadmin"))
# # Задача 7
# # Создай функцию student_info(name, age, city="Bishkek"),
# # которая возвращает словарь:
# # {"name": ..., "age": ..., "city": ...}
#
# def student_info(name, age, city) -> None:
#     person = {
#         "name": name,
#         "age": age,
#         "city": city
#     }
#     return person
# build_person = student_info("Кракен", 12, "Бишкек")
# print(build_person)




# 1. Удвоение чисел (map)
# Дан список [1, 2, 3, 4, 5]. Получи новый список, где каждое число умножено на 2.
nums = [1, 2, 3, 4, 5]
result1 = list(map(lambda number: number * 2, nums))
print(result1)




# 2. Чётные числа (filter)
# Дан список [1..10]. Оставь только чётные числа.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = list(filter(lambda number: number % 2 == 0, nums))
print(f"Только четные числа: {result2}")




# 3. Квадраты через lambda
# Используя lambda и map, получи квадраты чисел [1, 2, 3, 4].
nums = [1, 2, 3, 4]
result3 = list(map(lambda number: number ** 2, nums))
print(f"Квадраты: {result3}")




# 4. Пары имён и возрастов (zip)
# Получи список кортежей [("Аня", 20), ("Боря", 25), ("Вера", 30)]
names = ["Аня", "Боря", "Вера"]
ages = [20, 25, 30]
result4 = tuple(zip(names, ages))
print(result4)

# с циклом for
for name, age in zip(names, ages):
    print(name, age)




# 5. Суммы пар (zip + map)
# [1, 2, 3] и [10, 20, 30] -> [11, 22, 33]
a = [1, 2, 3]
b = [10, 20, 30]
result5 = list(map(sum, zip(a, b)))
print(result5)




# 6. Фильтр слов по длине (filter + lambda)
# Из списка оставь слова длиной больше 3
words = ["кот", "собака", "ёж", "слон", "мышь"]
result6 = list(filter(lambda word: len(word) > 3, words))
print(result6)




# 7. Все положительные? (all)
# Проверь, все ли числа в списке положительные. Ожидается True.
nums = [1, 2, 3, 4]
result7 = all(n for n in nums if n > 0)
print(result7)




# 8. Есть ли ноль? (any)
# Проверь, есть ли в списке хотя бы один ноль. Ожидается True.
nums = [1, 2, 0, 4]
result8 = any(n for n in nums if 0 in nums)
print(result8)




# 9. Все строки непустые? (all)
# Проверь, все ли строки непустые. Ожидается False.
strings = ["привет", "мир", "", "python"]
result9 = all(strings)
print(result9)




# 10. Есть ли слово длиннее 5 букв? (any + lambda)
# Ожидается True.
words = ["дом", "кот", "программирование", "лес"]
result10 = any(map(lambda word: len(word) > 5, words))
print(result10)



# 11. Приведение к верхнему регистру (map + lambda)
# ["hello", "world", "python"] -> ["HELLO", "WORLD", "PYTHON"]
words = ["hello", "world", "python"]
result11 = list(map(lambda word: word.upper(), words))
print(result11)



# 12. Только положительные (filter + lambda)
# Из списка оставь только положительные числа
nums = [-3, -1, 0, 2, 5, -7, 8]
result12 = list(filter(lambda num: num >= 0, nums))
print(result12)



# 13. Слияние словарей (zip + dict)
# keys и values -> {"a": 1, "b": 2, "c": 3}
keys = ["a", "b", "c"]
values = [1, 2, 3]
result13 = dict(zip(keys, values))
print(result13)



# 14. Проверка пароля (all + any)
# Проверь строку "Pass123":
#   all_alnum — все ли символы буквы или цифры
#   has_digit — есть ли хотя бы одна цифра
s = "Pass123"
# TODO: all_alnum = ...
# TODO: has_digit = ...
all_alnum = all(char.isalnum() for char in s)
has_digit = any(digit.isdigit() for digit in s)

print(all_alnum)
print(has_digit)


# 15. Индексы чётных чисел (filter + lambda + enumerate)
# [10, 15, 20, 25, 30] -> [0, 2, 4]
nums = [10, 15, 20, 25, 30]

even_pairs = filter(lambda pair: pair[1] % 2 == 0, enumerate(nums))
result15 = list(map(lambda pair: pair[0], even_pairs))

print(result15)