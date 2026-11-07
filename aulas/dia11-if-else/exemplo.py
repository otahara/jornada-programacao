META_MINUTOS = 120

minutos = int(input("Minutos estudados: "))

if minutos >= META_MINUTOS:
    print("Meta batida!")
    print("Até amanhã!")
else:
    faltam = META_MINUTOS - minutos
    print(f"Faltam {faltam} minutos")
    print(f"Estude mais {faltam} minutos para encerrar seu dia!")