import heapq

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_estrela(matriz, inicio, fim):
    linhas, colunas = len(matriz), len(matriz[0])
    fila = [(0, inicio)]
    veio_de = {}
    custo_ateagora = {inicio: 0}

    while fila:
        , atual = heapq.heappop(fila)

        if atual == fim:
            caminho = []
            while atual != inicio:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vizinho = (atual[0] + dx, atual[1] + dy)
            x, y = vizinho
            if 0 <= x < linhas and 0 <= y < colunas and matriz[x][y] != 1:
                novo_custo = custo_ate_agora[atual] + 1
                if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:
                    custo_ate_agora[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, fim)
                    heapq.heappush(fila, (prioridade, vizinho))
                    veio_de[vizinho] = atual
    return None
