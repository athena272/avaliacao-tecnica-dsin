# Função para verificar se um número é perfeito
def eh_perfeito(num):
    soma_divisores = sum(i for i in range(1, num) if num % i == 0)
    return soma_divisores == num

# Função para verificar se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Função principal
def gerar_sequencia(N):
    if N <= 0:
        print("Por favor, insira um número inteiro positivo.")
        return

    for num in range(1, N + 1):
        print(f"\nNúmero: {num}")
        if eh_perfeito(num):
            print("numero perfeito")
        if num % 2 == 0:
            print("multiplo de 2")
        if num % 7 == 0:
            print("multiplo de 7")
        if eh_primo(num):
            print("numero primo")

try:
    N = int(input("Digite um número inteiro positivo (N): "))
    gerar_sequencia(N)
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
