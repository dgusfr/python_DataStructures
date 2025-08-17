from linked_list import LinkedList


def imprime_estado(titulo, lista: LinkedList):
    print(f"\n{titulo}")
    print("Lista:", str(lista))
    print("Tamanho:", lista.tamanho_lista())


def testa_insercoes_finais():
    print("=== Teste: Inserções no final ===")
    l = LinkedList()
    imprime_estado("Inicial", l)
    l.insere_final_lista(8)
    imprime_estado("Após inserir 8 no final", l)
    l.insere_final_lista(6)
    imprime_estado("Após inserir 6 no final", l)
    l.insere_final_lista(10)
    imprime_estado("Após inserir 10 no final", l)
    return l


def testa_insercoes_qualquer_posicao():
    print("\n=== Teste: Inserções em qualquer posição ===")
    l = LinkedList()
    l.insere_qualquer_posicao(0, 1)
    imprime_estado("Após inserir 1 em index 0 (vazia)", l)
    l.insere_qualquer_posicao(1, 3)
    imprime_estado("Após inserir 3 no fim (index==_size)", l)
    l.insere_qualquer_posicao(1, 2)
    imprime_estado("Após inserir 2 no meio (index 1)", l)
    l.insere_qualquer_posicao(0, 0)
    imprime_estado("Após inserir 0 no início (index 0)", l)
    l.insere_qualquer_posicao(l.tamanho_lista(), 4)
    imprime_estado("Após inserir 4 no fim", l)
    return l


def testa_getitem_setitem(l: LinkedList):
    print("\n=== Teste: __getitem__ e __setitem__ ===")
    imprime_estado("Estado atual", l)
    try:
        print("Elemento na posição 0:", l[0])
        print("Elemento na posição 2:", l[2])
    except IndexError as e:
        print("IndexError ao acessar:", e)
    try:
        l[2] = 99
        imprime_estado("Após setitem [2]=99", l)
    except IndexError as e:
        print("IndexError ao atribuir:", e)
    try:
        _ = l[-1]
    except IndexError as e:
        print("IndexError esperado ao acessar índice negativo:", e)
    try:
        _ = l[l.tamanho_lista()]
    except IndexError as e:
        print("IndexError esperado ao acessar índice >= tamanho:", e)


def testa_index(l: LinkedList):
    print("\n=== Teste: index(valor) ===")
    try:
        print("Índice do valor 99:", l.index(99))
    except ValueError as e:
        print("ValueError inesperado ao buscar 99:", e)
    try:
        print("Índice do valor 123 (inexistente):", l.index(123))
    except ValueError as e:
        print("ValueError esperado ao buscar inexistente:", e)


def testa_remocoes():
    print("\n=== Teste: Remoções ===")
    l = LinkedList()
    for x in [1, 2, 3, 4]:
        l.insere_final_lista(x)
    imprime_estado("Inicial (1->2->3->4)", l)
    try:
        l.remove(3)
        imprime_estado("Após remover 3 (meio)", l)
    except ValueError as e:
        print("ValueError inesperado ao remover 3:", e)
    try:
        l.remove(1)
        imprime_estado("Após remover 1 (head)", l)
    except ValueError as e:
        print("ValueError inesperado ao remover 1:", e)
    try:
        l.remove(4)
        imprime_estado("Após remover 4 (tail)", l)
    except ValueError as e:
        print("ValueError inesperado ao remover 4:", e)
    try:
        l.remove(999)
    except ValueError as e:
        print("ValueError esperado ao remover inexistente:", e)
    l_vazia = LinkedList()
    try:
        l_vazia.remove(1)
    except ValueError as e:
        print("ValueError esperado ao remover em lista vazia:", e)
    return l


def testa_fluxo_completo():
    print("\n=== Fluxo completo ===")
    l = LinkedList()
    imprime_estado("Inicial", l)
    for x in [10, 20, 40]:
        l.insere_final_lista(x)
    imprime_estado("Após inserir 10,20,40 no fim", l)
    l.insere_qualquer_posicao(2, 30)
    imprime_estado("Após inserir 30 em index 2", l)
    print("Valor em [1]:", l[1])
    l[1] = 25
    imprime_estado("Após setitem [1]=25", l)
    print("Index do valor 30:", l.index(30))
    l.remove(10)
    imprime_estado("Após remover 10 (head)", l)
    l.remove(30)
    imprime_estado("Após remover 30 (meio)", l)
    l.remove(40)
    imprime_estado("Após remover 40 (tail)", l)
    imprime_estado("Final", l)


if __name__ == "__main__":
    lista_final = testa_insercoes_finais()
    lista_varias_pos = testa_insercoes_qualquer_posicao()
    testa_getitem_setitem(lista_varias_pos)
    testa_index(lista_varias_pos)
    lista_apos_remocoes = testa_remocoes()
    testa_fluxo_completo()
