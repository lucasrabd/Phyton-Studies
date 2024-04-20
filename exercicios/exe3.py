# Solicita ao usuário que insira um número e converte para inteiro
n = int(input('Digite um número: '))

# Imprime a mensagem indicando qual é a tabuada que será exibida
print('A tabuada do número é:', n)

# Inicializa o contador de multiplicação
multiplicacao = 1

# Loop para calcular e imprimir a tabuada do número fornecido
while multiplicacao <= 10:
    # Imprime a multiplicação atual da tabuada
    print(n, 'x', multiplicacao, '=', n * multiplicacao)
    
    # Incrementa o contador de multiplicação para a próxima iteração
    multiplicacao += 1
