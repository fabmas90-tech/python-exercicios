
# Calculadora de Aumento Salarial
# Este programa calcula o novo salário de um funcionário
# após a aplicação de um aumento de 15%.

# Solicita o salário atual do funcionário
salario = float(input("Digite seu salário: "))

# Calcula o novo salário com o aumento de 15%
novo_salario = salario * 1.15

# Exibe o novo salário com duas casas decimais
print("Seu novo salário com aumento de 15% é R$ {:.2f}".format(novo_salario))
