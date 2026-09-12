valor = float(input("Digite um valor: "))

dobro = valor * 2
triplo = valor * 3
metade = valor / 2

# Remove casas decimais desnecessárias para números inteiros na exibição
def formatar(n):
    return f"{int(n)}" if n.is_integer() else f"{n}"

print(f"\nDobro: {formatar(dobro)}")
print(f"Triplo: {formatar(triplo)}")
print(f"Metade: {formatar(metade)}")