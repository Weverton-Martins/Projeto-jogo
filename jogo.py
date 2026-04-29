import random

print('-'*5,'Boas-Vindas ao jogo de adivinhação','-'*5)
print('Escolha o nivel de dificuldade')
print('1 - Facil(10 Tentativa)')
print('2 - Normal(7 Tentativa)')
print('3 - Difici(5 Tentativa)')

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


pontuacao = []
palpites = []

print('Você tem 7 tentativas para adivinhar o numero secreto!\n')

while True:
    num_aleatorio = random.randint(1,100)
    tentativa_restante = tentativa_total
    tentativa = 0

    while tentativa_restante > 0:
        entrada = input('\nInforme seu palpite de 1 até 100: ')
        
        if not entrada.isdigit():
            print('Favor informe apenas numeros!')
            break

        palpite = int(entrada)
        tentativa_restante -=1
        tentativa +=1
        
        if palpite <= 1 or palpite >=100:
            print('\nO numero deve ser entre 1 e 100.')
            print(f'Restam {tentativa_restante}')
        
        elif palpite > num_aleatorio:
            print(f'\nVocê errou, o numero secreto é menor. Restam {tentativa_restante}')
            palpites.append(palpite)
            print(f'Numeros tentatos: {palpites}')
        
        elif palpite < num_aleatorio:
            print(f'\nVocê errou, o numero secreto é maior. Restam {tentativa_restante}')
            palpites.append(palpite)
            print(f'Numeros tentatos: {palpites}')

        elif palpite == num_aleatorio:
            pontos = tentativa_restante * 10 * (int(dificuldade))
            pontuacao.append(pontos)
            print(f'Parabéns você acertou em {tentativa} tentativas.')
            print(f'Sua pontuação é {pontos}')
            break

    if tentativa_restante == 0:
        print(f'\n Que pena suas tentativas acabram, o numero secreto era {num_aleatorio}')
    
    denovo = input('\nDeseja jogar novamente ? (S / N): ').lower()
    if denovo != 's':
        print('Obrigado por jogar!')
        print(f'\nPlacar de todas as jogadas: {pontuacao}')
        break


    

            