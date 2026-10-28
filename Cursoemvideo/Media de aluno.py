
# Calculadora de Média Escolar
# Este programa recebe duas notas e calcula a média aritmética.

# Solicita a primeira nota do aluno
nota = int(input("Digite sua primeira nota: "))

# Solicita a segunda nota do aluno
nota2 = int(input("Digite sua segunda nota: "))

# Calcula e exibe a média das duas notas
media = (nota + nota2) / 2

print("A média é: {:.1f}".format(media))
