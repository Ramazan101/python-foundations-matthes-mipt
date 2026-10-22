# # Список моделей которых необходимо напечатать
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []
#
# # Цикл последовательно печатает каждую модель до конца списка.
# # После печати каждая модель перемещается в список completed_models.
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print(f"Printing models: {current_designs}")
#     completed_models.append(current_designs)
#
# # Вывод всех готовых моделей
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing models: {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
