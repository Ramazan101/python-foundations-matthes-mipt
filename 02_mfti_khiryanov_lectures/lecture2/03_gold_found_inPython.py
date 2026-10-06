T = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
a, b, *rest = T
print(type(T))
print(T)
print(a)
print(a, b, rest)

*rest, a, b = T
print(type(T))
print(T)
print(rest, a, b)
