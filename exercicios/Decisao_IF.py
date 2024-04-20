# Solicita ao usuário que insira o nome
nome = input("Digite o nome: ")

# Solicita ao usuário que insira a idade e converte para inteiro
idade = int(input("Digite a idade: "))

# Solicita ao usuário que indique se há suspeita de doença infecto-contagiosa e converte para maiúsculas
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?: ").upper()

# Verifica as condições para determinar o atendimento prioritário
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")

# Mensagem de conclusão do sistema
print("Sistema finalizado com sucesso. Execute novamente se precisar.")
