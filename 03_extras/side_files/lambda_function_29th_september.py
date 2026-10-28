products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 20},
    {"name": "Keyboard", "price": 50},
    {"name": "Monitor", "price": 300},
]


expensive = list(
    filter(
        lambda product: product["price"] > 100,
        products
    )
)

sorted_products = sorted(
    products,
    key=lambda product: product["price"],
    reverse=True
)

print(sorted_products)

print(expensive)