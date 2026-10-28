
# Simulador de Financiamento Imobiliário
# Este programa avalia uma solicitação de financiamento
# conforme o salário, o prazo e o valor da casa.

# Solicita o valor do imóvel
casa = float(input("Qual o valor da casa? R$ "))

# Solicita o salário atual
salario = float(input("Qual seu salário atual? R$ "))

# Solicita o prazo de pagamento em anos
anos = int(input("Em quantos anos você quer pagar? "))

# Calcula o limite de prestação mensal permitido pelo programa
prestacao = salario * 0.30

# Converte o prazo de anos para meses
meses = anos * 12

# Calcula o total que seria pago usando essa prestação mensal
valor_total = prestacao * meses

# Verifica se o total calculado cobre o valor da casa
if valor_total > casa:
    print("Empréstimo aprovado!")

elif valor_total == casa:
    print("Empréstimo aprovado!")

else:
    print("Empréstimo negado!")
