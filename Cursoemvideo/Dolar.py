
# Conversor de Reais para Dólares
# Este programa calcula quantos dólares podem ser comprados
# com uma quantia em reais, considerando a cotação de R$ 3,27.

# Solicita ao usuário uma quantia em reais
reais = int(input("Digite sua renda em reais: "))

# Converte reais para dólares usando a cotação informada
dolares = reais / 3.27

# Exibe o resultado com duas casas decimais
print("Você pode comprar {:.2f} dólares".format(dolares))
