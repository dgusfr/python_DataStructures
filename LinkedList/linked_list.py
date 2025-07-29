from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insere_final_lista(self, elemento):
        if self.head:
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next
            ponteiro.next = Node(elemento)
        else:
            self.head = Node(elemento)
        self._size = self._size + 1

    def tamanho_lista(self):
        return self._size

    def __getitem__(self, posicao_desejada):
        ponteiro = self.head
        for i in range(posicao_desejada):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        if ponteiro:
            return ponteiro.data
        raise IndexError("list index out of range")

    def __setitem__(self, posicao_desejada, elem):
        ponteiro = self.head
        for i in range(posicao_desejada):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        if ponteiro:
            ponteiro.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        pointer = self.head
        indice = 0
        while pointer:
            if pointer.data == elemento:
                return indice
            pointer = pointer.next
            indice = indice + 1
        raise ValueError("{} is not in list".format(elemento))
