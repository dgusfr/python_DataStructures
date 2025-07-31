# Estrutura de Dados em Python

## Sumário

1. [Tipos de Dados Agregados](#tipos-de-dados-agregados)
   - [Listas](#listas)
   - [Tuplas](#tuplas)
   - [Dicionários](#dicionarios)
   - [Conjuntos (Sets)](#conjuntos-sets)
2. [Estruturas de Dados Avançadas](#estruturas-de-dados-avancadas)
   - [Listas Ligadas (Linked Lists)](#listas-ligadas-linked-lists)
   - [Pilhas (Stacks)](#pilhas-stacks)
   - [Filas (Queues)](#filas-queues)
3. [Conclusão](#conclusao)

---

## Tipos de Dados Agregados

Tipos de dados agregados permitem armazenar múltiplos valores em uma única estrutura. 

### Listas

As listas são coleções ordenadas e **mutáveis**, permitindo armazenar elementos de diferentes tipos.

```python
lista = [1, 2, 3]

minha_lista = [42, "Python", 3.14, [1, 2, 3], {"chave": "valor"}]
```

**Características:**
- **Mutáveis**: Permitem adicionar, remover e modificar elementos.
- **Ordenadas**: Mantêm a sequência dos elementos.
- **Tamanho dinâmico**: Podem crescer e diminuir conforme necessário.
- **Indexação**: Cada elemento pode ser acessado por seu índice.

**Exemplo:**

```python
notas = [5, 6, 6]
media = sum(notas) / len(notas)
print(f"Média das notas: {media}")
```

### Métodos para Listas

- **Acessar elementos**:
  - `lista[1]`: Retorna o elemento na segunda posição, pois a indexação das listas começam com 0.
- **Adicionar elementos**:
  - `append(item)`: Adiciona um item ao final da lista.
  - `insert(posição, item)`: Insere um item na posição especificada.
  - `extend(iterável)`: Adiciona elementos de outro iterável à lista.
- **Remover elementos**:
  - `remove(item)`: Remove a primeira ocorrência do item.
  - `pop(posição)`: Remove e retorna o item na posição especificada.
  - `clear()`: Remove todos os elementos da lista.

---

### Tuplas

As tuplas são coleções ordenadas, porém **imutáveis** e utilizam parênteses.

```python
minha_tupla = (42, "Python", 3.14, [1, 2, 3], {"chave": "valor"})
```

**Características:**
- **Imutáveis**: Não podem ser modificadas após a criação.
- **Ordenadas**: Mantêm a sequência dos elementos.
- **Acessíveis por índice**: Permitem acessar elementos por sua posição.

**Exemplo:**

```python
coordenadas = (10, 20)
print(coordenadas[0])  # Saída: 10
```

> *Observação: Apesar de imutáveis, se uma tupla contiver uma lista, essa lista pode ser alterada.*

---

### Operações em Listas e Tuplas

Listas e tuplas, por serem sequências ordenadas, compartilham operações essenciais para manipulação de seus elementos.

### Acesso por Índice

O acesso a um elemento específico é feito através de seu índice, um número inteiro que representa sua posição na sequência. A contagem sempre se inicia em zero.

```python
lista = [10, 20, 30]
print(lista[1])  # Saída: 20

tupla = (11, 42, 64)
print(tupla[1])  # Saída: 42
```

O código `lista[1]` acessa o segundo elemento da lista (índice 1), que é o valor `20`. 

De forma análoga, `tupla[1]` acessa o segundo elemento da tupla, resultando em `42`. 

### Slicing (Fatiamento)

O fatiamento (`slicing`) extrai uma subsequência a partir de um intervalo de índices, especificado como `[start:stop]`. O elemento no índice `start` é incluído, mas o elemento no índice `stop` é excluído.

```python
lista = [10, 20, 30, 40]
print(lista[1:3])  # Saída: [20, 30]

tupla = (10, 20, 30, 40)
print(tupla[1:3])  # Saída: (20, 30)
```

A expressão `lista[1:3]` cria uma nova lista contendo os elementos do índice 1 (`20`) até o índice 2 (`30`), sem incluir o elemento do índice 3. 

O resultado é `[20, 30]`. O mesmo princípio se aplica à tupla, retornando uma nova tupla `(20, 30)`.

### Operador `in`

O operador `in` verifica a existência de um elemento dentro da sequência, retornando um valor booleano: `True` se o elemento for encontrado e `False` caso contrário.

```python
lista = [10, 20, 30]
print(20 in lista)  # Saída: True
print(40 in lista)  # Saída: False

tupla = (10, 20, 30)
print(20 in tupla)  # Saída: True
print(40 in tupla)  # Saída: False
```

Esta operação percorre a sequência para encontrar o valor. 

A expressão `20 in lista` retorna `True` porque `20` está presente na lista. Já `40 in lista` retorna `False`. 

A complexidade de tempo desta operação é, em média, linear, $O(n)$, pois no pior caso é necessário verificar todos os `n` elementos.


























___

### Dicionários

Os **dicionários** armazenam dados como pares **chave-valor**.

```python
meu_dicionario = {
    "nome": "Diego",
    "idade": 25,
    "cursos": ["Python", "Java", "C++"],
    "matriculado": True
}
```

**Características:**
- **Mutáveis**: Permitem adicionar, remover e modificar elementos.
- **Chaves únicas**: Cada chave deve ser única dentro do dicionário.
- **Acesso rápido**: Recuperação eficiente de valores associados a chaves.

**Métodos Úteis:**
- **Adicionar/Modificar**:
  - `dicionario[chave] = valor`
  - `update({chave: valor})`
- **Remover**:
  - `pop(chave)`
  - `del dicionario[chave]`
  - `clear()`

**Exemplo:**

```python
print(meu_dicionario["nome"])  # Saída: Diego
meu_dicionario["idade"] = 26  # Modificando valor
meu_dicionario["nota"] = 9.5  # Adicionando novo par
```

---

### Conjuntos (Sets)

Os **conjuntos** armazenam **valores únicos** e não mantêm ordem.

```python
frutas = {"maçã", "banana", "laranja"}
```

**Características:**
- **Elementos únicos**: Não permite duplicatas.
- **Operações matemáticas**: União, interseção, diferença.

**Exemplo:**

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # União: {1, 2, 3, 4, 5}
print(A & B)  # Interseção: {3}
print(A - B)  # Diferença: {1, 2}
```

---

## Estruturas de Dados Avançadas

### Listas Ligadas (Linked Lists)

Estruturas lineares onde cada nó contém um valor e uma referência ao próximo nó.

```python
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def inserir(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.head
        self.head = novo_no
    
    def exibir(self):
        atual = self.head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")
```

**Uso:**

```python
lista = LinkedList()
lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.exibir()  # Saída: 30 -> 20 -> 10 -> None
```

---

### Pilhas (Stacks)

Estrutura LIFO (Last In, First Out).

```python
class Pilha:
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        return self.itens.pop()

pilha = Pilha()
pilha.push(5)
pilha.push(10)
print(pilha.pop())  # Saída: 10
```

---

### Filas (Queues)

Estrutura FIFO (First In, First Out).

```python
from collections import deque

fila = deque()
fila.append(1)
fila.append(2)
fila.append(3)
print(fila.popleft())  # Saída: 1
```

---

## Conclusão

| Estrutura    | Ordenada | Mutável | Permite Duplicatas |
|-------------|---------|---------|----------------|
| **Lista** | ✅ | ✅ | ✅ |
| **Tupla** | ✅ | ❌ | ✅ |
| **Dicionário** | ✅ (Python 3.7+) | ✅ | ❌ (chaves únicas) |
| **Conjunto** | ❌ | ✅ | ❌ |

**Quando usar cada uma?**
- **Listas**: Quando precisar de uma coleção ordenada e mutável.
- **Tuplas**: Quando precisar de uma coleção ordenada e imutável.
- **Dicionários**: Quando precisar de acesso rápido por chave.
- **Conjuntos**: Quando precisar de elementos únicos e operações matemáticas entre coleções.

---