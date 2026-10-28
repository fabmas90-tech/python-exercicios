
# Analisador de Nome
# Este programa recebe um nome e apresenta informações
# sobre suas letras e sua quantidade de caracteres.

# Solicita o nome completo ao usuário
frase = input("Qual o seu nome: ")

# Exibe o nome em letras maiúsculas
print(frase.upper())

# Exibe o nome em letras minúsculas
print(frase.lower())

# Conta os caracteres sem considerar os espaços
print(len(frase.replace(" ", "")))

# Divide o texto em palavras e conta as letras da primeira
print(len(frase.split()[0]))
