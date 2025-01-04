import sys

# Verifica se o Python é compatível
if sys.version_info < (3, 6):
    print("Este script requer Python 3.6 ou superior.")
    sys.exit(1)

def menu():
    print("\nMenu de Operações com Lista")
    print("1. Adicionar um elemento")
    print("2. Remover um elemento")
    print("3. Ordenar a lista")
    print("4. Reverter a lista")
    print("5. Inserir elemento em uma posição")
    print("6. Remover elemento por índice")
    print("7. Limpar a lista")
    print("8. Mostrar a lista")
    print("9. Sair")

def main():
    lista = []  # Lista inicial
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        try:
            processar_opcao(opcao, lista)
        except ValueError as e:
            print(f"Erro: {e}")

def processar_opcao(opcao, lista):
    if opcao == '1':
        adicionar_elemento(lista)
    elif opcao == '2':
        remover_elemento(lista)
    elif opcao == '3':
        ordenar_lista(lista)
    elif opcao == '4':
        reverter_lista(lista)
    elif opcao == '5':
        inserir_em_posicao(lista)
    elif opcao == '6':
        remover_por_indice(lista)
    elif opcao == '7':
        limpar_lista(lista)
    elif opcao == '8':
        mostrar_lista(lista)
    elif opcao == '9':
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida. Tente novamente.")
