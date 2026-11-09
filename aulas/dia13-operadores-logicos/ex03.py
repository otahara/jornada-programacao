ENTRADA_INTEIRA = 30.0
MEIA_ENTRADA = ENTRADA_INTEIRA / 2
IDADE_MINIMA = 14
IDADE_IDOSO = 60

idade = int(input("Idade: "))
resposta_responsavel = input("Está com um responsável? (s/n) ")
tem_responsavel = resposta_responsavel.lower() == "s"
resposta_estudante = input("É estudante? (s/n) ")
estudante = resposta_estudante.lower() == "s"

if idade < IDADE_MINIMA and not tem_responsavel:
    print("Entrada não permitida")
elif idade >= IDADE_IDOSO or estudante:
    print(f"Meia-entrada: R$ {MEIA_ENTRADA:.2f}")
else:
    print(f"Inteira: R$ {ENTRADA_INTEIRA:.2f}")