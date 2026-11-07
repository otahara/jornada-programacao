META_MINUTOS = 120

minutos = int(input("Minutos estudados: "))
# Defeito original: esta linha estava com um recuo a mais.
# Nenhum if ou else abria um bloco aqui, e por isso o Python mostrava:
# IndentationError: unexpected indent
faltam = META_MINUTOS - minutos

if minutos >= META_MINUTOS:
    print("Meta batida!")
else:
    print(f"Faltam {faltam} minutos")