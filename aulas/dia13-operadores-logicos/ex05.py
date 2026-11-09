LIMITE_LIVROS = 3

resposta_cadastro = input("Tem cadastro? (s/n) ")
tem_cadastro = resposta_cadastro.lower() == "s"
resposta_multa = input("Tem multa? (s/n) ")
tem_multa = resposta_multa.lower() == "s"

quantidade_livros = int(input("Quantos livros estão com você? "))

if not tem_cadastro:
    print("Faça o cadastro primeiro")
elif tem_multa or quantidade_livros >= LIMITE_LIVROS:
    print("Empréstimo bloqueado")
else:
    print("Empréstimo liberado")