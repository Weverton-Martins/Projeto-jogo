import random

#Lista para armazenar as pontuações
pontuacoes = []

print("Bem vindo ao jogo de Adivinhação")

#loop de dificuldade
print("Escolha o nivel de dificuldade")
print("1. Fácil (10 tentativas)")
print("2. Médio (7 tentativas)")
print("3. Difícil (5 tentativas)")

while True:
    dificuldade = input("Digite o número da dificuldade desejada: ")
    if dificuldade == "1":
        tentativa_totais = 10
        break
    elif dificuldade == "2":
        tentativa_totais = 7
        break
    elif dificuldade == "3":
        tentativa_totais = 5
        break
    else:
        print("Opção invalida. Escolha 1, 2 ou 3.")

# Fazendo o loop de repetição do cód ate o usuario acertar, ate da o break ou decidir sair
while True:
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = tentativa_totais
    tentativas = 0

    print("\nEu pensei em um número entre 1 e 100.")
    print(f"Você tem {tentativa_totais} tentativas para adivinhar.")

    #loop das tentativas, jogador faz palpites até acertar ou acabar as tentativas.
    while tentativas_restantes > 0:
        palpite = input("\nDigite o seu palpite: ")

        #Verificando se o input é um número válido
        if not palpite.isdigit():
            print("Por favor, digite um número válido")
            continue
        #convertendo palpite para inteiro
        palpite = int(palpite)

        if palpite < 1 or palpite > 100:
            print("O numero deve estar entre 1 e 100")
            continue
        tentativas += 1
        #desconta tentativas
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao = tentativas_restantes * 10  #calculo de pontuação
            pontuacoes.append(pontuacao)
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")
        
        print(f"Tentativas restantes: {tentativas_restantes}")
    #while else para qnd as tentativa acabarem
    else:
        print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}.") 
        pontuacoes.append(0)

        # Exibindo o Placar, após cada partida exibir o histórico de pontuações
    print("\nPlacar:")
    for idx, pontos in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pontos} pontos")

# Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break