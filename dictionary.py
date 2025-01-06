import sys

def menu():
    print("\nMenu de Operações com Dicionário")
    print("1. Adicionar uma chave-valor")
    print("2. Atualizar valor de uma chave existente")
    print("3. Remover uma chave")
    print("4. Obter valor por chave")
    print("5. Verificar existência de chave")
    print("6. Listar todas as chaves")
    print("7. Listar todos os valores")
    print("8. Listar todos os pares chave-valor")
    print("9. Limpar o dicionário")
    print("10. Sair")

print("Menu inicializado.")


def adicionar_chave_valor(dicionario):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario[chave] = valor
    print(f"Chave-valor '{chave}: {valor}' adicionada com sucesso!")

def atualizar_valor(dicionario):
    chave = input("Digite a chave para atualizar: ")
    if chave in dicionario:
        novo_valor = input("Digite o novo valor: ")
        dicionario[chave] = novo_valor
        print(f"Valor da chave '{chave}' atualizado para '{novo_valor}'.")
    else:
        print(f"Chave '{chave}' não encontrada.")

def remover_chave(dicionario):
    chave = input("Digite a chave para remover: ")
    if chave in dicionario:
        del dicionario[chave]
        print(f"Chave '{chave}' removida com sucesso.")
    else:
        print(f"Chave '{chave}' não encontrada.")

def obter_valor(dicionario):
    chave = input("Digite a chave: ")
    if chave in dicionario:
        print(f"O valor associado à chave '{chave}' é '{dicionario[chave]}'.")
    else:
        print(f"Chave '{chave}' não encontrada.")

def verificar_chave(dicionario):
    chave = input("Digite a chave para verificar: ")
    if chave in dicionario:
        print(f"A chave '{chave}' existe no dicionário.")
    else:
        print(f"A chave '{chave}' não existe no dicionário.")

def listar_chaves(dicionario):
    print("Chaves no dicionário:")
    for chave in dicionario.keys():
        print(chave)

def listar_valores(dicionario):
    print("Valores no dicionário:")
    for valor in dicionario.values():
        print(valor)

def listar_pares(dicionario):
    print("Pares chave-valor no dicionário:")
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")
def limpar_dicionario(dicionario):
    dicionario.clear()
    print("Dicionário limpo com sucesso.")

def processar_opcao(opcao, dicionario):
    if opcao == '1':
        adicionar_chave_valor(dicionario)
    elif opcao == '2':
        atualizar_valor(dicionario)
    elif opcao == '3':
        remover_chave(dicionario)
    elif opcao == '4':
        obter_valor(dicionario)
    elif opcao == '5':
        verificar_chave(dicionario)
    elif opcao == '6':
        listar_chaves(dicionario)
    elif opcao == '7':
        listar_valores(dicionario)
    elif opcao == '8':
        listar_pares(dicionario)
    elif opcao == '9':
        limpar_dicionario(dicionario)
    elif opcao == '10':
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida. Tente novamente.")
