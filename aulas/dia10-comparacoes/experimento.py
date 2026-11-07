uf = input("Digite a UF: ").upper()
capital = input(f"Qual é a capital do {uf}? (desconsiderar acentos) ")

if uf == "AC":
    capital_certa = "rio branco"
elif uf == "AL":
    capital_certa = "maceio"
elif uf == "AM":
    capital_certa = "manaus"
elif uf == "AP":
    capital_certa = "macapa"
elif uf == "BA":
    capital_certa = "salvador"
elif uf == "CE":
    capital_certa = "fortaleza"
elif uf == "DF":
    capital_certa = "brasilia"
elif uf == "ES":
    capital_certa = "vitoria"
elif uf == "GO":
    capital_certa = "goiania"
elif uf == "MA":
    capital_certa = "sao luis"
elif uf == "MG":
    capital_certa = "belo horizonte"
elif uf == "MS":
    capital_certa = "campo grande"
elif uf == "MT":
    capital_certa = "cuiaba"
elif uf == "PA":
    capital_certa = "belem"
elif uf == "PB":
    capital_certa = "joao pessoa"
elif uf == "PE":
    capital_certa = "recife"
elif uf == "PI":
    capital_certa = "teresina"
elif uf == "PR":
    capital_certa = "curitiba"
elif uf == "RJ":
    capital_certa = "rio de janeiro"
elif uf == "RN":
    capital_certa = "natal"
elif uf == "RO":
    capital_certa = "porto velho"
elif uf == "RR":
    capital_certa = "boa vista"
elif uf == "RS":
    capital_certa = "porto alegre"
elif uf == "SC":
    capital_certa = "florianopolis"
elif uf == "SE":
    capital_certa = "aracaju"
elif uf == "SP":
    capital_certa = "sao paulo"
elif uf == "TO":
    capital_certa = "palmas"
else:
    print("ERRO")

print(f"Acertou? {capital.upper() == capital_certa.upper()}")