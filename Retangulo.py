import math

B = float(input("Base do retângulo: "))
A = float(input("Altura do retângulo: "))

area = B * A
print(f"AREA = {area:.4f}")

per = B + B + A + A
print(f"PERIMETRO = {per:.4f}")

diag = math.sqrt(B ** 2 + A ** 2)
print(f"DIAGONAL = {diag:.4f}")