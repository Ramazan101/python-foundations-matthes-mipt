# Создай validate_password(password). Пароль должен соответствовать всем условиям:
# Минимум 8 символов.
# Хотя бы одна заглавная буква.
# Хотя бы одна строчная буква.
# Хотя бы одна цифра.
# Хотя бы один специальный символ.
# Функция должна возвращать True или False.
# Пример: validate_password("Python123!") → True

# import string
SPECIAL_CHAR = set(string.punctuation)

def validate_password(password: str) -> bool:
    if len(password) <= 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in SPECIAL_CHAR:
            has_special = True

        if has_upper and has_lower and has_digit and has_special:
            return True

    return False


print(validate_password("HelloWorld1!"))  # True
print(validate_password("Python123!"))    # True
print(validate_password("short1!A"))      # False




def is_animal(animals: list[str]) -> dict:
    seen = {}

    for animal in animals:
        seen[animal] = seen.get(animal, 0) + 1


    return seen

print(is_animal(["cat", "dog", "cat"]))



# найти второе максимальное число
def find_max_num(numbers: list[int]) -> int:
    max_num = max(numbers)

    smaller_char = [num for num in numbers if num < max_num]

    if not smaller_char:
        raise ValueError("Все элементы в списке одинаковы")

    return max(smaller_char)

print(find_max_num([40, 25, 10, 28, 17]))
