import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\nEscolha uma operação para realizar no conjunto:")
    print("1. Adicionar um elemento")
    print("2. Remover um elemento")
    print("3. Verificar se um elemento existe")
    print("4. Listar todos os elementos")
    print("5. Limpar o conjunto")
    print("6. Sair\n")

my_set = set()
