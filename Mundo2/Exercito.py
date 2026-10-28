
# Verificador de Alistamento Militar
# Este programa calcula a idade do usuário e informa
# quanto falta para completar 18 anos ou há quanto tempo
# essa idade foi ultrapassada.

# Solicita o ano de nascimento
ano_de_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade usando 2026 como ano de referência
idade = 2026 - ano_de_nascimento

# Verifica se o usuário ainda não completou 18 anos
if idade < 18:
    print("Você ainda vai se alistar, faltam", 18 - idade, "anos.")

# Verifica se o usuário tem exatamente 18 anos
elif idade == 18:
    print("É hora de se alistar, guerreiro!")

# Caso tenha mais de 18 anos, calcula a diferença
else:
    print(
        "Já passou seu tempo de alistamento, já passaram",
        idade - 18,
        "anos da hora de se alistar"
    )
