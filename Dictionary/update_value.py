estoque = {"Caderno universitário": 50, "Caneta azul": 120, "Borracha branca": 30}


def update_item(prod):
    if prod not in estoque:
        print(f"Product '{prod}' not found in the inventory.")
    else:
        quantity = int(input("Enter the new quantity: "))
        estoque[prod] = quantity
        show_inventory()


def show_inventory():
    for key, value in estoque.items():
        print(f"{key}: {value}")


product = input("Enter the name of the product: ")

update_item(product)
