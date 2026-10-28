
# Contagem Regressiva para o Ano-Novo
# Este programa realiza uma contagem regressiva de 10 até 1
# e exibe uma mensagem de feliz ano-novo ao terminar.

# Importa o módulo time para criar pausas
import time

# Percorre os números de 10 até 1, em ordem decrescente
for c in range(10, 0, -1):

    # Exibe o número atual da contagem
    print(c)

    # Aguarda um segundo antes de continuar
    time.sleep(1)

# Exibe a mensagem após o fim da contagem
print("Feliz ano novo!")
