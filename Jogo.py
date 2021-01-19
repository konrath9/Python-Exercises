import random

print("Bem-vindo ao jogo #ADVINHE O NÚMERO#")
print("Você tem 7 chances para acertar o número. BOA SORTE!!!")
print()
sorteio = random.randint(1, 100)
nome = str(input("Digite seu nome: "))
palpite = int(input("Qual é o seu palpite? "))

if palpite == sorteio:
    print(f"Parabéns {nome}, você acertou de primeira. O número é {sorteio}.")
else:
    if palpite < sorteio:
        print("Você errou, o número informado é menor. Você pode tentar mais 6 vezes")
    else:
        print("Você errou, o número informado é maior. Você pode tentar mais 6 vezes")

    for i in range(0, 6):
        palpite = int(input("Digite um novo número: "))
        if palpite == sorteio:
            print(f"Parabéns {nome}, você acertou em {i+2} tentativas. O número é {sorteio}.")
            break
        elif palpite < sorteio:
            if i == 5:
                print(f"Você errou e suas tentativas acabaram. O número era {sorteio}.")
            else:
                print(f"Você errou, o número informado é menor. Você pode tentar mais {5-i} vezes")
        else:
            if i == 5:
                print(f"Você errou e suas tentativas acabaram. O número era {sorteio}.")
            else:
                print(f"Você errou, o número informado é maior. Você pode tentar mais {5-i} vezes")