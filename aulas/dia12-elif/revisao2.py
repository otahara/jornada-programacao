DESCONTO = 15

produto = input("Produto: ")
preco = float(input("Preço: "))

preco_com_desconto = preco - (preco * (DESCONTO / 100))

print(f"{produto}: R$ {preco:.2f} -> com desconto R$ {preco_com_desconto:.2f}")