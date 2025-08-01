def main():
    print(
        """
        Menu de Operações com Lista\n
        1. Adicionar um elemento
        2. Remover um elemento
        3. Ordenar a lista
        4. Reverter a lista
        5. Inserir em uma posição específica
        6. Remover por índice
        7. Limpar a lista
        8. Mostrar a lista atual
        9. Sair
        """
    )

    lista = []
    while True:
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                adicionar_elemento(lista)
            case "2":
                remover_elemento(lista)
            case "3":
                ordenar_lista(lista)
            case "4":
                reverter_lista(lista)
            case "5":
                inserir_em_posicao(lista)
            case "6":
                remover_por_indice(lista)
            case "7":
                limpar_lista(lista)
            case "8":
                mostrar_lista(lista)
            case "9":
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                break


def adicionar_elemento(lista):
    elemento = input("Digite o elemento para adicionar: ")
    lista.append(elemento)
    print(f"'{elemento}' foi adicionado à lista.")


def remover_elemento(lista):
    elemento = input("Digite o elemento para remover: ")
    try:
        lista.remove(elemento)
        print(f"'{elemento}' foi removido da lista.")
    except ValueError:
        print(f"Erro: '{elemento}' não está na lista.")


def ordenar_lista(lista):
    lista.sort()
    print("A lista foi ordenada.")


def reverter_lista(lista):
    lista.reverse()
    print("A lista foi invertida.")


def inserir_em_posicao(lista):
    elemento = input("Digite o elemento para inserir: ")
    try:
        posicao = int(input("Digite a posição (índice): "))
        if 0 <= posicao <= len(lista):
            lista.insert(posicao, elemento)
            print(f"'{elemento}' foi inserido na posição {posicao}.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido para a posição.")


def remover_por_indice(lista):
    try:
        posicao = int(input("Digite o índice para remover: "))
        if 0 <= posicao < len(lista):
            elemento = lista.pop(posicao)
            print(f"'{elemento}' foi removido da posição {posicao}.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido para o índice.")


def limpar_lista(lista):
    lista.clear()
    print("A lista foi completamente limpa.")


def mostrar_lista(lista):
    print("Lista atual:", lista)


if __name__ == "__main__":
    main()
