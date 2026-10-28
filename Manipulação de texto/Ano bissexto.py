
# Verificador de Ano Bissexto
# Este programa verifica se um ano é bissexto.

# Solicita o ano ao usuário
ano = int(input("Qual ano você quer verificar se é bissexto? "))

# Verifica se o ano é divisível por 4
if ano % 4 == 0:

    # Verifica se o ano é divisível por 100
    if ano % 100 == 0:

        # Anos divisíveis por 400 são bissextos
        if ano % 400 == 0:
            print("Esse ano é bissexto.")
        else:
            print("Esse ano não é bissexto.")

    else:
        # Se for divisível por 4, mas não por 100, é bissexto
        print("Esse ano é bissexto.")

else:
    # Se não for divisível por 4, não é bissexto
    print("Esse ano não é bissexto.")
