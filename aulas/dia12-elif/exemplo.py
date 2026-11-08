NOTA_MINIMA_A = 9
NOTA_MINIMA_B = 7

nota = float(input("Nota: "))

if nota >= NOTA_MINIMA_A:
    print(f"Nota {nota:.2f} é Conceito A")
elif nota >= NOTA_MINIMA_B:
    print(f"Nota {nota:.2f} é Conceito B")
else:
    print(f"Nota {nota:.2f} é Conceito C")
