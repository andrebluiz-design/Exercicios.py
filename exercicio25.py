preco = float(input("Preço: R$ "))
opcao = int(input("Opção: "))

if opcao == 1:
  valor_final = preco * 0.9
elif opcao == 2:
  valor_final = preco * 0.95
elif opcao == 3:
  valor_final = preco
elif opcao == 4:
  valor_final = preco * 1.08

print(f"Valor final: R$ {valor_final:.2f}")