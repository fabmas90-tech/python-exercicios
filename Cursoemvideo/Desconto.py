
# Calculadora de Desconto
# Este programa calcula o preço de um produto com 5% de desconto.

# Solicita ao usuário o preço do produto
preco = float(input("Digite o preço do produto: "))

# Calcula o desconto de 5% e subtrai do preço original
desconto = preco - (preco * 0.05)

# Exibe o preço final com desconto
print("O preço com desconto de 5% é: R$ {:.2f}".format(desconto))
