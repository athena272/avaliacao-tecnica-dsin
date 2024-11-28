horas_por_dia = float(input("Digite a quantidade de horas trabalhadas por dia: "))
preco_por_hora = float(input("Digite o preço da hora trabalhada: "))
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês: "))

salario_bruto = horas_por_dia * preco_por_hora * dias_trabalhados

# Aplicando o desconto de 21%
desconto = salario_bruto * 0.21

# E agora temos o salario liquido
salario_liquido = salario_bruto - desconto

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto (21%): R$ {desconto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
