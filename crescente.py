print("Digite dois números:")
a = int(input())
b = int(input())

while a != b :
    if a > b:
        print("Decrescente")
    else:
        print("Crescente")

    print("Digite outros dois números:")
    a = int(input())
    b = int(input())