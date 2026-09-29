a = float(input("Primeiro lado: "))  
b = float(input("Segundo lado: "))  
c = float(input("Terceiro lado: "))  

if (a < b + c) and (b < a + c) and (c < a + b):  
  if a == b == c:  #[cite: 16]
    print("Tipo: EQUILÁTERO")  
  elif a == b or b == c or a == c:  
    print("Tipo: ISÓSCELES") 
  else:  #[cite: 16]
    print("Tipo: ESCALENO")  
else:
  print("Resultado: NÃO FORMAM UM TRIÂNGULO") 