from time import sleep
import cx_Oracle

# Função para estabelecer a conexão com o banco de dados Oracle.
def conectar_banco_dados():
    try:
        connection = cx_Oracle.connect('user/senha@dominio:1521/sid')
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Erro ao conectar ao banco de dados:", error.message)
        return None

# Função para inserir um usuário no banco de dados.
def inserir_usuario(connection, cpf, nome, email, telefone, senha):
    try:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO usuarios (cpf, nome, email, telefone, senha) VALUES (:1, :2, :3, :4, :5)',
                       (cpf, nome, email, telefone, senha))  # Removi o campo de email extra
        connection.commit()
        cursor.close()
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Erro ao inserir usuário:", error.message)

# Função onde irá criar uma conta para caso o usuário não tenha e queira criar uma.
def criar_conta(connection):
    global usuario_logado
    print("-----Criação de cadastro------")
    try:
        nome_usuario = input("Digite o seu nome completo: ")
        cpf_usuario = int(input("Digite o seu CPF: "))
        email_usuario = input("Digite o seu email: ")
        telefone_usuario = int(input("Digite o seu número de telefone: "))
        senha_usuario = input("Digite uma senha: ")

        inserir_usuario(connection, cpf_usuario, nome_usuario, email_usuario, telefone_usuario, senha_usuario)

        # Define o usuário como logado
        usuario_logado = cpf_usuario

        print("\n")
        print("Agora vamos conferir seus dados!")
        print("Nome:", nome_usuario)
        print("CPF:", cpf_usuario)
        print("Email:", email_usuario)
        print("Telefone:", telefone_usuario)
        print("Senha:", senha_usuario)
    except ValueError as e:
        print("Erro ao criar conta:", e)

# Função para fazer login
def login(connection):
    global usuario_logado
    print("-----Login------")
    try:
        email_usuario = input("Digite o seu email: ")  # Alterado para pegar o email
        senha_usuario = input("Digite a sua senha: ")
        
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE email = :1 AND senha = :2', (email_usuario, senha_usuario))  # Alterado para buscar pelo email
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print("Login bem-sucedido!")
            usuario_logado = resultado[0]  # Define o usuário como logado
        else:
            print("E-mail ou senha incorretos. Tente novamente.")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Erro ao fazer login:", error.message)

# Função para limitar o valor de bicicletas que podem ser seguradas.
def valor_bicicleta():
    while True:
        print("")
        try:
            valor_bike = int(input("Digite o valor da sua bike: "))
            if valor_bike > 100000:
                print("")
                print("O valor da bicicleta está acima do permitido! Valor permitido apenas abaixo de R$100.000!")
                print("")
            elif valor_bike < 2000:
                print("")
                print("O valor da bicicleta não pode ser menor que R$2000")
                print("")
            else:
                return valor_bike
        except ValueError as e:
            print("Erro ao inserir valor da bicicleta:", e)
            opcao = input("Digite (1) para tentar novamente ou (2) para voltar ao menu principal: ")
            print("")
            if opcao == '2':
                menu_principal(connection)
                return -1


