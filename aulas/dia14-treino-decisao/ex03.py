primeiro_numero = int(input("Número 1: "))
segundo_numero = int(input("Número 2: "))
terceiro_numero = int(input("Número 3: "))
quarto_numero = int(input("Número 4: "))
quinto_numero = int(input("Número 5: "))
sexto_numero = int(input("Número 6: "))
setimo_numero = int(input("Número 7: "))

maior = primeiro_numero

if segundo_numero > maior:
    maior = segundo_numero
if terceiro_numero > maior:
    maior = terceiro_numero
if quarto_numero > maior:
    maior = quarto_numero
if quinto_numero > maior:
    maior = quinto_numero
if sexto_numero > maior:
    maior = sexto_numero
if setimo_numero > maior:
    maior = setimo_numero

print(f"Maior: {maior}")