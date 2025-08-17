from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

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

    def __setitem__(self, posicao_desejada, elemento):
        ponteiro = self.head
        for i in range(posicao_desejada):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("list index out of range")
        if ponteiro:
            ponteiro.data = elemento
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        ponteiro = self.head
        indice = 0
        while ponteiro:
            if ponteiro.data == elemento:
                return indice
            ponteiro = ponteiro.next
            indice = indice + 1
        raise ValueError("{} is not in list".format(elemento))

    def _getnode(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("list index out of range")
        ponteiro = self.head
        for _ in range(index):
            ponteiro = ponteiro.next
        return ponteiro

    def insere_final_lista(self, elemento):
        if self.head:
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next
            ponteiro.next = Node(elemento)
        else:
            self.head = Node(elemento)
        self._size = self._size + 1

    def insere_qualquer_posicao(self, index, elemento):
        if index < 0 or index > self._size:
            raise IndexError("list index out of range")

        node = Node(elemento)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            anterior = self._getnode(index - 1)
            node.next = anterior.next
            anterior.next = node
        self._size = self._size + 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            ponteiro = self.head.next
            while ponteiro:
                if ponteiro.data == elem:
                    ancestor.next = ponteiro.next
                    ponteiro.next = None
                    self._size = self._size - 1
                    return True
                ancestor = ponteiro
                ponteiro = ponteiro.next
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self):
        r = ""
        ponteiro = self.head
        while ponteiro:
            r = r + str(ponteiro.data) + "->"
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()
