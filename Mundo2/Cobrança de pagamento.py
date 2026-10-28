
# Calculadora de Pagamento
# Este programa calcula o preço conforme o método de pagamento
# e a quantidade de parcelas informada.

# Solicita o preço do produto e trata possíveis erros de conversão
try:
    preco = float(input("Digite o valor do produto: "))
except ValueError:
    print("Digite apenas números!")
    raise SystemExit

# Solicita o método de pagamento
metodo = input("Qual o método de pagamento? ").strip().lower()

# Solicita a quantidade de parcelas
try:
    parcela = int(input("Quantas parcelas? "))
except ValueError:
    print("Digite um número válido de parcelas!")
    raise SystemExit

# Aplica 10% de desconto para cheque ou dinheiro
if metodo in ("cheque", "dinheiro"):
    novo_preco = preco - (preco * 0.10)
    print("Você vai pagar R$ {:.2f}".format(novo_preco))

# Aplica 5% de desconto para pagamento no cartão à vista
elif metodo in ("cartão", "cartao"):
    novo_preco = preco - (preco * 0.05)
    print("Você vai pagar R$ {:.2f}".format(novo_preco))

# Mantém o preço original para pagamento em duas vezes
elif metodo in ("2x no cartão", "2x", "duas vezes"):
    print("Você irá pagar R$ {:.2f}".format(preco))

# Aplica 20% de acréscimo para pagamentos em três parcelas ou mais
elif metodo in ("cartão", "cartao") and parcela >= 3:
    novo_preco = preco + (preco * 0.20)
    print("Você pagará R$ {:.2f}".format(novo_preco))

else:
    print("Digite um método de pagamento válido!")
