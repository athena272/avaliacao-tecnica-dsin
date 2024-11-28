def gerar_matriz_caracol(N):
    # Inicializa uma matriz N x N preenchida com zeros
    matriz = [[0] * N for _ in range(N)]
    
    # Define as variáveis de controle
    numero = 1  # Primeiro número a ser preenchido
    inicio_linha, fim_linha = 0, N - 1
    inicio_coluna, fim_coluna = 0, N - 1
    
    # Preenche a matriz em formato de espiral
    while inicio_linha <= fim_linha and inicio_coluna <= fim_coluna:
        # Preenche da esquerda para a direita
        for coluna in range(inicio_coluna, fim_coluna + 1):
            matriz[inicio_linha][coluna] = numero
            numero += 2
        inicio_linha += 1  # Move para a próxima linha

        # Preenche de cima para baixo
        for linha in range(inicio_linha, fim_linha + 1):
            matriz[linha][fim_coluna] = numero
            numero += 2
        fim_coluna -= 1  # Move para a coluna anterior

        # Preenche da direita para a esquerda
        if inicio_linha <= fim_linha:
            for coluna in range(fim_coluna, inicio_coluna - 1, -1):
                matriz[fim_linha][coluna] = numero
                numero += 2
            fim_linha -= 1  # Move para a linha anterior

        # Preenche de baixo para cima
        if inicio_coluna <= fim_coluna:
            for linha in range(fim_linha, inicio_linha - 1, -1):
                matriz[linha][inicio_coluna] = numero
                numero += 2
            inicio_coluna += 1  # Move para a próxima coluna

    return matriz


# Função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{num:2}" for num in linha))

try:
    N = int(input("Digite o tamanho da matriz quadrada (N): "))
    if N <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        matriz_caracol = gerar_matriz_caracol(N)
        exibir_matriz(matriz_caracol)
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro positivo.")
