
# Calculadora de IMC
# Este programa calcula o Índice de Massa Corporal (IMC)
# com base no peso e na altura informados pelo usuário.

# Solicita o peso em quilogramas
peso = float(input("Qual é o seu peso? "))

# Solicita a altura em metros
altura = float(input("Qual é sua altura? "))

# Calcula o IMC dividindo o peso pela altura ao quadrado
imc = peso / (altura ** 2)

# Classifica o resultado conforme as faixas do programa
if imc < 18.5:
    print("Você está abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Você está no seu peso ideal")

elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso")

elif imc >= 30 and imc <= 40:
    print("Você está com obesidade")

else:
    print("Você está com obesidade mórbida")
