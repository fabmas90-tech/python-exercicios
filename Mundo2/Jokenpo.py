
# Jokenpô: Pedra, Papel e Tesoura
# Este programa permite que o usuário jogue contra o computador,
# que escolhe uma opção aleatoriamente.

# Importa o módulo random para realizar a escolha do computador
import random

# Define as opções possíveis do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Solicita a escolha do jogador e converte para letras minúsculas
jogador = input("Pedra, papel ou tesoura? ").lower()

# Sorteia a jogada do computador
computador = random.choice(opcoes)

# Exibe a escolha do computador
print("O computador escolheu: {}".format(computador))

# Verifica se houve empate
if jogador == computador:
    print("Empate!")

# Pedra vence tesoura
elif jogador == "pedra" and computador == "tesoura":
    print("Você ganhou!")

# Papel vence pedra
elif jogador == "papel" and computador == "pedra":
    print("Você ganhou!")

# Tesoura vence papel
elif jogador == "tesoura" and computador == "papel":
    print("Você ganhou!")

# Verifica se o jogador digitou uma opção inválida
elif jogador not in opcoes:
    print("Opção inválida!")

# Se não houve empate, vitória ou erro, o computador venceu
else:
    print("Você perdeu!")
