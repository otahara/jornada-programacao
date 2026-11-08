IDADE_MINIMA_IDOSO = 60
IDADE_MINIMA_ADULTO = 18
IDADE_MINIMA_ADOLESCENTE = 12

idade = int(input("Idade: "))

if idade >= IDADE_MINIMA_IDOSO:
    faixa = "idoso"
elif idade >= IDADE_MINIMA_ADULTO:
    faixa = "adulto"
elif idade >= IDADE_MINIMA_ADOLESCENTE:
    faixa = "adolescente"
else:
    faixa = "criança"
    
print(f"Com {idade} anos, você é {faixa}.")