lista_de_compras = ["Macarrão", "Arroz", "Banana"]

item = input("Enter the item you want to verify:")

if item in lista_de_compras:
    print(f"{item} já consta na lista.")
else:
    print(f"O {item} precisa ser comprado.")
