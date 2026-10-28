
# Verificador de Triângulo
# Este programa recebe três medidas e verifica se elas
# podem formar um triângulo.

# Solicita as medidas das três retas
retaa = int(input("Digite a primeira reta: "))
retab = int(input("Digite a segunda reta: "))
retac = int(input("Digite a terceira reta: "))

# Verifica as condições para formar um triângulo
if retaa + retab > retac and retaa + retac > retab and retab + retac > retaa:
    print("Pode fazer um triângulo")
else:
    print("Não pode fazer um triângulo")
