# Plano em 4 partes, feito para o estacionamento com tolerância (ex01.py do Dia 14).
# O plano vem antes do código, todo em português, sem código e sem fazer as contas.

# Dados:
#   digitados: os minutos e se tem cartão de cliente (s/n).
#   fixos (viram constantes): R$ 8,00 a primeira hora, R$ 3,00 as demais,
#   30 minutos de tolerância, R$ 5,00 de desconto a partir de 3 horas com cartão.

# Contas:
#   horas cobradas = horas inteiras, mais 1 se sobrar algum minuto.
#   valor = preço da primeira hora + preço das demais × (horas cobradas − 1).
#   valor com desconto = valor − desconto.

# Decisões:
#   1. minutos negativos → "Tempo inválido".
#   2. até 30 minutos → grátis.
#   3. sobrou algum minuto → soma 1 hora.
#   4. 3 horas ou mais e tem cartão → aplica o desconto.

# Alguma decisão depende de outra?
#   A 2 só acontece se a 1 deixar passar, e a 3 e a 4 só se a 2 deixar passar:
#   ficam dentro do else. A pergunta do cartão também, porque só serve para quem paga.
#   A 3 e a 4 não se excluem: são if separados. A 4 vem depois da 3,
#   porque usa as horas já cobradas.
