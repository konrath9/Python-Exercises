n = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range (n)] for x in range (n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = input(f"Elemento [{i},{j}]: ")

print("Diagonal principal:")

for i in range(0, n):
    for j in range(0, n):
        if i == j:
            print(f"{mat[i][j]} ", end="")

cont = 0
for i in range(0, n):
    for j in range(0, n):
        if int(mat[i][j]) < 0:
            cont = cont + 1
print()
print(f"Quantidade de negativos = {cont}")
