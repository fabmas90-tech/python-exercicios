# Simulador de Radar
# Este programa gera uma velocidade aleatória e verifica
# se o veículo será multado conforme o limite definido.

# Importa a função para gerar números inteiros aleatórios
from random import randint

# Sorteia uma velocidade entre 1 e 100 km/h
radar = randint(1, 100)

# Calcula a multa fictícia com base no excesso de 80 km/h
multa = (radar - 80) * 7

# Exibe a velocidade sorteada
print(radar)

# Verifica se a velocidade atingiu ou ultrapassou 80 km/h
if radar >= 80:
    print("Você foi multado!")
    print("Você deve pagar:", multa, "R$")

# Se a velocidade for inferior a 80 km/h, não há multa
elif radar < 80:
    print("Ok, nada aconteceu!")
