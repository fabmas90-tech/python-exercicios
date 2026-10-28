
# Calculadora de Aumento Salarial
# Aplica um aumento conforme o salário informado:
# 15% para salários acima ou iguais a R$ 1.250
# 10% para salários abaixo de R$ 1.250.

# Recebe o salário como texto para permitir vírgula e ponto
salario_texto = input("Informe seu salário: ")

# Remove o separador de milhar e ajusta o separador decimal
salario_formatado = salario_texto.replace(".", "").replace(",", ".")

# Converte o salário para número decimal
salario = float(salario_formatado)

# Aplica 15% de aumento para salários a partir de R$ 1.250
if salario >= 1250:
    salario = salario + (salario * 0.15)
    print("Será adicionado 15% ao seu salário. Seu novo salário é {:.2f}".format(salario))

# Aplica 10% de aumento para salários abaixo de R$ 1.250
elif salario < 1250:
    salario = salario + (salario * 0.10)
    print("Será adicionado 10% ao seu salário. Seu novo salário é {:.2f}".format(salario))
