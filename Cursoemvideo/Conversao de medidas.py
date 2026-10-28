
# Conversor de Metros para Centímetros e Milímetros
# Recebe uma medida em metros e calcula suas equivalências.

# Solicita ao usuário uma metragem
metro = int(input("Digite uma metragem: "))

# Exibe a conversão para centímetros e milímetros
print("{} metro(s), em centímetros é {} e em milímetros é {}".format(
    metro, metro * 100, metro * 1000
))
