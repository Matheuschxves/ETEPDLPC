import time 
print("Olá Seja Bem vinda ao Joben")
a = int(input(''' Deseja ir em busca de alguma funcionária?
[1]- Sim, Me mostre as pessoas que estão em busca de uma oportunidade de emprego
[2]- Não, Desejo continuar na tela inicial.
Resposta: '''))
time.sleep(1)
sim = 1
não = 2
if a == 1:
    print("Lista das pessoas que estão procurando uma oportunidade de emprego:")
    vet1 = [''' Nome e Sobrenome: Maria Oliveira
    Área de atuação: Estética
    Estado: Pernambuco
    Cidade: Paulista
    Bairro: Pau Amarelo
    Experiência: 5 anos trabalhando na área
    ''']
    vet2 = [''' Nome e Sobrenome: Joanna Silva
    Área de atuação: Engenharia Civil
    Estado: Pernambuco
    Cidade: Olinda
    Bairro: Rio Doce
    Experiência: 6 Anos atuando no ramo
    ''']
    vet3 = [''' Nome e Sobrenome: Eduarda Marques
    Área de atuação: Teatro e Dramartugia
    Estado: São Paulo
    Cidade: São Paulo
    Bairro: Vila Edge
    Experiência: 10 Anos trabalhando como atriz, mais de 4000 peças e filmes feitos
    ''']
    vet4 = [''' Nome e Sobrenome: Danny Maria
    Área de atuação: Medicina Veterinária
    Estado: Pernambuco
    Cidade: Jaboatão dos Gurarapes
    Bairro: Curado
    Experiência: 9 Anos no mercado
    ''']
    
    funcionaria = int(input('''Selecione a candidata que seja da mesma área de atuação que sua empresa
    [1]- Maria
    [2]- Joanna
    [3]- Eduarda
    [4]- Danny
     Resposta: '''))
    time.sleep(1)
    maria = 1
    joanna = 2
    eduarda = 3
    danny = 4
    if funcionaria == 1:
        print("Você selecionou a funcionária Maria!")
        contato1 = int(input('''Você deseja entrar em contato com essa candidata?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1 
        nao = 2
        if contato1 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para a candidata entrar em contato com você!")) 
            time.sleep(1)
            print("Seu número foi confirmado, Aguarde a resposta da candidata") 
        if contato1 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if funcionaria  == 2:
        print("Você selecionou a candidata Joanna")
        time.sleep(1)
        contato2 = int(input('''Você deseja entrar em contato com essa candidata?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1 
        não = 2
        if contato2 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para a candidata entrar em contato com você!")) 
            time.sleep(1)
            print("Seu número foi confirmado, Aguarde a resposta da candidata")
        if contato2 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if funcionaria == 3:
        print("Você selecionou a candidata Eduarda")
        contato3 = int(input('''Você deseja entrar em contato com essa candidata?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1
        não = 2
        if contato3 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para a candidata entrar em contato com você")) 
            time.sleep(1)
            print("Seu número foi confirmado. Aguarde a resposta da candidata")
        if contato3 == 2:
            print("Okay, levaremos você de volta a tela inicial!")
    if funcionaria == 4:
        print("Você selecionou a candidata Danny")
        contato4 = int(input('''Você deseja entrar em contato com essa Candidata?
        [1]-Sim.
        [2]-Não.
        Resposta: '''))
        time.sleep(1)
        sim = 1
        não = 2
        if contato4 == 1:
            int(input("Seja bem vindo ao nosso chat, Informe um número de whatsapp para  a candidata entrar em contato com você")) 
            time.sleep(1)
            print("Seu número foi confirmado; Aguarde a resposta da candidata")
            if contato4 == 2:
                print("Okay, levaremos você de volta a tela inicial!")
if a == 2:
    print("Você continuará na tela inicial!")
