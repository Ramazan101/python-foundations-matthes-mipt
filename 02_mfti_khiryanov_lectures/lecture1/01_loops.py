# brute force 'not using elif'.
x = int(input())
y = int(input())

# if x > 0 and y > 0:
#     print(1)
# else:
#     if x < 0 and y > 0:
#         print(2)
#     else:
#         if x < 0 and y < 0:
#             print(3)
#         else:
#             if x > 0 and y < 0:
#                 print(4)
#             else:
#                 print("Never")

# using elif
# is_activate = True
# while is_activate:
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("Never")