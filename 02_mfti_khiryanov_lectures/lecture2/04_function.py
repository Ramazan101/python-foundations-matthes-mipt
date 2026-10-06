def hello_n(name: str, n: int):
    for idx in range(1, n + 1):
        print("Hello",name.title())

# hello_n("asan", 2)
# hello_n("alex", 10)
vasily = "alex", 12
hello_n(*vasily)