n = int(input("Quantos números você vai digitar? "))

vet = [0 for x in range(n)]

soma = 0
for i in range (0, n):
    vet[i] = float(input("Digite um número: "))
    soma = soma + vet[i]

print()
print("Valores = ", end="")
for i in range (0,n):
    print(f"{vet[i]:.1f} ", end="")

print()
print(f"Soma = {soma:.2f}")
media = soma / n
print(f"Media = {media:.2f}")

