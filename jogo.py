import random #Importando a biblioteca
#Menu da escolha do nivel de dificuldade
print('-'*5,'Boas-Vindas ao jogo de adivinhação','-'*5)
print('1 - Facil(10 Tentativa)')
print('2 - Normal(7 Tentativa)')
print('3 - Difici(5 Tentativa)')
#Laço do menu
while True:
    dificuldade = int(input('\nEscolha qual nivel de dificuldade deseja jogar: '))
    
    if dificuldade == 1:
        tentativa_total = 10
        break
    
    elif dificuldade == 2:
        tentativa_total = 7
        break

    elif dificuldade == 3:
        tentativa_total = 5
        break
    
    else:
        print('Opção invalida, digite uma nova opção que esteja disponivel!')

#Listas que armazenan pontuação 
pontuacao = []

print(f'\nVocê tem {tentativa_total} tentativas para adivinhar o numero secreto!')
#Laço onde jogador informa seus palpites e joga ate acertar dentro do limite de tentativas ou escolha sair 
while True:
    
    palpites = [] #palpites já informados pelos jogadores
    num_aleatorio = random.randint(1,100)#gerador de número aleatório
    #contador de tentativas
    tentativa_restante = tentativa_total
    tentativa = 0
    #Laço dos palpites/tentativas e opções
    while tentativa_restante > 0:
        entrada = input('\nInforme seu palpite de 1 até 100: ')
        #validador de números, não aceita letras 
        if not entrada.isdigit():
            print('Favor informe apenas numeros!')
            break

        palpite = int(entrada) #pegando o valor de entrada
        tentativa_restante -=1 #a cada jogada desconta na quantidade total de tentativa
        tentativa +=1 #a cada jogada acrescenta tentativa
        
        if palpite < 1 or palpite >=100: #Valida se esta dentro do limear solicitado
            print('\nO numero deve ser entre 1 e 100.')
            print(f'Restam {tentativa_restante} tentativas!')
        
        elif palpite > num_aleatorio:
            print(f'\nVocê errou, o numero secreto é menor. Restam {tentativa_restante} tentativas!')
            palpites.append(palpite)#Guarda quais numeros ja foram ditos
            print(f'Numeros tentatos: {palpites}')
        
        elif palpite < num_aleatorio:
            print(f'\nVocê errou, o numero secreto é maior. Restam {tentativa_restante} tentativas!')
            palpites.append(palpite)
            print(f'Numeros tentatos: {palpites}')

        elif palpite == num_aleatorio:
            pontos = tentativa_restante * 10 * (int(dificuldade)) #calculo de pontuação
            pontuacao.append(pontos)#Guarda o ponto feito
            print(f'Parabéns você acertou em {tentativa} tentativas.')
            print(f'Sua pontuação é {pontos}')
            break

        if tentativa_restante == 0:
            print(f'\n Que pena suas tentativas acabram, o numero secreto era {num_aleatorio}')
    #condição se deseja continuar jogando ou não
    denovo = input('\nDeseja jogar novamente ? (S / N): ').lower()#.lower() evita que o terminal recuse letras maiúscula ou minúsculas
    if denovo != 's':
        print('Obrigado por jogar!')
        print(f'\nPlacar de todas as jogadas: {pontuacao}') #exibe o placar das rodadas que foram jogadas
        break


    

            