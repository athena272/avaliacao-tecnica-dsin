A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Condicao com base no enunciado do material
if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0 and D > 0) and (A % 2 == 0):
    print("\nValores aceitos")
else:
    print("\nValores não aceitos")
