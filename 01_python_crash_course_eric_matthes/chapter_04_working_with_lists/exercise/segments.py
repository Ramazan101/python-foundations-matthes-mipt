"""4.10. Сегменты: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
который делает следующее:
• Выводит сообщение «The irst three items in the list are:», а затем использует сегмент
для вывода первых трех элементов из списка.
• Выводит сообщение «Three items from the middle of the list are:», а затем использует
сегмент для вывода первых трех элементов из середины списка.
• Выводит сообщение «The last three items in the list are:», а затем использует сегмент
для вывода последних трех элементов из списка.
"""

foods_name = ["potato", "pizza", "mushroom cake", "beshbarmak", "chiz cake"]

print(f"The irst three items in the list are: {foods_name[:3]}")

print(f"Three items from the middle of the list are: {foods_name[1:4]}")

print(f"The last three items in the list are: {foods_name[-3:]}")

"""4.11. Моя пицца, твоя пицца: начните с программы из упражнения 4.1. Создайте копию
списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее:
• Добавьте новую пиццу в исходный список.
• Добавьте другую пиццу в список friend_pizzas.
• Докажите, что в программе существуют два разных списка. Выведите сообщение
«My favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение
«My friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том,
что каждая новая пицца находится в соответствующем списке."""

the_foods = ["pizza chiz", "pizza paperoni", "pizza mushroom", "pizza potato"]
friend_pizzas = the_foods[:]

the_foods.append("pizza just")
print(f"My favorite pizzas are: ")

for my_pizza in the_foods:
    print(my_pizza)



friend_pizzas.append("pizza smash")
print(f"\nMy friend's favorite pizzas are:")

for my_fr in friend_pizzas:
    print(my_fr)



"""4.12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования
цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла for для вывода каждого списка."""




