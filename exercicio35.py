idade = int(input("Idade: "))
estudante_input = input("Estudante: ").strip().upper()


if idade < 12 or estudante_input == "SIM" or idade >= 60:
    valor_ingresso = 15.00
else:
    valor_ingresso = 30.00

print(f"Valor do ingresso: R$ {valor_ingresso:.2f}")