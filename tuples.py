import sys

if sys.version_info < (3, 6):
    print("Este script requer Python 3.6 ou superior.")
    sys.exit(1)

def menu():
    print("\nMenu de Operações com Tupla")
    print("1. Criar uma tupla")
    print("2. Concatenar tuplas")
    print("3. Obter elemento por índice")
    print("4. Contar ocorrências de um elemento")
    print("5. Obter índice de um elemento")
    print("6. Verificar se um elemento existe")
    print("7. Mostrar a tupla atual")
    print("8. Sair")

def main():
    tupla = ()  # Tupla inicial vazia
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        try:
            processar_opcao(opcao, tupla)
        except ValueError as e:
            print(f"Erro: {e}")

def criar_tupla():
    elementos = input("Digite os elementos da tupla separados por vírgula: ")
    nova_tupla = tuple(elementos.split(","))
    print(f"Tupla criada: {nova_tupla}")
    return nova_tupla

def concatenar_tuplas(tupla):
    elementos = input("Digite os elementos para concatenar, separados por vírgula: ")
    nova_tupla = tuple(elementos.split(","))
    resultado = tupla + nova_tupla
    print(f"Resultado da concatenação: {resultado}")
    return resultado

def concatenar_tuplas(tupla):
    elementos = input("Digite os elementos para concatenar, separados por vírgula: ")
    nova_tupla = tuple(elementos.split(","))
    resultado = tupla + nova_tupla
    print(f"Resultado da concatenação: {resultado}")
    return resultado

def processar_opcao(opcao, tupla):
    if opcao == '1':
        tupla = criar_tupla()
    elif opcao == '2':
        tupla = concatenar_tuplas(tupla)
    elif opcao == '3':
        obter_elemento_por_indice(tupla)
    elif opcao == '4':
        contar_ocorrencias(tupla)
    elif opcao == '5':
        obter_indice(tupla)
    elif opcao == '6':
        verificar_elemento(tupla)
    elif opcao == '7':
        mostrar_tupla(tupla)
    elif opcao == '8':
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida. Tente novamente.")