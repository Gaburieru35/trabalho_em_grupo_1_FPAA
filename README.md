# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

## 👥 Equipe
- Gabriel Henrique Mota Rodrigues - RA1450612

- Matheus Vinicius Mota Rodrigues - RA1462287

- José Miguel Quintão Magalhães - RA1396023

## 📘 Descrição do Projeto

O **PathFinder** é um projeto desenvolvido para encontrar o menor caminho entre dois pontos em um labirinto 2D utilizando o algoritmo **A\***. A aplicação simula o movimento de um robô de resgate, que deve sair de um ponto inicial (S) e chegar a um ponto final (E), desviando de obstáculos e otimizando sua rota.

## 🎯 Objetivo

- Implementar o algoritmo A* para resolver um labirinto 2D.
- Evitar obstáculos e considerar o custo de movimentação.
- Exibir o menor caminho encontrado, se houver, ou informar que não há solução possível.

## 🧠 Algoritmo A* (A-Star)

O **A\*** é um algoritmo de busca heurística que combina:

- `g(n)`: o custo do caminho já percorrido até o nó `n`.
- `h(n)`: uma estimativa do custo até o objetivo, calculada usando **distância de Manhattan**:

h(n) = |x_atual - x_final| + |y_atual - y_final|

A função total de custo é:

f(n) = g(n) + h(n)

O algoritmo explora os caminhos com menor valor de `f(n)` até encontrar o objetivo.

## 🧱 Regras do Labirinto

- O labirinto é uma matriz 2D com:
  - `0`: célula livre
  - `1`: obstáculo
  - `S`: início (start)
  - `E`: fim (end)

- O robô pode se mover em 4 direções: cima, baixo, esquerda e direita.
- Custo de cada movimento é igual a 1.
- O algoritmo deve detectar se `S` e `E` existem e lidar com labirintos sem solução.

## 🖥️ Exemplo de Entrada

```python
labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1]
]
```

## ✅ Saída Esperada

Menor caminho (em coordenadas):
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com o caminho destacado:
```python
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```


## 🚀 Como Executar

Clone o repositório:
```bash
    git clone https://github.com/seuusuario/pathfinder-a-star.git
    cd pathfinder-a-star
```

Execute o código:

```bash
python pathfinder.py
```
Você pode editar a matriz diretamente no arquivo pathfinder.py para testar diferentes labirintos.

## ⚠️ Requisitos

Python 3.6 ou superior