
# Calculadora de Raiz Quadrada
# Este programa calcula a raiz quadrada de um número inteiro
# e arredonda o resultado para baixo, obtendo um número inteiro.

# Importa sqrt para calcular a raiz quadrada e floor para arredondar para baixo
from math import sqrt, floor

# Solicita um número ao usuário
num = int(input("Digite seu número: "))

# Calcula a raiz quadrada do número informado
raiz = sqrt(num)

# Exibe a raiz quadrada arredondada para baixo
print("A raiz quadrada de {} é igual a {}".format(num, floor(raiz)))
