balas = int(input("Quantas balas? "))
criancas = int(input("Quantas crianças? "))

balas_por_crianca = balas // criancas
resto_balas = balas % criancas

print("Cada criança recebe", balas_por_crianca, "balas")
print("Sobram", resto_balas, "balas")