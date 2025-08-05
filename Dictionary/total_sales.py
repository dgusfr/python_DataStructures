sales = {
    "Eletrônicos": [
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000},
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500},
    ],
    "Eletrodomésticos": [
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000},
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800},
    ],
    "Livros": [
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50},
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100},
    ],
}


def total_sales(sales):
    for category, items in sales.items():
        total_sales = 0
        for item in items:
            total_sales += item["quantidade"] * item["valor_unitario"]

        print(f"Total sales for {category}: R$ {total_sales:.2f}")


total_sales(sales)
