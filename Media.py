print("Media Escolar:")
print()
nome = input("Digite seu nome: ")
materia = input("Digite o nome da matéria: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = float((nota1 + nota2 + nota3 + nota4) / 4)

if media < 7:
    print(f"Aluno {nome}, você foi REPROVADO. Sua média em {materia} foi {media:.1f}")
else:
    print("PARABENS!!")
    print(f"Aluno {nome}, você foi APROVADO. Sua média em {materia} foi {media:.1f}")
