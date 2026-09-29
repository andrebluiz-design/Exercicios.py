nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")

if media >= 7.0:
  print("Situação: APROVADO")
elif media >= 5.0:
  print("Situação: RECUPERAÇÃO")
else:
  print("Situação: REPROVADO")