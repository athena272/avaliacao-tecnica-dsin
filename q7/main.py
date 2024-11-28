def imprimir_titulo(titulo_superior, titulo_inferior):
    largura_total = 50  # Largura total da moldura
    char_lateral = "||"  # Borda lateral dupla
    char_superior_inferior = "|"  # Borda superior/inferior
    
    # Calcula a largura do texto e centraliza
    titulo_superior_centralizado = titulo_superior.center(largura_total - 4)
    titulo_inferior_centralizado = titulo_inferior.center(largura_total - 4)
    
    # Imprime o título formatado
    print(char_superior_inferior * largura_total)  # Linha superior
    print(f"{char_lateral}{' ' * (largura_total - 4)}{char_lateral}")  # Linha vazia
    print(f"{char_lateral}{titulo_superior_centralizado}{char_lateral}")  # Título superior
    print(f"{char_lateral}{titulo_inferior_centralizado}{char_lateral}")  # Título inferior
    print(f"{char_lateral}{' ' * (largura_total - 4)}{char_lateral}")  # Linha vazia
    print(char_superior_inferior * largura_total)  # Linha inferior


titulo_superior = input("Digite o título superior: ")
titulo_inferior = input("Digite o título inferior: ")

imprimir_titulo(titulo_superior, titulo_inferior)
