def get_users(names):
    """Вывод простого приветствия для каждого пользователя"""
    for name in names:
        msg = f"Hell, {name.title()}!"
        print(msg)
usernames = ["hannah", "ty", "tamara"]
get_users(usernames)
