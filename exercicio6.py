largura = float(input("Largura: "))
altura = float(input("Altura: "))

area = largura * altura
perimetro = 2 * (largura + altura)

def formatar(n):
    return f"{int(n)}" if n.is_integer() else f"{n}"

print(f"\nÁrea: {formatar(area)}")
print(f"Perímetro: {formatar(perimetro)}")