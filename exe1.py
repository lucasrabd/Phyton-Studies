## LUCAS CARABOLAD BOB RM 550519
## PAULO HENRIQUE MOREIRA ANGUEIRA RM 99704

numeros = []
operacao = input("Qual operacao deseja realizar? (+, -, *, /): ")
quantidade = int(input("Quantos números deseja utilizar? "))

for i in range(quantidade):
    numeros.append(float(input("Digite o número {}: ".format(i+1))))

resultado = numeros[0]

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

maior = max(numeros)
menor = min(numeros)
somatorio = sum(numeros)

print("O maior número digitado foi:", maior)
print("O menor número digitado foi:", menor)
print("O total é:", somatorio)