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

def start_program():
    clear_screen()
    print("Bem-vindo! Comece a gerenciar seu conjunto.")
    perform_operation()

def perform_operation():
    display_menu()
    option = input("Digite a opção desejada: ")
    match option:
        case "1":
            add_element()
        case "2":
            remove_element()
        case "3":
            check_element_exists()
        case "4":
            list_elements()
        case "5":
            clear_set()
        case "6":
            exit_program()
        case _:
            print("Opção inválida. Tente novamente.")
            perform_operation()

def add_element():
    element = input("Digite o elemento para adicionar: ")
    if element in my_set:
        print(f"O elemento '{element}' já existe no conjunto.")
    else:
        my_set.add(element)
        print(f"Elemento '{element}' adicionado com sucesso.")
    perform_operation()
