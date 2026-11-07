VALOR_FRETE_PADRAO = 15
VALOR_PARA_ISENCAO_FRETE = 100

valor_compra = float(input("Valor da compra: "))

if valor_compra >= VALOR_PARA_ISENCAO_FRETE:
    frete = 0
    print("Frete grátis!")
else:
    frete = VALOR_FRETE_PADRAO
    print(f"Frete: R$ {VALOR_FRETE_PADRAO:.2f}")
print(f"Total: R$ {valor_compra + frete:.2f}")