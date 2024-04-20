# Solicita ao usuário que digite o nome do funcionário.
nome = input("Digite um funcionário: ")

# Solicita ao usuário que digite o nome da empresa.
empresa = input("Digite a instituição: ")

# Solicita ao usuário que digite a quantidade de funcionários na empresa.
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))

# Solicita ao usuário que digite a média da mensalidade na empresa.
mediaMensalidade = float(input("Digite a média da mensalidade: "))

# Imprime as informações inseridas pelo usuário.
print(nome + " trabalha na empresa " + empresa)
print("Possui:", qtde_funcionarios, "funcionários.")
print("A média da mensalidade é de:", str(mediaMensalidade))

# Imprime os tipos de dados de cada variável.
print("================Verifique os tipos de dados abaixo:================")
print("O tipo de dado da variável [nome] é:", type(nome))
print("O tipo de dado da variável [empresa] é:", type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é:", type(qtde_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é:", type(mediaMensalidade))
