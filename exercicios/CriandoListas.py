# Lista para armazenar o inventário
inventario = []

# Variável de controle para o loop
resposta = "S"

# Loop para coletar informações sobre o inventário
while resposta == "S":
    # Coleta informações sobre o equipamento e adiciona à lista de inventário
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))

    # Pergunta ao usuário se deseja continuar adicionando itens ao inventário
    resposta = input("Digite \"S\" para continuar, caso não digite \"N\" para finalizar: ").upper()

    # Loop para imprimir os elementos do inventário
    for elemento in inventario:
        print(elemento)


