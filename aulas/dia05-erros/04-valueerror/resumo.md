# Dia 5 · Bloco 4: `ValueError`

## ✅ O que aprendi neste bloco

- `ValueError` aparece quando o **tipo é o esperado, mas o conteúdo não serve** para aquela operação
- O caso mais comum: converter um texto que **não tem cara de número** com `int()` ou `float()`
- A mensagem mostra o valor problemático entre aspas:
  - `invalid literal for int() with base 10: 'dois'`
  - `could not convert string to float: '46,50'`
- `int(7.5)` funciona (corta a parte decimal e dá `7`), mas `int("7.5")` **não**: o texto `"7.5"` não é um inteiro escrito
- Decimal no Python usa **ponto**, não vírgula

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- Nenhum tropeço neste bloco: os 3 saíram certos de primeira.
- Lembrete: o `input` entrega **texto**. Digitar `7.5` entrega `"7.5"` (um `str` com cara de decimal), não um `float`.

## Os 3 casos

| Exercício | Código quebrado | Quebra na | Problema na | Conserto |
|---|---|---|---|---|
| [ex01](ex01.py) | `int("dois")` | linha 2 | linha 2 | `int("2")` |
| [ex02](ex02.py) | `valor = "46,50"` … `float(valor)` | linha 4 | linha 2 | `"46.50"` (ponto) |
| [ex03](ex03.py) | `int(input(...))`, digitando `7.5` | linha 2 | linha 2 | `float(input(...))` |

## Repare no `ex03`

O código parece certo, e funciona se a pessoa digitar `7`. Ele só quebra com `7.5`. Ou seja, um `ValueError` pode depender **do que o usuário digita**. Por isso a conversão precisa combinar com o dado: nota pode ter casa decimal, então é `float`.
