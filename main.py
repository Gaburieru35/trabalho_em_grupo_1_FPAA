from labirinto import validar_labirinto
from a_estrela import a_estrela

labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1]
]

inicio, fim = validar_labirinto(labirinto)
caminho = a_estrela(labirinto, inicio, fim)

if caminho:
    print("Menor caminho (em coordenadas):")
    print(caminho)

    for i, j in caminho[1:-1]:  # não marca S e E
        labirinto[i][j] = '*'

    print("\nLabirinto com o caminho destacado:")
    for linha in labirinto:
        print(' '.join(str(c) for c in linha))
else:
    print("Sem solução possível para esse labirinto.")