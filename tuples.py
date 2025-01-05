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
