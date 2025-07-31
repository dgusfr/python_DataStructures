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

## Listas

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

Listas em Python possuem métodos específicos para manipular seus elementos. Essas operações, em sua maioria, modificam a lista original diretamente (operações "in-place").

Vamos usar uma lista de tarefas como exemplo prático:

```python
tarefas = ['Revisar código', 'Atualizar documentação', 'Testar novo endpoint']
```

#### Adicionar Elementos

**`.append(item)`**
Adiciona um único item ao final da lista. É a forma mais eficiente de adicionar um elemento, pois tem complexidade de tempo amortizada de $O(1)$.

```python
tarefas.append('Deploy em staging')

print(f"Após append: {tarefas}")
# Saída: Após append: ['Revisar código', 'Atualizar documentação', 'Testar novo endpoint', 'Deploy em staging']
```

**`.insert(índice, item)`**
Insere um item em uma posição específica, deslocando os elementos subsequentes para a direita.

```python
tarefas.insert(1, 'Corrigir bug #123')

print(f"Após insert: {tarefas}")
# Saída: Após insert: ['Revisar código', 'Corrigir bug #123', 'Atualizar documentação', 'Testar novo endpoint', 'Deploy em staging']
```

#### Remover Elementos

**`.remove(item)`**
Remove a primeira ocorrência do valor especificado. Se o item não existir, levanta um erro `ValueError`.

```python
tarefas.remove('Atualizar documentação')

print(f"Após remove: {tarefas}")
# Saída: Após remove: ['Revisar código', 'Corrigir bug #123', 'Testar novo endpoint', 'Deploy em staging']
```

**`.pop(índice)`**
Remove e **retorna** o elemento de uma posição. Se nenhum índice for fornecido, remove e retorna o último item da lista.

```python
tarefa_removida = tarefas.pop(0) # Remove do índice 0
print(f"Tarefa removida: '{tarefa_removida}'") # Saída: Tarefa removida: 'Revisar código'
print(f"Após pop(0): {tarefas}") # Saída: Após pop(0): ['Corrigir bug #123', 'Testar novo endpoint', 'Deploy em staging']

ultima_tarefa = tarefas.pop() # Remove o último
print(f"Última tarefa removida: '{ultima_tarefa}'") # Saída: Última tarefa removida: 'Deploy em staging'
print(f"Após pop(): {tarefas}") # Saída: Após pop(): ['Corrigir bug #123', 'Testar novo endpoint']
```

**`.clear()`**
Remove todos os elementos, deixando a lista vazia.

```python
tarefas.clear()

print(f"Após clear: {tarefas}")
# Saída: Após clear: []
```

### Ordenar Elementos

**`.sort()`**
Ordena os elementos da lista "in-place" (modifica a própria lista). Por padrão, a ordem é ascendente (alfabética para strings, numérica para números).

```python
tarefas = ['Testar API', 'Corrigir bug', 'Atualizar docs', 'Refatorar código']
tarefas.sort()

print(f"Após sort(): {tarefas}")
# Saída: Após sort(): ['Atualizar docs', 'Corrigir bug', 'Refatorar código', 'Testar API']

# Ordenando em ordem decrescente
tarefas.sort(reverse=True)

print(f"Após sort(reverse=True): {tarefas}")
# Saída: Após sort(reverse=True): ['Testar API', 'Refatorar código', 'Corrigir bug', 'Atualizar docs']
```

**`.reverse()`**
Inverte a ordem atual dos elementos da lista, também "in-place".

```python
tarefas.reverse()

print(f"Após reverse(): {tarefas}")
# Saída: Após reverse(): ['Atualizar docs', 'Corrigir bug', 'Refatorar código', 'Testar API']
```


---

<br>

___

## Tuplas

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

### Métodos para Tuplas

Como tuplas são imutáveis, não temos métodos de alteração.

___

<br>

___


## Operações em Listas e Tuplas

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

