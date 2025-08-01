def main():
    while True:
        lista = []
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                print(f"Executando: Adicionar elemento à lista {lista}")
                adicionar_elemento(lista)
            case "2":
                print(f"Executando: Remover elemento da lista {lista}")
            case "3":
                print(f"Executando: Ordenar a lista {lista}")
            case "4":
                print(f"Executando: Reverter a lista {lista}")
            case "5":
                print(f"Executando: Inserir em posição na lista {lista}")
            case "6":
                print(f"Executando: Remover por índice da lista {lista}")
            case "7":
                print(f"Executando: Limpar a lista {lista}")
            case "8":
                print(f"Lista atual: {lista}")
            case _:
                print("Opção inválida. Tente novamente.")
                break


# Adiciona um elemento à lista
def adicionar_elemento(lista):
    elemento = input("Digite o elemento para adicionar: ")
    lista.append(elemento)
    print(f"'{elemento}' foi adicionado à lista.")


# Remove um elemento da lista
def remover_elemento(lista):
    elemento = input("Digite o elemento para remover: ")
    try:
        lista.remove(elemento)
        print(f"'{elemento}' foi removido da lista.")
    except ValueError:
        print(f"Erro: '{elemento}' não está na lista.")


# Ordena a lista
def ordenar_lista(lista):
    lista.sort()
    print("A lista foi ordenada.")


# Reverte a lista
def reverter_lista(lista):
    lista.reverse()
    print("A lista foi invertida.")


# Insere um elemento em uma posição específica
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


# Remove um elemento por índice
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


# Limpa toda a lista
def limpar_lista(lista):
    lista.clear()
    print("A lista foi completamente limpa.")


# Exibe os elementos da lista
def mostrar_lista(lista):
    print("Lista atual:", lista)


# Inicializa o programa
if __name__ == "__main__":
    main()
