# Informações de login do usuário
nome_user = 'Lucas'
senha_user = '12456'

# Contador de tentativas de login
tentativas = 0

# Loop para controlar as tentativas de login
while tentativas < 3:  # Garante que o número máximo de tentativas seja 3
    # Solicita ao usuário que insira o login e a senha
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    # Verifica se o login e a senha inseridos correspondem aos dados de login do usuário
    if login == nome_user and senha == senha_user:
        print('Login efetuado com sucesso')
        break  # Sai do loop se o login for bem-sucedido
    else:    
        print('Login e/ou senha estão inválidas')
    
    # Incrementa o contador de tentativas
    tentativas += 1

# Verifica se o usuário excedeu o número máximo de tentativas
if tentativas >= 3:
    print('Você excedeu o número máximo de tentativas')
