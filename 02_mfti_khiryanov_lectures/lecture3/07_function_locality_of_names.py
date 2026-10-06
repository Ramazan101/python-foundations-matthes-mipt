# def foo(x) -> int: # 'annotation' another called 'comment'.
#     return x * 2
#
# y = foo(32)
# print(y) # если передаваемый переменный будет не y а х
#          # тогда будет NameError
#
#
#
# # DuckTyping
# def foo(x: str, y: int) -> str:
#     result = x
#     for i in range(y - 1):
#         result += x
#     return result
#
# t = foo("ma", 2)
# print(t)
#
#
#
# def count_letters(text : str):
#     vowels = set("aeiou")
#
#     result = {
#         "Гласных": 0,
#         "Согласных": 0
#     }
#
#     for char in text.lower():
#         if char.isalpha():
#             if char in vowels:
#                 result["Гласных"] += 1
#             else:
#                 result["Согласных"] += 1
#     return result
#
# print(count_letters("Hello world!"))
#
#
#
# def word_count(text: str):
#     words = text.split()
#
#     return {
#         "total_words": len(words),
#         "unique_words": len(set(words))
#     }
#
#
# print(word_count("hello world helo"))
#
#
# def filter_long_word(words: str, n: int) -> list:
#     return [word for word in words if len(word) > n]
#
#
# words = ["apple", "cat", "banana", "dog"]
# print(filter_long_word(words, 3))
#
#
#
# def count_numbers(nums: list[int]):
#     result = {}
#
#     for num in nums:
#         if num in result:
#             result[num] += 1
#         else:
#             result[num] = 1
#
#     return result
#
# print(count_numbers([1, 2, 2, 3, 1, 1]))


def foo(x, y, z):

    return 100*x + y*2 + z*1


print(foo(1,10,3))
print(foo(z=1, y=10, x=3)) # named parameters
# print(foo(1, 2)) # TypeError: foo() missing 1 required positional argument: 'z'



def bar(*args, named_parameters="bar"):
    for arg in args:
        print(named_parameters, "arg", arg)


bar(1, 2, 3, 4, 5, 6, 7)
# bar(1, 2, 3) # TypeError: bar() takes 1 positional argument but 3 were given
bar(["jelly", "fish"])
bar("jelly", "fish", named_parameters="VICTOR")


# Пространство имён — это обычный ассоциативный массив (словарь Python dict),
# где ключами являются строки с именами переменных, а значениями — ссылки на объекты в памяти.
# У каждого изолированного контекста есть свой личный словарь:
# -- Глобальное пространство (__main__): имена, объявленные на уровне файла.
# -- Локальное пространство функции: создаётся заново в момент вызова функции внутри её фрейма в стеке.


#Локальность означает, что переменные, созданные внутри функции, существуют
#только пока эта функция живёт на вершине стека, и не видны снаружи.

x = 10 # global name x (lives in __main__)

def foo():
    x = 42 # local name x (lives inside frame foo)
    print("inside foo", x)

foo() # output 42
print("inside __main__: ", x) # output 10
