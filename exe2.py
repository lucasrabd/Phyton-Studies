
## LUCAS CARABOLAD BOB RM550519
## PAULO HENRIQUE MOREIRA ANGUEIRA RM99704
nome_user = 'Lucas'
senha_user = '12456'

tentativas: 0

while True <= 3:
    login: input('Digite o login: ')
    senha: input('Digite a senha: ')
if  login == login and senha == senha_user:
    print('Login efetuado com exito')
    break
else:    
    print ('Login e/ou senha estão invalidas')
tentativas += 1

if tentativas >=3:
    print ('Você execedeu o numero máximo de tentativas')