Dando continuidade, a iteração é o processo de percorrer os elementos de uma sequência, um a um, para executar uma determinada operação em cada um deles.

### Iteração sobre Elementos

Tanto listas quanto tuplas são objetos iteráveis, o que significa que seus elementos podem ser acessados sequencialmente utilizando laços de repetição, como o `for`.

```python
lista = [1, 2, 3, 4]
for item in lista:
    print(item)

tupla = (1, 2, 3, 4)
for item in tupla:
    print(item)
```

Em ambos os casos, o laço `for` percorre a coleção (`lista` ou `tupla`). A cada iteração, o próximo elemento da sequência é atribuído à variável `item`, e o bloco de código dentro do laço (neste caso, `print(item)`) é executado. O processo se repete até que todos os elementos tenham sido visitados.

Por baixo dos panos, o laço `for` utiliza o protocolo de iteração do Python. Ele solicita um "iterador" do objeto (a lista ou tupla) e, a cada passo, chama a função `next()` nesse iterador para obter o próximo item, até que a exceção `StopIteration` seja levantada, sinalizando o fim da sequência. 

Essa abstração torna o código limpo e eficiente para percorrer qualquer tipo de sequência.


___


### Desempacotamento de Sequências

O desempacotamento (ou *unpacking*) permite que os itens de um iterável, como uma lista ou tupla, sejam distribuídos em variáveis individuais em uma única linha de atribuição. A condição principal é que o número de variáveis à esquerda do operador de atribuição (`=`) deve ser igual ao número de elementos na sequência.

```python
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"x={x}, y={y}, z={z}") # Saída: x=10, y=20, z=30

# Desempacotamento de Lista
dados = [10, 20, 30]
a, b, c = dados
print(f"a={a}, b={b}, c={c}") # Saída: a=10, b=20, c=30
```

Na prática, a atribuição `x, y, z = coordenadas` mapeia cada variável a um elemento da tupla na ordem correspondente: `x` recebe `coordenadas[0]`, `y` recebe `coordenadas[1]`, e assim por diante. Esse mecanismo é mais legível e conciso do que realizar atribuições individuais por índice (`x = coordenadas[0]`, `y = coordenadas[1]`, etc.).

O Python também suporta o **desempacotamento estendido** com o operador `*`, que permite capturar múltiplos itens restantes em uma nova lista. Isso é útil quando não se sabe o tamanho exato da sequência ou se deseja separar apenas os primeiros e/ou últimos elementos.

```python
numeros = [1, 2, 3, 4, 5]
primeiro, *meio, ultimo = numeros

print(primeiro)  # Saída: 1
print(meio)      # Saída: [2, 3, 4]
print(ultimo)    # Saída: 5
```


___

### Concatenação de Tuplas e Listas

Tanto tuplas quanto listas suportam o operador de concatenação (`+`) para combinar duas sequências em uma nova. É fundamental entender que essa operação sempre cria um novo objeto na memória, em vez de modificar os originais.

```python
# Concatenação de Tuplas
tupla1 = (1, 2)
tupla2 = (3, 4)
nova_tupla = tupla1 + tupla2
print(nova_tupla)  # Saída: (1, 2, 3, 4)

# Concatenação de Listas
lista1 = [1, 2]
lista2 = [3, 4]
nova_lista = lista1 + lista2
print(nova_lista)  # Saída: [1, 2, 3, 4]
```

O operador `+`, quando aplicado a tuplas ou listas, cria uma nova sequência contendo todos os elementos do primeiro operando, seguidos por todos os elementos do segundo. No exemplo da tupla, `nova_tupla` é uma tupla completamente nova, e as `tupla1` e `tupla2` originais permanecem inalteradas. Isso é consistente com a imutabilidade das tuplas. Para listas, embora sejam mutáveis, a concatenação com `+` também resulta em uma nova lista, sendo uma operação distinta de métodos que modificam a lista no local (in-place), como o `list.extend()`.























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