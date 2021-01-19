l1 = float(input("Digite a primeira medida: "))
l2 = float(input("Digite a segunda medida: "))
l3 = float(input("Digite a terceira medida: "))
l4 = float(input("Digite a quarta medida: "))

if (l1 == l2) and (l3 == l4) or (l1 == l3) and (l2 == l4) or (l1 == l4) and (l2 == l3) or (l2 == l4) and (l3 == l4):
    if (l1 == l2 == l3 == l4):
        print("É um quadrado")
    else:
        print("É um retângulo")
else:
    print("Não é quadrado nem retângulo")