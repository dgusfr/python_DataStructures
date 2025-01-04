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
