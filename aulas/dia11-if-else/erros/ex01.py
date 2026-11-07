idade = int(input("Idade: "))

if idade >= 18:
    # Defeito original: esta linha estava sem o recuo de 4 espaços.
    # Todo if precisa de um bloco, e por isso o Python mostrava:
    # IndentationError: expected an indented block after 'if' statement on line 3
    print("Maior de idade")
else:
    print("Menor de idade")