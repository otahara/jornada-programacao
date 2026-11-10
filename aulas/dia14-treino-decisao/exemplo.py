IDADE_MINIMA = 18

idade = int(input("Idade: "))

if idade < IDADE_MINIMA:
    print("Entrada proibida")
else:
    tem_ingresso = input("Tem ingresso? (s/n) ").lower() == "s"
    if tem_ingresso:
        print("Pode entrar")
    else:
        print("Compre o ingresso na bilheteria")