
# Classificador de Triângulos
# Este programa recebe três medidas e identifica
# se o triângulo é equilátero, isósceles ou escaleno.

# Solicita as medidas dos três lados
ladoa = float(input("Digite a primeira reta: "))
ladob = float(input("Digite a segunda reta: "))
ladoc = float(input("Digite a terceira reta: "))

# Verifica se todos os lados possuem a mesma medida
if ladoa == ladob and ladoa == ladoc:
    print("É um triângulo equilátero")

# Verifica se pelo menos dois lados possuem a mesma medida
elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print("É um triângulo isósceles")

# Se todos os lados forem diferentes, classifica como escaleno
else:
    print("É um triângulo escaleno")
