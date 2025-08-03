# Estrutura de Dados em Python

## Sumário

1. [Tipos de Dados Agregados](#tipos-de-dados-agregados)
   - [Listas](#listas)
     - [Métodos para Listas](#métodos-para-listas)
     - [Adicionar Elementos](#adicionar-elementos)
     - [Remover Elementos](#remover-elementos)
     - [Ordenar Elementos](#ordenar-elementos)
   - [Tuplas](#tuplas)
     - [Métodos para Tuplas](#métodos-para-tuplas)
   - [Operações em Listas e Tuplas](#operações-em-listas-e-tuplas)
     - [Acesso por Índice](#acesso-por-índice)
     - [Slicing (Fatiamento)](#slicing-fatiamento)
     - [Operador `in`](#operador-in)
     - [Iteração sobre Elementos](#iteração-sobre-elementos)
     - [Desempacotamento de Sequências](#desempacotamento-de-sequências)
     - [Concatenação de Tuplas e Listas](#concatenação-de-tuplas-e-listas)
2. [Conjuntos (Sets)](#conjuntos-sets)
   - [Conjunto Vazio](#conjunto-vazio)
   - [Verificando a Existência de um Elemento](#verificando-a-existência-de-um-elemento)
   - [Métodos de Manipulação](#métodos-de-manipulação)
   - [Operações entre Conjuntos](#operações-entre-conjuntos)
   - [Outros Métodos e Funções](#outros-métodos-e-funções)
3. [Dicionários](#dicionários)
   - [Dicionário Vazio](#dicionário-vazio)
   - [Criando com Lista de Tuplas](#criando-com-lista-de-tuplas)
   - [Tipos de Chaves e Valores](#tipos-de-chaves-e-valores)
   - [Acessando e Modificando Dados](#acessando-e-modificando-dados)
   - [Verificando a Existência de uma Chave](#verificando-a-existência-de-uma-chave)
   - [Métodos de Dicionários](#métodos-de-dicionários)
     - [Métodos de Visualização e Contagem](#métodos-de-visualização-e-contagem)
     - [Métodos de Busca e Remoção](#métodos-de-busca-e-remoção)
     - [Outros Métodos de Manipulação](#outros-métodos-de-manipulação)
   - [Exemplo Prático: Dicionários e Conjuntos](#exemplo-prático-dicionários-e-conjuntos)
4. [Estruturas de Dados Avançadas](#estruturas-de-dados-avançadas)

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

O operador `+`, quando aplicado a tuplas ou listas, cria uma nova sequência contendo todos os elementos do primeiro operando, seguidos por todos os elementos do segundo. 

No exemplo da tupla, `nova_tupla` é uma tupla completamente nova, e as `tupla1` e `tupla2` originais permanecem inalteradas. Isso é consistente com a imutabilidade das tuplas. Para listas, embora sejam mutáveis, a concatenação com `+` também resulta em uma nova lista, sendo uma operação distinta de métodos que modificam a lista no local (in-place), como o `list.extend()`.




___

<br>
<br>
<br>
<br>
<br>

___


## Conjuntos (Sets)

Um conjunto é uma coleção não ordenada de elementos, sem elementos repetidos.

Formas de criar um Conjunto:

* Chaves `{ }`

```python
conjunto1 = {'a', 'b', 'c'}
```

* Função `set( )`
```python
conjunto2 = set([3, 4, 5, 6])
```

### Conjunto Vazio

Para criar um conjunto vazio, **sempre**** use `set()` sem argumentos. Chaves vazias (`{}`) criam um dicionário, não um conjunto.

```python
conjunto_vazio = set()
print(type(conjunto_vazio)) # <class 'set'>
```

### Verificando a Existência de um Elemento

Para verificar se um item pertence a um conjunto, utilize os operadores `in` e `not in`.

  * **Contexto:** `conjunto = {1, 2, 3, 4, 5}`

| Operador | Conceito                                                                                                  | Exemplo                 | Saída |
| :------- | :-------------------------------------------------------------------------------------------------------- | :---------------------- | :---- |
| `in`     | Retorna `True` se o elemento estiver presente no conjunto e `False` caso contrário.                       | `print(3 in conjunto)`  | True  |
| `not in` | Retorna `True` se o elemento **não** estiver presente no conjunto e `False` caso contrário.                 | `print(6 not in conjunto)` | True  |

-----

### Métodos de Manipulação

Conjuntos possuem diversos métodos para adicionar e remover elementos.

  * **Contexto:** `conjunto = {1, 2, 3}`

| Método             | Conceito                                                | Exemplo                  | Conjunto Resultante |
| :----------------- | :------------------------------------------------------ | :----------------------- | :------------------ |
| `add(elemento)`    | Adiciona um único elemento.                             | `conjunto.add(4)`        | `{1, 2, 3, 4}`      |
| `update(iterável)` | Adiciona múltiplos elementos de um iterável.            | `conjunto.update([5, 6])`  | `{1, 2, 3, 5, 6}`   |
| `remove(elemento)` | Remove um item. Gera `KeyError` se o item não existir.  | `conjunto.remove(2)`     | `{1, 3}`            |
| `discard(elemento)`| Remove um item. Não gera erro se o item não existir.    | `conjunto.discard(2)`    | `{1, 3}`            |
| `pop()`            | Remove e retorna um elemento arbitrário do conjunto.    | `conjunto.pop()`         | Varia, ex: `{2, 3}` |
| `clear()`          | Remove todos os elementos do conjunto.                  | `conjunto.clear()`       | `set()`             |

-----

### Operações entre Conjuntos

Existem diversos métodos e operadores para realizar operações matemáticas entre conjuntos.

  * **Contexto:** `a = {1, 2, 3}` e `b = {3, 4, 5}`

| Método                               | Operador | Conceito                                                                 | Exemplo                        | Saída       |
| :----------------------------------- | :------- | :----------------------------------------------------------------------- | :----------------------------- | :---------- |
| `union(set2)`                        | `\|`     | **União**: Retorna um conjunto com todos os elementos de ambos.            | `a.union(b)`                   | `{1, 2, 3, 4, 5}` |
| `intersection(set2)`                 | `&`      | **Interseção**: Retorna um conjunto com os elementos comuns a ambos.       | `a.intersection(b)`            | `{3}`       |
| `difference(set2)`                   | `-`      | **Diferença**: Retorna os elementos que estão no primeiro conjunto, mas não no segundo. | `a.difference(b)`              | `{1, 2}`    |
| `symmetric_difference(set2)`         | `^`      | **Diferença Simétrica**: Retorna os elementos que estão em um dos conjuntos, mas não em ambos. | `a.symmetric_difference(b)`    | `{1, 2, 4, 5}`|

-----

### Outros Métodos e Funções

Métodos para verificação de relacionamento, contagem e cópia.

  * **Contexto:** `a = {1, 2}`, `b = {1, 2, 3}`, `c = {4, 5}`

| Método             | Operador | Conceito                                                                 | Exemplo               | Saída   |
| :----------------- | :------- | :----------------------------------------------------------------------- | :-------------------- | :------ |
| `issubset(set2)`   | `<=`     | Verifica se um conjunto é **subconjunto** de outro.                      | `a.issubset(b)`       | `True`  |
| `issuperset(set2)` | `>=`     | Verifica se um conjunto é **superconjunto** de outro.                    | `b.issuperset(a)`     | `True`  |
| `isdisjoint(set2)` |          | Verifica se os conjuntos não têm elementos em comum (são disjuntos).     | `a.isdisjoint(c)`     | `True`  |
| `len(conjunto)`    |          | Retorna a quantidade de elementos de um conjunto.                        | `len(a)`              | `2`     |
| `copy()`           |          | Retorna uma cópia rasa (*shallow copy*) do conjunto.                     | `copia = a.copy()`    | `{1, 2}`|


---

<br>
<br>
<br>

___



## Dicionários

Um dicionário é uma coleção de pares chave-valor, onde cada chave única mapeia para um valor. Os dicionários são mutáveis e não ordenados (embora, a partir do Python 3.7, preservem a ordem de inserção).

Formas de criar um Dicionário:

* Chaves `{ }`

```python
# inserindo pares chave-valor.
dic1 = {"nome": "Ana", "nota": 10.0}
```

* Função `dict( )`
```python
# passando pares chave-valor como argumentos nomeados.
dic2 = dict(nome="Eva", nota=9.4)
```

### Dicionário Vazio

Um dicionário vazio pode ser criado usando `{}` ou a função `dict()` sem argumentos.

```python
dicionario_vazio1 = {}
dicionario_vazio2 = dict()
```

### Criando Dicionário com Lista de Tuplas

É possível criar um dicionário a partir de um iterável de pares (como uma lista de tuplas), onde cada tupla contém uma chave e um valor.

```python
lista_de_tuplas = [("nome", "Ana"), ("nota", 10.0)]
dicionario = dict(lista_de_tuplas)

print(dicionario)
# Saída: {'nome': 'Ana', 'nota': 10.0}
```

-----

### Tipos de Chaves e Valores

#### Tipos Permitidos para Chaves

As chaves de um dicionário devem ser de um tipo de dado **imutável**.

  * **Permitido:** Strings, números (int, float), tuplas.
  * **Não permitido:** Listas, outros dicionários ou qualquer objeto mutável.

<!-- end list -->

```python
# Chaves válidas (string, inteiro, tupla)
dicionario_valido = {
    "nome": "Ana",
    1: "um",
    (2, 3): "par ordenado"
}

# Tentar usar uma lista como chave gera um erro
# dicionario_invalido = {[1, 2]: "lista"}
# TypeError: unhashable type: 'list'
```

#### Tipos Permitidos para Valores

Os valores de um dicionário podem ser de **qualquer tipo de dado**, incluindo outros dicionários, listas e objetos.

```python
dicionario = {
    "nome": "João",
    "idade": 25,
    "notas": [10.0, 6.3, 7.5],
    "endereco": {"cidade": "São Paulo", "bairro": "Centro"}
}
```

-----

### Acessando e Modificando Dados

Podemos acessar, modificar e remover itens usando a chave entre colchetes `[]`.

  * **Contexto:** `dic = {"nome": "Ana", "nota": 10.0}`

| Operação                          | Conceito                  | Exemplo                | Resultado                                |
| :-------------------------------- | :------------------------ | :--------------------- | :--------------------------------------- |
| `dicionario[chave]`               | Acessar um valor.         | `dic["nome"]`          | Retorna `"Ana"`                          |
| `dicionario[chave] = valor`       | Atribuir/modificar um valor. | `dic["nota"] = 9.2`    | `dic` se torna `{'nome': 'Ana', 'nota': 9.2}` |
| `del dicionario[chave]`           | Remover um item.          | `del dic["nome"]`      | `dic` se torna `{'nota': 9.2}`             |

### Verificando a Existência de uma Chave

Use os operadores `in` e `not in` para verificar se uma chave existe no dicionário.

  * **Contexto:** `dic = {"nome": "Ana", "nota": 10.0}`

| Operador | Conceito                                              | Exemplo                 | Saída |
| :------- | :---------------------------------------------------- | :---------------------- | :---- |
| `in`     | Retorna `True` se a chave estiver presente.           | `print("nome" in dic)`  | True  |
| `not in` | Retorna `True` se a chave **não** estiver presente. | `print("idade" not in dic)`| True |

-----

### Métodos de Dicionários

#### Métodos de Visualização e Contagem

  * **Contexto:** `dicionario = {"nome": "João", "idade": 28}`

| Método           | Conceito                                  | Exemplo             | Saída                                      |
| :--------------- | :---------------------------------------- | :------------------ | :----------------------------------------- |
| `keys()`         | Retorna uma visão das chaves.             | `dicionario.keys()` | `dict_keys(['nome', 'idade'])`             |
| `values()`       | Retorna uma visão dos valores.            | `dicionario.values()`| `dict_values(['João', 28])`                |
| `items()`        | Retorna uma visão dos pares (chave, valor).| `dicionario.items()` | `dict_items([('nome', 'João'), ('idade', 28)])` |
| `len(dicionario)`| Retorna o número de pares chave-valor.    | `len(dicionario)`   | `2`                                        |

#### Métodos de Busca e Remoção

  * **Contexto:** `dicionario = {"nome": "João", "idade": 28}`

| Método                          | Conceito                                                              | Exemplo                               | Saída/Resultado                                  |
| :------------------------------ | :-------------------------------------------------------------------- | :------------------------------------ | :----------------------------------------------- |
| `get(chave, padrão=None)`       | Obtém um valor. Retorna `padrão` (ou `None`) se a chave não existir, sem gerar erro. | `dicionario.get("altura", "N/A")` | `"N/A"`                                          |
| `pop(chave, padrão)`            | Remove uma chave e retorna seu valor. Gera `KeyError` se a chave não existir e `padrão` não for fornecido. | `dicionario.pop("idade")`               | Retorna `28` e `dicionario` se torna `{'nome': 'João'}` |
| `list(dicionario)`              | Converte as chaves do dicionário para uma lista.                      | `chaves = list(dicionario)`           | `chaves` será `['nome', 'idade']`                |
| `clear()`                       | Apaga todos os itens do dicionário.                                   | `dicionario.clear()`                  | `dicionario` se torna `{}`                       |

#### Outros Métodos de Manipulação

  * **Contexto:** `dicionario = {"a": 1, "b": 2, "c": 3}`

| Método                | Conceito                                                              | Exemplo                             | Resultado                                  |
| :-------------------- | :-------------------------------------------------------------------- | :---------------------------------- | :----------------------------------------- |
| `popitem()`           | Remove e retorna o último par (chave, valor) inserido.                 | `dicionario.popitem()`              | Retorna `('c', 3)` e `dicionario` vira `{'a': 1, 'b': 2}` |
| `reversed(dicionario)`| Retorna um iterador reverso sobre as chaves.                          | `list(reversed(dicionario))`        | `['c', 'b', 'a']`                          |
| `update([outro])`     | Atualiza o dicionário com os pares chave-valor de outro.                | `dicionario.update({"c": 4, "d": 5})` | `dicionario` vira `{'a': 1, 'b': 2, 'c': 4, 'd': 5}` |
| `copy()`              | Retorna uma cópia rasa (*shallow copy*) do dicionário.                  | `copia = dicionario.copy()`         | `copia` será `{'a': 1, 'b': 2, 'c': 3}`     |

-----

### Exemplo Prático: Dicionários e Conjuntos

É comum combinar estruturas de dados. Abaixo, um dicionário onde os valores são conjuntos.

```python
# Dicionário com conjuntos como valores
estoque = {
    "frutas": {"maçã", "uva"},
    "verduras": {"cenoura", "alface"}
}

# Adicionando um item ao conjunto de frutas
estoque["frutas"].add("morango")

# Removendo um item do conjunto de verduras
estoque["verduras"].discard("alface")

print(estoque)
# Saída: {'frutas': {'uva', 'maçã', 'morango'}, 'verduras': {'cenoura'}}
```

___

<br>
<br>
<br>
<br>
<br>

___


# Estruturas de Dados Avançadas

