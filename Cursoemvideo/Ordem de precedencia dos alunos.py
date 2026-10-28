
# Sorteador de Ordem de Apresentação
# Este programa recebe os nomes de quatro alunos e sorteia
# uma ordem aleatória para as apresentações.

# Importa o módulo random para trabalhar com sorteios
import random

# Solicita os nomes dos quatro alunos
aluno1 = input("Digite o primeiro aluno: ")
aluno2 = input("Digite o segundo aluno: ")
aluno3 = input("Digite o terceiro aluno: ")
aluno4 = input("Digite o quarto aluno: ")

# Armazena os nomes em uma lista
lista = [aluno1, aluno2, aluno3, aluno4]

# Embaralha os alunos em uma ordem aleatória
random.shuffle(lista)

# Exibe a ordem sorteada
print("A ordem sorteada é:")
print(lista)
