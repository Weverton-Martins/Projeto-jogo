import random #Importando a biblioteca

print('-'*5,'Boas-Vindas ao jogo de adivinhação','-'*5)
#Menu de dificuldade
print('Escolha o nivel de dificuldade')
print('1 - Facil(10 Tentativa)')
print('2 - Normal(7 Tentativa)')
print('3 - Difici(5 Tentativa)')
#Laço do menu
while True:
    dificuldade = int(input('Escolha o nivel de dificuldade: '))
    
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

#Listas
pontuacao = []
palpites = []

print('Você tem 7 tentativas para adivinhar o numero secreto!\n')
#Laço pro jogador jogar ate escolher sair
while True:
    num_aleatorio = random.randint(1,100)
    tentativa_restante = tentativa_total
    tentativa = 0
    #Laço dos palpites/tentativas e opções
    while tentativa_restante > 0:
        entrada = input('\nInforme seu palpite de 1 até 100: ')
        #validar que não aceita letras, apenas numeros
        if not entrada.isdigit():
            print('Favor informe apenas numeros!')
            break

        palpite = int(entrada) #pegando o valor de entrada
        tentativa_restante -=1 #a cada jogada desconta na quantidade total de tentativa
        tentativa +=1 #a cada jogada acrescenta tentativa
        #Valida se esta dentro do limear solicitado
        if palpite <= 1 or palpite >=100:
            print('\nO numero deve ser entre 1 e 100.')
            print(f'Restam {tentativa_restante}')
        
        elif palpite > num_aleatorio:
            print(f'\nVocê errou, o numero secreto é menor. Restam {tentativa_restante}')
            palpites.append(palpite)#Guarda quais numeros ja foram ditos
            print(f'Numeros tentatos: {palpites}')
        
        elif palpite < num_aleatorio:
            print(f'\nVocê errou, o numero secreto é maior. Restam {tentativa_restante}')
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
    denovo = input('\nDeseja jogar novamente ? (S / N): ').lower()
    if denovo != 's':
        print('Obrigado por jogar!')
        print(f'\nPlacar de todas as jogadas: {pontuacao}') #exibe o placar de rodas as jogadas
        break


    

            