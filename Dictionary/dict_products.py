products = dict()

for i in range(0, 3):
    key = input("Enter the name of the product:")
    value = input("Enter the quantity of the product:")

    products[key] = value

print("Products in the dictionary:")

for key, value in products.items():
    print(f"{key}: {value}")
