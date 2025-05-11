def encontrar_pontos_inicio_fim(matriz):
    inicio = fim = None
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 'S':
                inicio = (i, j)
            elif matriz[i][j] == 'E':
                fim = (i, j)
    return inicio, fim

def validar_labirinto(matriz):
    inicio, fim = encontrar_pontos_inicio_fim(matriz)
    if not inicio or not fim:
        raise ValueError("O labirinto deve conter um ponto inicial 'S' e final 'E'")
    return inicio, fim
