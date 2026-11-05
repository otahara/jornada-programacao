MINUTOS_POR_HORA = 60

minutos = int(input("Tempo de prova (em minutos): "))
feitas = int(input("Total de questões: "))
acertadas = int(input("Total de acertadas: "))

horas = minutos // MINUTOS_POR_HORA
minutos_restantes = minutos % MINUTOS_POR_HORA

taxa_de_acerto = (acertadas / feitas) * 100

print(f"Tempo: {horas}h{minutos_restantes:02d}")
print(f"Acertos: {taxa_de_acerto:.1f}%")