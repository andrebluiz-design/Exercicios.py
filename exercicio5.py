metros = float(input("Metros: "))

cm = metros * 100
mm = metros * 1000

def formatar(n):
    return f"{int(n)}" if n.is_integer() else f"{n}"

print(f"\nCentímetros: {formatar(cm)}")
print(f"Milímetros: {formatar(mm)}")