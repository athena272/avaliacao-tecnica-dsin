# Aqui estou chamando um lib para trabalhar com expressoes regulares
import re 

# Função para validar e identificar o padrão da placa
def validar_e_converter_placa(placa):
    # Validação para formato Brasil (AAA9999)
    padrao_brasil = r"^[A-Z]{3}[0-9]{4}$"
    # Validação para formato Mercosul (AAA9A99)
    padrao_mercosul = r"^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$"

    # Dicionário de conversão entre os padrões Brasil e Mercosul
    tabela_conversao = {
        "0": "A", "1": "B", "2": "C", "3": "D", "4": "E",
        "5": "F", "6": "G", "7": "H", "8": "I", "9": "J",
        "A": "0", "B": "1", "C": "2", "D": "3", "E": "4",
        "F": "5", "G": "6", "H": "7", "I": "8", "J": "9"
    }

    # Verifica o padrão da placa
    if re.match(padrao_brasil, placa):
        # Placa no formato Brasil, converte para Mercosul
        padrao = "Brasil"
        # Realiza a conversão
        correspondente = (
            placa[:4]  # Primeiros 4 caracteres mantidos
            + tabela_conversao[placa[4]]  # Converte o 5º caractere
            + placa[5:]  # Mantém o restante
        )
    elif re.match(padrao_mercosul, placa):
        # Placa no formato Mercosul, converte para Brasil
        padrao = "Mercosul"
        # Realiza a conversão
        correspondente = (
            placa[:4]  # Primeiros 4 caracteres mantidos
            + tabela_conversao[placa[4]]  # Converte o 5º caractere
            + placa[5:]  # Mantém o restante
        )
    else:
        # Placa não é válida
        return "Formato inválido"

    # Retorna o padrão identificado e a correspondente no outro formato
    return f"Padrão: {padrao}\nCorrespondente: {correspondente}"


placa = input("Digite a placa (formato AAA9999 ou AAA9A99): ").strip().upper()

resultado = validar_e_converter_placa(placa)
print("\n" + resultado)
