# 1. Частоты элементов в Tuple → Dict.

def tuple_frequencies(t: tuple): # t = (1, 2, 1, 3, 2, 1)
    seen = {}           # {1: 3, 2: 2, 3: 1}
    for key in t:
        if key not in seen:
            seen[key] = 1
        else:
            seen[key] += 1

    return seen


# пример:
print(tuple_frequencies((1, 2, 1, 3, 2, 1)))
# {1: 3, 2: 2, 3: 1}



# 2. Перемести нули в конец (сохрани порядок остальных)
def move_zeroes(nums): # nums = [0, 1, 0, 3, 12]
    count_zeroes = []
    non_zeros = []
    for x in nums:
        if x != 0:
            non_zeros.append(x)
        elif x == 0:
            count_zeroes.append(x)

    return non_zeros + count_zeroes


    # non_zeros = [x for x in nums if x != 0]
    #
    # count_zeroes = nums.count(0)
    #
    # return non_zeros + [0] * count_zeroes


# l = [0] * 2
# print(l)
# пример:
arr = [0, 1, 0, 3, 12]
print(move_zeroes(arr))
# [1, 3, 12, 0, 0]


# 3. Есть ли повтор?
def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)

# nums = [1, 2, 3, 3]
# n = set(nums)
# print(len(n))

# пример:
print(contains_duplicate([1, 2, 3, 3])) # 3
# True                   #0 #1 #2 #3 = 4
print(contains_duplicate([1, 2, 3, 4])) # 4
# False




# 4. Найти индексы суммы
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

# пример:
print(two_sum([3, 4, 5, 6], 7))
# [0, 1]
print(two_sum([4, 5, 6], 10))
# [0, 2]
print(two_sum([5, 5], 10))
# [0, 1]




# 5. Слить два словаря: при совпадении ключей сложить значения.
def merge_dicts_sum(a, b):
    result = a.copy()

    for key, value in b.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result

# пример:
print(merge_dicts_sum({"x": 1, "y": 2}, {"y": 5, "z": 3}))
# {'x': 1, 'y': 7, 'z': 3}

