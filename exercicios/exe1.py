# Lista para armazenar os números fornecidos pelo usuário
numeros = []

# Solicita ao usuário que escolha a operação a ser realizada
operacao = input("Qual operacao deseja realizar? (+, -, *, /): ")

# Solicita ao usuário quantos números deseja utilizar e converte para inteiro
quantidade = int(input("Quantos números deseja utilizar? "))

# Loop para coletar os números fornecidos pelo usuário e adicioná-los à lista
for i in range(quantidade):
    numeros.append(float(input("Digite o número {}: ".format(i + 1))))

# Inicializa o resultado com o primeiro número digitado
resultado = numeros[0]

# Verifica a operação selecionada e realiza o cálculo correspondente
if operacao == "+":
    for i in range(1, quantidade):
        resultado += numeros[i]
    print("O resultado da adição é: ", resultado)
    
elif operacao == "-":
    for i in range(1, quantidade):
        resultado -= numeros[i]
    print("O resultado da subtração é: ", resultado)
    
elif operacao == "*":
    for i in range(1, quantidade):
        resultado *= numeros[i]
    print("O resultado da multiplicação é: ", resultado)
    
elif operacao == "/":
    for i in range(1, quantidade):
        resultado /= numeros[i]
    print("O resultado da divisão é: ", resultado)
    
else:
    print("Operação inválida.")

# Calcula o maior, menor e a soma dos números da lista
maior = max(numeros)
menor = min(numeros)
somatorio = sum(numeros)

# Imprime os resultados do maior, menor e soma dos números
print("O maior número digitado foi:", maior)
print("O menor número digitado foi:", menor)
print("O total é:", somatorio)
