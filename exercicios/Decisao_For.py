# Solicita ao usuário que insira um número para exibir a tabuada
tabuada = int(input("Digite um número para exibir a tabuada: "))

# Imprime a mensagem indicando qual é a tabuada que será exibida
print("Tabuada do número ", tabuada)

# Loop para calcular e exibir a tabuada do número fornecido pelo usuário
# Itera de 1 a 10, pois queremos apenas a tabuada de 1 a 10
for valor in range(1, 11, 1):
    # Calcula a multiplicação e imprime o resultado da tabuada
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))
