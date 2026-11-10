primeiro_numero = int(input("Número 1: "))
segundo_numero = int(input("Número 2: "))
terceiro_numero = int(input("Número 3: "))

# eu comparei o primeiro número com o segundo e terceiro, se ele for maior ou igual, vai ser ele o maior número, e assim eu vou fazer para o restante do código
if primeiro_numero >= segundo_numero and primeiro_numero >= terceiro_numero:
    print(f"Maior: {primeiro_numero}")
elif segundo_numero >= primeiro_numero and segundo_numero >= terceiro_numero:
    print(f"Maior: {segundo_numero}")
else:
    print(f"Maior: {terceiro_numero}")