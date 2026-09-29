mes = int(input("Mês: "))
ano = int(input("Ano: "))

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")
else:
    
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
    
    if mes == 2:
        dias = 29 if bissexto else 28
    elif mes in [4, 6, 9, 11]:
        dias = 30
    else:
        dias = 31
        
    print(f"{dias} dias")