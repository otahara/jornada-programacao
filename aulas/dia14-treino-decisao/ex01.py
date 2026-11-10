PRIMEIRA_HORA = 1
PRECO_PRIMEIRA_HORA = 8.00
PRECO_DEMAIS_HORAS = 3.00
HORAS_MINIMAS_DESCONTO = 3
DESCONTO = 5.00
MINUTOS_POR_HORA = 60
MINUTOS_TOLERANCIA  = 30

minutos = int(input("Minutos: "))

if minutos < 0:
    print("Tempo inválido")
elif minutos <= MINUTOS_TOLERANCIA :
    print(f"Primeiros {MINUTOS_TOLERANCIA } minutos são grátis")
else:
    tem_cartao = input("Tem cartão de cliente? (s/n) ").lower() == "s"

    horas_cobradas = minutos // MINUTOS_POR_HORA
    minutos_restantes = minutos % MINUTOS_POR_HORA

    if minutos_restantes > 0:
        horas_cobradas = horas_cobradas + 1

    valor = PRECO_PRIMEIRA_HORA + (PRECO_DEMAIS_HORAS * (horas_cobradas - PRIMEIRA_HORA))

    if horas_cobradas >= HORAS_MINIMAS_DESCONTO and tem_cartao:
        valor = valor - DESCONTO

    print(f"Horas cobradas: {horas_cobradas}")
    print(f"Total: R$ {valor:.2f}")