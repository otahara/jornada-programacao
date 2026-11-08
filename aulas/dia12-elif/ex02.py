LIMITE_FAIXA_1 = 100
PRECO_FAIXA_1 = 0.60
LIMITE_FAIXA_2 = 200
PRECO_FAIXA_2 = 0.90
PRECO_FAIXA_3 = 1.20

consumo = int(input("Consumo (kWh): "))

if consumo <= LIMITE_FAIXA_1:
    valor_conta = consumo * PRECO_FAIXA_1
elif consumo <= LIMITE_FAIXA_2:
    valor_conta = (LIMITE_FAIXA_1 * PRECO_FAIXA_1) + ((consumo - LIMITE_FAIXA_1) * PRECO_FAIXA_2)
else:
    valor_conta = (LIMITE_FAIXA_1 * PRECO_FAIXA_1) + ((LIMITE_FAIXA_2 - LIMITE_FAIXA_1) * PRECO_FAIXA_2) + ((consumo - LIMITE_FAIXA_2) * PRECO_FAIXA_3)

print(f"Valor da conta: R$ {valor_conta:.2f}")