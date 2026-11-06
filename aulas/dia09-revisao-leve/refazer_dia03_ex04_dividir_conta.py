valor_total = float(input("Qual é o valor total da conta? "))
quantitdade_pessoas = int(input("Quantas pessoas vão dividir? "))
valor_por_pessoa = valor_total / quantitdade_pessoas
print(f"Cada pessoa paga R$ {valor_por_pessoa:.2f}")