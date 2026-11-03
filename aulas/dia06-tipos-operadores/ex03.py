primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero
divisao_inteira = primeiro_numero // segundo_numero
resto = primeiro_numero % segundo_numero
potencia = primeiro_numero ** segundo_numero

print(primeiro_numero, "+", segundo_numero, "=", soma)
print(primeiro_numero, "-", segundo_numero, "=", subtracao)
print(primeiro_numero, "*", segundo_numero, "=", multiplicacao)
print(primeiro_numero, "/", segundo_numero, "=", divisao)
print(primeiro_numero, "//", segundo_numero, "=", divisao_inteira)
print(primeiro_numero, "%", segundo_numero, "=", resto)
print(primeiro_numero, "**", segundo_numero, "=", potencia)