
# Sistema de Monitoramento de Velocidade
# Simula um radar que verifica a velocidade de um veículo
# e calcula uma multa fictícia quando o limite é ultrapassado.

# Importa o módulo time para criar pausas
import time

# Exibe o cabeçalho do sistema
print("=" * 50)
print("     SISTEMA DE MONITORAMENTO ELETRÔNICO")
print("=" * 50)

# Simula o carregamento do sistema
time.sleep(5)

print("\nIniciando sistema...")
time.sleep(1)

print("Verificando sensores de velocidade...")
time.sleep(1)

print("Sistema iniciado com sucesso!")

# Define as configurações do radar
LIMITE_DE_VELOCIDADE = 80
VALOR_POR_KM = 7.00

# Exibe as informações do radar
print("\n" + "-" * 50)
print("INFORMAÇÕES DO RADAR")
print("-" * 50)

# Solicita a velocidade registrada
velocidade = float(input("\nDigite a velocidade registrada pelo radar: "))

# Simula o processamento das informações
print("\nProcessando informações...")
time.sleep(2)

# Verifica se a velocidade ultrapassou o limite
if velocidade > LIMITE_DE_VELOCIDADE:

    # Calcula o excesso de velocidade
    excesso_velocidade = velocidade - LIMITE_DE_VELOCIDADE

    # Calcula a multa fictícia por quilômetro excedido
    valor_multa = excesso_velocidade * VALOR_POR_KM

    # Exibe o resultado da infração
    print("\n" + "=" * 50)
    print("⚠️ VELOCIDADE ACIMA DO LIMITE DETECTADA!")
    print("=" * 50)

    print("\nVelocidade registrada: {:.1f} km/h".format(velocidade))
    print("Limite permitido: {} km/h".format(LIMITE_DE_VELOCIDADE))
    print("Excesso de velocidade: {:.1f} km/h".format(excesso_velocidade))
    print("Valor por km excedido: R${:.2f}".format(VALOR_POR_KM))
    print("-" * 50)
    print("VALOR TOTAL DA MULTA: R${:.2f}".format(valor_multa))

    print("\nSituação: MULTADO ❌")

else:
    # Calcula quanto falta para atingir o limite
    diferenca = LIMITE_DE_VELOCIDADE - velocidade

    # Exibe o resultado para velocidades dentro do limite
    print("\n" + "=" * 50)
    print("VELOCIDADE DENTRO DO LIMITE PERMITIDO!")
    print("=" * 50)

    print("\nVelocidade registrada: {:.1f} km/h".format(velocidade))
    print("Limite permitido: {} km/h".format(LIMITE_DE_VELOCIDADE))
    print("Margem restante: {:.1f} km/h".format(diferenca))

    print("\nSituação: VELOCIDADE PERMITIDA ✅")

# Exibe a mensagem de encerramento
print("\n" + "=" * 50)
print("RELATÓRIO FINALIZADO COM SUCESSO")
print("=" * 50)

print("\nTenha um bom dia e dirija com segurança! 🚗")
