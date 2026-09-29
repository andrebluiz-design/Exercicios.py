celsius = float(input("Temperatura em °C: "))

fahrenheit = (celsius * 9 / 5) + 32

def formatar(n):
    return f"{int(n)}" if n.is_integer() else f"{n}"

print(f"\nTemperatura em °F: {formatar(fahrenheit)}")