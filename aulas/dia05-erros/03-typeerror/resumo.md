# Dia 5 · Bloco 3: `TypeError`

## ✅ O que aprendi neste bloco

- `TypeError` aparece quando uma operação junta **tipos que não combinam**, como texto (`str`) com número (`int`)
- Os valores em si podem estar certos (`"Você tem "`, `30`, `" anos"`). O problema é **misturar os tipos** na mesma operação
- A mensagem diz quais tipos se misturaram e em qual operação:
  - `can only concatenate str (not "int") to str`: só dá para juntar texto com texto
  - `unsupported operand type(s) for -: 'str' and 'int'`: o `-` não funciona entre texto e número
- A linha que quebra nem sempre é a linha do problema. Quando o dado vem de um `input`, o problema costuma estar **onde o valor entrou** sem conversão

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- Achei a linha e consertei de primeira, mas fiquei na dúvida sobre **por que** é `TypeError`. O que respondeu a dúvida: os valores estão certos, mas os **tipos** (`str` e `int`) não podem ser misturados naquela operação.

## Os 2 casos

| Exercício | Código quebrado | Quebra na | Problema na | Conserto |
|---|---|---|---|---|
| [ex01](ex01.py) | `idade = 30` … `"Você tem " + idade + " anos"` | linha 3 | linha 3 | `str(idade)` **ou** separar com vírgulas no `print` |
| [ex02](ex02.py) | `estoque = input(...)` … `estoque - vendidas` | linha 4 | linha 2 | `estoque = int(input(...))` |

## Dois jeitos de consertar o `ex01`

```python
idade = 30
print("Você tem " + str(idade) + " anos")   # converte para texto e junta com +
print("Você tem", idade, "anos")            # a vírgula aceita tipos diferentes
```

O `+` entre textos **gruda** (então os espaços precisam estar dentro das aspas); a vírgula do `print` põe um espaço sozinha.
