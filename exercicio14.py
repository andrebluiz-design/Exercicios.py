a = int(input("A: "))
b = int(input("B: "))

# Troca utilizando uma variável auxiliar (conforme o requisito)
aux = a
a = b
b = aux

print("\nDepois da troca:")
print(f"A: {a}")
print(f"B: {b}")