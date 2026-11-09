IDADE_MINIMA = 18

idade = int(input("Idade: "))
tem_ingresso = input("Tem ingresso? (s/n) ")

if idade >= IDADE_MINIMA and tem_ingresso.lower() == "s":
    print("Pode entrar")
else:
    print("Não pode entrar")