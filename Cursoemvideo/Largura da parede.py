
# Calculadora de Área e Quantidade de Tinta
# Este programa calcula a área de uma parede e estima quantos litros
# de tinta são necessários, considerando que 1 litro pinta 2 m².

# Solicita a largura da parede em metros
largura = float(input("Digite a largura da parede: "))

# Solicita a altura da parede em metros
altura = float(input("Digite a altura da parede: "))

# Calcula a área da parede em metros quadrados
area = largura * altura

# Calcula a quantidade de tinta necessária em litros
tinta = area / 2

# Exibe a área calculada e a quantidade estimada de tinta
print("A área da parede é {:.2f} m², e a quantidade de tinta necessária é {:.2f} L".format(area, tinta))
