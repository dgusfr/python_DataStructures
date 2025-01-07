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

def remove_element():
    element = input("Digite o elemento para remover: ")
    if element in my_set:
        my_set.remove(element)
        print(f"Elemento '{element}' removido com sucesso.")
    else:
        print(f"O elemento '{element}' não foi encontrado no conjunto.")
    perform_operation()

def check_element_exists():
    element = input("Digite o elemento para verificar: ")
    if element in my_set:
        print(f"O elemento '{element}' existe no conjunto.")
    else:
        print(f"O elemento '{element}' não foi encontrado no conjunto.")
    perform_operation()

def list_elements():
    if len(my_set) == 0:
        print("O conjunto está vazio.")
    else:
        print("Elementos no conjunto:")
        for item in my_set:
            print(item)
    perform_operation()

def clear_set():
    my_set.clear()
    print("O conjunto foi limpo com sucesso.")
    perform_operation()

def exit_program():
    print("Encerrando o programa. Até logo!")
    exit()

def input_with_validation():
    while True:
        try:
            option = input("Digite uma opção: ")
            if option.isdigit() and 1 <= int(option) <= 6:
                return option
            else:
                print("Opção inválida. Digite um número entre 1 e 6.")
        except ValueError:
            print("Erro na entrada. Tente novamente.")

operation_count = 0

def increment_operation_count():
    global operation_count
    operation_count += 1
    print(f"Operações realizadas: {operation_count}")

def print_feedback(message):
    print(f"[INFO]: {message}")
