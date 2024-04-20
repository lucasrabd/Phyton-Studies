# Solicita ao usuário que insira um número e converte para inteiro
numero = int(input("Digite um número: "))

# Loop while para imprimir números até atingir ou ultrapassar 10011
while numero < 10011:
    # Imprime o número com um tabulação à frente
    print("\t" + str(numero))

    # Incrementa o número em 1 para a próxima iteração
    numero = numero + 1

# Mensagem de conclusão do laço
print("Laço encerrado.....")
