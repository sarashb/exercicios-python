print("************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1
for rodada in range (1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    chute = int(input("Digite um número: "))
    print("Voce digitou", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100!")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        break
    elif (maior):
        print("Você errou! O seu chute foi maior que o numero secreto.")
    elif (menor):
        print("Você errou! O seu chute foi menor que o numero secreto.")
    rodada = rodada + 1
print("Fim de jogo.")