
# Sorteador de Alunos
# Este programa recebe quatro nomes e escolhe aleatoriamente
# um deles para participar de uma atividade.

# Importa o módulo random para realizar o sorteio
import random

# Solicita os nomes dos quatro participantes
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")

# Armazena os nomes em uma lista
nomes = [nome1, nome2, nome3, nome4]

# Escolhe aleatoriamente um nome da lista
sorteado = random.choice(nomes)

# Exibe o nome do aluno escolhido
print("O aluno escolhido foi {}".format(sorteado))
