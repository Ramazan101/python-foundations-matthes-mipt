def describe_pet(animal_type, animal_name):
    """Вывод инфы о животном"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")

"""Именованные аргументы"""
describe_pet(animal_type="cat", animal_name="marus")
"""Многократные вызовы функций"""
describe_pet("dog", "lion")
describe_pet("hamster", "buba")
#два вызова функции эквивалентны:
describe_pet(animal_name="kanchuk", animal_type="dog")

# ПРИМЕЧАНИЕ При использовании именованных аргументов будьте внимательны —
# имена должны точно совпадать с именами параметров из определения функции.


"""Значения по умолчанию"""
def describe_pet(animal_name, animal_type="dog"):
    """Вывод инфы о животном"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}.")
describe_pet(animal_name="wille")
