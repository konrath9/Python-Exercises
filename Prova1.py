print("Bem-vindo a calculadora, você deve digitar o tipo de operação e os dois números da operação\n")
codigo = int(input("Digite o codigo da operação, 1 = soma. 2 = subtração. 3 = multiplicação. "
                   "4 = divisão inteira\n"))
N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))

if codigo >=1 and codigo <= 4:
    if codigo == 1:
        resultado = N1 + N2
        print ("{} + {} = {}".format (N1, N2, resultado))
    elif codigo == 2:
        resultado = N1 - N2
        print ("{} - {} = {}".format (N1, N2, resultado))
    elif codigo == 3:
        resultado = N1 * N2
        print ("{} x {} = {}".format (N1, N2, resultado))
    else:
        resultado = N1 // N2
        print ("{} : {} = {}".format (N1, N2, resultado))
else:
    print("Esse número não corresponde a nenhuma das operações")





