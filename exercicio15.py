preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"\nSubtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")