# Função da vistoria, que no caso seriam as informações da bike.
def seguro_de_bicicleta():
    try:
        print("-----Seguro de bicicleta-----")
        print("Para darmos continuidade no seu seguro, precisamos de certas informações")
        marca_bike = input("Digite a marca da sua bicicleta: ")
        modelo_bike = input("Digite o modelo da sua bicicleta: ")
        numero_nota_fiscal = input("Digite o número da nota fiscal da sua bicicleta: ")
        chassi = input("Digite o número do chassi da sua bicicleta: ")

        valor_bike = valor_bicicleta()  
        if valor_bike == -1:
            return

        acessorios_lista = []

        while True:
            acessorios = input("Possui algum acessório? Digite (1) para sim, digite (2) para não!\n")
            
            if acessorios != '1':
                break

            print("Precisaremos de algumas informações")
            qual_acessorio = input("Nome do acessório:\n")
            valor_acessorio = int(input("Digite o valor do acessório:\n"))
            nmr_nota_fiscal_acessorio = int(input("Digite o número de série da nota fiscal:\n"))

            acessorios_lista.append({
                "Nome do acessório": qual_acessorio,
                "Valor do acessório": valor_acessorio,
                "Número da nota fiscal": nmr_nota_fiscal_acessorio
            })

            print("Agora vamos conferir os dados da bike!")

            for acessorio in acessorios_lista:
                print("Informações do acessório:", acessorio)

        sleep(1)
        print("")
        print("Marca da bicicleta: ", marca_bike)
        print("Modelo da bicicleta: ", modelo_bike)
        print("Número da nota fiscal: ", numero_nota_fiscal)
        print("Valor da bicicleta: ", valor_bike)
        print("Número do chassi: ", chassi)
        print("\n")

        sleep(0.5)

        print("Para terminar o processo de vistoria, precisaremos de algumas fotos da bicicleta para confirmarmos que ela existe e que você possa pedalar em segurança!")
        print("Contudo, te encaminharemos uma mensagem para acessar o site onde possa tirar as fotos")
        print("\n")

        sleep(1)

        print("Após validação das fotos, confirmamos que está apto a fazer o seguro! Precisamos que escolha o plano de seguro!")
        print("\n")

        print("-----Planos de seguros-----")
        plano_seguro = (input("Digite (1) para o plano Pedal essencial \n"
                                "Digite (2) para o plano Pedal leve \n"
                                "Digite (3) para o plano Pedal elite \n"
                                "Digite (4) para voltar ao menu anterior \n"
                            "R: "))

        if plano_seguro == '1':
            print("Ok, o plano escolhido foi Pedal essencial!")
            print("")
            menu_principal(connection)
        elif plano_seguro == '2':
            print("Ok, o plano escolhido foi Pedal leve!")
            print("")
            menu_principal(connection)
        elif plano_seguro == '3':
            print("Ok, o plano escolhido foi Pedal elite!")
            print("")
            menu_principal(connection)
        elif plano_seguro == '4':
            menu_principal(connection)
        else:
            print("Número inválido!")

        # Criar uma string com as informações do seguro
        informacoes_seguro = f"Marca da bicicleta: {marca_bike}\n" \
                             f"Modelo da bicicleta: {modelo_bike}\n" \
                             f"Número da nota fiscal: {numero_nota_fiscal}\n" \
                             f"Valor da bicicleta: {valor_bike}\n" \
                             f"Número do chassi: {chassi}\n" \
                             f"Acessórios:\n"

        for acessorio in acessorios_lista:
            informacoes_seguro += f"  Nome do acessório: {acessorio['Nome do acessório']}\n" \
                                  f"  Valor do acessório: {acessorio['Valor do acessório']}\n" \
                                  f"  Número da nota fiscal: {acessorio['Número da nota fiscal']}\n"

        # Nome do arquivo de texto será o número do chassi
        nome_arquivo = f"{chassi}.txt"

        # Salvar as informações em um arquivo de texto
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(informacoes_seguro)

        print(f"As informações do seguro foram salvas no arquivo {nome_arquivo}")

    except Exception as e:
        print("Ocorreu um erro ao processar o seguro de bicicleta:", str(e))


# Função principal, sendo a função que será usada no principal, chamando todas as outras funções para poder rodar o nosso sistema.
def menu_principal(connection):
    global usuario_logado
    while True:
        print("--------Bem vindo ao menu da Porto--------")        
        try:
            escolha = int(input("Para criar a conta, digite (1) \n"
                            "Para fazer login, digite (2) \n"
                            "Para acessar as opções de seguro, digite (3) \n"
                            "Para tirar dúvidas, digite (4) \n"
                            "Para sair do programa, digite (0) \n"
                            "R: "))
            if escolha == 1:
                criar_conta(connection)
            elif escolha == 2:
                login(connection)
            elif escolha == 3:
                if usuario_logado:
                    print("-----Opções de seguro-----")
                    menu_seguro(connection)
                else:
                    print("Você precisa fazer login primeiro ou criar uma conta.")
            elif escolha == 4:
                print("-----Dúvidas-----")
                print("Para tirar as dúvidas, entre em contato no email\n"
                        "email@gmail.com")
                print("")
            elif escolha == 0:
                print("Obrigado por usar o nosso programa! \n"
                        "Programa encerrando...")
                sleep(1)
                break
            else:
                print("Opção inválida")
                print("")
        except ValueError as e:
            print("Erro ao processar escolha:", e)

# Função para levar o cliente para onde ele queira, puxando as outras funções.
def menu_seguro(connection):
    global usuario_logado
    opcoes = input("Para acessar seguro de carro, digite (1) \n"
                "Para acessar seguro de moto, digite (2) \n"
                "Para acessar seguro de bicicleta, digite (3)\n"
                "Para voltar ao menu anterior, digite (4) \n"
                "R: ") 

    if opcoes == '1' and usuario_logado:
        print("Esse serviço não está disponível!")
    elif opcoes == '2' and usuario_logado:
        print("Esse serviço não está disponível!")
    elif opcoes == '3' and usuario_logado:
        seguro_de_bicicleta()
    elif opcoes == '4':
        menu_principal(connection)
    else:
        print("Opção inválida")
        print("")

# Variável global para rastrear se o usuário está logado.
usuario_logado = None

# Principal
connection = conectar_banco_dados()
menu_principal(connection)
