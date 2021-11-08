import time 
login = int (input('''Seja bem vindo(a) ao aplicativo Joben!
Você já tem alguma conta no APP?
    [1]- Sim, fazer login
    [2]- Não, fazer cadastro
    Resposta: '''))
sim = 1
não = 2
if login == 1:
    user = int(input(''' 
    Selecione o seu Usuário:
    [1]-Empresa
    [2]-Funcionária
    '''))
    empresa = 1
    funcionaria = 2
    if user == 1:
        str(input("Insira seu E-mail: "))
        int(input("Agora insira sua senha contendo apenas números: "))
        time.sleep(1)
        print("Login realizado com sucesso!!")
        time.sleep(1)
        print("Bem vindo de volta!!!")
    if user == 2:
        str(input("Insira seu E-mail: "))
        int(input("Agora insira sua senha contendo apenas números: "))
        time.sleep(1)
        print("Login realizado com sucesso!!")
        time.sleep(1)
        print("Bem vinda de volta!!!")
if login == 2:
    cadastro = int (input('''Você deseja criar uma conta?
    [1]- Sim, Iniciar cadastro
    [2]- Não, Voltar para a página inicial
    Resposta: '''))
    time.sleep(1)
    sim = 1 
    não = 2
    if cadastro == 1:
        usuario = int (input('''Selecione o seu usuário
        [1]- Empresa ou pequeno négocio
        [2]- Funcionárias
        Resposta: '''))
        time.sleep(1)
        if usuario == 1:
            print("Insira os seguintes dados: ")
            str(input("Nome da sua empresa:"))
            str(input("Área de atuação da empresa(EX:Alimentação;Industria; ETC..."))
            str(input("Estado:"))
            str(input("Cidade:"))
            str(input("Bairro:"))
            time.sleep(1)
            str(input("Agora insira seu endereço de E-Mail: "))
            int(input("Insira uma senha(CONTENDO APENAS NÚMEROS): "))
            time.sleep(1)
            print("O cadastro da sua empresa foi concluído com sucesso!!!")
            time.sleep(1)
            print("Bem vindo ao Jobeen!!!")
            print("Esperamos que sua experiência com o app seja incrível!!! Ass: Equipe Joben")
        if usuario == 2:
            print("insira os seguintes dados:")
            str(input("Nome Completo: "))
            str(input("Naturalidade: "))
            str(input("Estado Civil: "))
            int(input("Digite seu CPF: "))
            int(input("Insira um telefone para contato: "))
            str(input("Insira seu E-Mail: "))
            int(input("Insira uma senha(CONTENDO APENAS NÚMEROS): "))
            time.sleep(1)
            print("Cadastro realizado com sucesso!!! ")
            time.sleep(1)
            print("Esperamos que sua experiência com o app seja incrível!!! Ass: Equipe Joben")
    if cadastro == 2:
        print("você retornou para a página inicial!")
