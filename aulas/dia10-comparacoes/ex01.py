META_DE_APROVEITAMENTO = 70

questoes_feitas = int(input("Questões feitas: "))
questoes_acertadas = int(input("Questões acertadas: "))

aproveitamento = questoes_acertadas / questoes_feitas * 100

print(f"Aproveitamento: {aproveitamento:.1f}%")

print(f"Atingiu a meta de {META_DE_APROVEITAMENTO}%? {aproveitamento >= META_DE_APROVEITAMENTO}")
print(f"Errou alguma? {questoes_acertadas != questoes_feitas}")