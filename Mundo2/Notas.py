
# Calculadora de Média Escolar
# Este programa calcula a média de duas notas e informa
# se o aluno foi aprovado, está de recuperação ou foi reprovado.

# Solicita a primeira nota
nota = float(input("Digite a primeira nota: "))

# Solicita a segunda nota
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média aritmética das duas notas
media = (nota + nota2) / 2

# Verifica se o aluno foi aprovado
if media >= 7:
    print("Parabéns, você foi aprovado :)")

# Verifica se a média está entre 5 e 6,9
elif media >= 5 and media < 7:
    print("Você está de recuperação!")

# Se a média for menor que 5, o aluno está reprovado
else:
    print("Você está reprovado!")
