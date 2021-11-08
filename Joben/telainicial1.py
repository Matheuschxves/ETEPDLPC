import time 
print("Olá Seja Bem vinda ao Joben")
a = int(input(''' Deseja ir em busca de alguma oportunidade de emprego? 
[1]- Sim, Me mostre as oportunidades de emprego disponível
[2]- Não, Desejo continuar na tela inicial.
Resposta: '''))
time.sleep(1)
sim = 1
não = 2
if a == 1:
    print("Aqui temos essas opções de emprego disponíveis:")
    vet1 = [''' Nome: Esposende
    Área de atuação: Calçados/Vendas
    Estado: Pernambuco
    Cidade: Recife
    Bairro: Boa vista
    Salário: R$1200,00/mês
    Requer experiência: Sim, mínimo 1 ano de trabalho como vendedora
    ''']
    vet2 = ['''Nome: Coca-cola
    Área de atuação: Indústria de Alimentos
    Estado: Pernambuco
    Cidade: Paulista
    Bairro: Pau amarelo
    Salário: R$850,00/mês
    Requer experiência: Não, não exigimos nenhum tipo de experiência
    ''']
    vet3 = [''' Nome: MGM Tecnologia
    Área de atuação:T.i
    Estado: Pernambuco
    Cidade: Ipojuca
    Bairro: Porto de Galinhas
    Salário: R$:50.000,00/mês
    Requer experiência: Sim, Mínimo de 3 anos no mercado de tecnologia
    OBS: Procuramos por profissional de segurança da informação
    ''']
    vet4 = [''' Nome: Netflix
    Área de atuação: Entreterimento 
    Estado: São Paulo
    Cidade: Guarulhos
    Bairro: Vila Augusta
    Salário: R$:100.000,00/mês
    Requer experiência: Sim, 5 anos de experiência
    ''']
    empresa = int(input('''Selecione a vaga de emprego na qual você mais se interessou
    [1]- Esposende
    [2]- Coca-Cola
    [3]- MGM Tecnologia
    [4]- Netflix
    Resposta: '''))
    time.sleep(1)
    esposende = 1
    cocacola = 2
    mgm = 3
    netflix = 4
    if empresa == 1:
        print("Você selecionou a empresa Esposende!")
        contato1 = int(input('''Você deseja entrar em contato com essa empresa?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1 
        nao = 2
        if contato1 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para entrarmos em contato com você: ")) 
            time.sleep(1)
            print("Seu número foi confirmado, entrameros em contato com você para acertamos direto essa contratação.") 
        if contato1 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if empresa  == 2:
        print("Você selecionou a empresa Coca-Cola")
        time.sleep(1)
        contato2 = int(input('''Você deseja entrar em contato com essa empresa?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1 
        não = 2
        if contato2 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para entrarmos em contato com você: ")) 
            time.sleep(1)
            print("Seu número foi confirmado, entrameros em contato com você para acertamos direto essa contratação.")
        if contato2 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if empresa == 3:
        print("Você selecionou a empresa MGM Tecnologia")
        contato3 = int(input('''Você deseja entrar em contato com essa empresa?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1
        não = 2
        if contato3 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para entrarmos em contato com você: ")) 
            time.sleep(1)
            print("Seu número foi confirmado, entrameros em contato com você para acertamos direto essa contratação.")
        if contato3 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if empresa == 4:
        print("Você selecionou a empresa Netflix")
        contato4 = int(input('''Você deseja entrar em contato com essa empresa?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1
        não = 2
        if contato4 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para entrarmos em contato com você: ")) 
            time.sleep(1)
            print("Seu número foi confirmado, entrameros em contato com você para acertamos direto essa contratação.")
        if contato4 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
if a == 2:
    print("Você continuará na tela inicial!")
