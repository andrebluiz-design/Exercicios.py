a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if (a < b + c) and (b < a + c) and (c < a + b):
  print("Resultado: FORMAM UM TRIÂNGULO")
else:
  print("Resultado: NÃO FORMAM UM TRIÂNGULO")