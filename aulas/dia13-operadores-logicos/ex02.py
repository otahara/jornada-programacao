PRIMEIRA_HORA = 1
PRECO_PRIMEIRA_HORA = 8.00
PRECO_DEMAIS_HORAS = 3.00
HORAS_MINIMAS_DESCONTO = 3
DESCONTO = 5.00

horas = int(input("Horas: "))
tem_cartao = input("Tem cartão de cliente? (s/n) ").lower()

if horas > PRIMEIRA_HORA:
    valor = PRECO_PRIMEIRA_HORA + (PRECO_DEMAIS_HORAS * (horas - PRIMEIRA_HORA))
else:
    valor = PRECO_PRIMEIRA_HORA

if horas >= HORAS_MINIMAS_DESCONTO and tem_cartao == 's':
    valor = valor - DESCONTO

print(f"Total: R$ {valor:.2f}")