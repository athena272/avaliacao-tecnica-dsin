descricao = input("Digite a descrição do item: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário do item: "))

total_sem_desconto = quantidade * preco_unitario

# Aqui estou determinando qual é porcentagem que vai ser usada como desconto
if quantidade <= 5:
    porcentagem_desconto = 5.55
elif quantidade <= 10:
    porcentagem_desconto = 8.0
else:
    porcentagem_desconto = 12.5

valor_desconto = total_sem_desconto * (porcentagem_desconto / 100)

# Valor final que vai ser pago
total_a_pagar = total_sem_desconto - valor_desconto

print(f"\nItem: {descricao}")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Total sem Desconto: R$ {total_sem_desconto:.2f}")
print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
