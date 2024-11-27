A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A == 0 and B == 0 and C != 1:
    print("\nSolução impossível")
else:
    denominador = A + B
    numerador = 1 - C

    if denominador == 0:
        # Caso de divisao por 0 sendo tratada aqui embaixo
        if numerador == 0:
            print("\nA equação possui infinitas soluções (X indeterminado).")
        else:
            print("\nSolução impossível")
    else:
        X = numerador / denominador
        print(f"\nO valor de X é: {X}")
