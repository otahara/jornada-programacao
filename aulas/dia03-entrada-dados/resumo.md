# Dia 3: Entrada de dados (`input`)

## ✅ O que aprendi neste dia

- `input("pergunta")` faz o programa perguntar e esperar o usuário digitar
- O `input` **sempre devolve texto**: digitar `5` entrega `"5"` (por isso `"5" + "5"` dá `"55"`)
- Converter com `int()` (inteiros: idade, ano, unidades) e `float()` (decimais: preço, nota, peso)
- O jeito comum é converter na chegada, `int(input(...))`, que se lê de dentro para fora
- `int` e `float` fazem conta juntos, e o resultado vira `float` (`10.0 + 5` → `15.0`)
- Decimal usa ponto: `float("3,5")` dá erro
- Três erros: `SyntaxError` (código mal escrito), `TypeError` (o culpado é o **tipo**: `5 + "5"`) e `ValueError` (o culpado é o **valor**: `int("2.5")`)
- O modo interativo (`python` no terminal, `>>>`) serve para testar coisas rápidas

---

## ⚠️ Pontos de atenção (onde eu tropecei)
- **TypeError × ValueError:** os exemplos eu acertava, mas as definições saíam trocadas. Truque: **o nome do erro diz quem é o culpado**. No *Type*Error o culpado é o **tipo** (a mistura: `5 + "5"`); no *Value*Error é o **valor** (o conteúdo: `int("2.5")`). Comparação do caixa eletrônico: moeda na entrada do cartão (Type) × cartão vencido (Value).
- O `input` **sempre** devolve texto, não "por padrão". Não existe outro jeito: a conversão é sempre trabalho meu.
- `int("2.5")`: o `"2.5"` ainda é **texto** com cara de decimal, e por isso o erro é de valor e não de tipo.
- **Saída exata:** um `:` a mais (`ex03`) e um "é o" faltando (`ex04`). Um caractere diferente já conta como saída errada.
- Decimal com **vírgula** (`float("3,5")`) dá ValueError. Os usuários brasileiros vão digitar assim.
- `float` sempre mostra casa decimal: `5 + 5.0` → `10.0`.

## `input`: o programa pergunta e escuta

```python
nome = input("Qual é o seu nome? ")
print("Olá,", nome)
```

- `input("pergunta")` mostra a pergunta, **para o programa** e espera o usuário digitar e apertar Enter.
- O que foi digitado vira o resultado, que normalmente é guardado numa variável.
- Deixe um **espaço depois do `?`** dentro das aspas, senão a resposta fica grudada na pergunta.

## Regra de ouro: `input` sempre devolve TEXTO

Mesmo que a pessoa digite `5`, chega `"5"` (texto). Por isso:

```python
numero = input("Digite um número: ")   # digitou 5
print(numero + numero)                  # 55  → texto + texto = cola
```

## Convertendo: `int()` e `float()`

| Função | Transforma | Exemplo | Use para |
|---|---|---|---|
| `int()` | texto → inteiro | `int("5")` → `5` | idade, ano, quantidade |
| `float()` | texto → decimal | `float("2.5")` → `2.5` · `float("5")` → `5.0` | preço, nota, altura |
| `str()` | número → texto | `str(5)` → `"5"` | juntar com texto usando `+` |

O jeito mais comum é **converter uma vez, logo na chegada**:

```python
numero = int(input("Digite um número: "))
```

Lê-se **de dentro para fora**: `input` devolve `"5"`, o `int` transforma em `5` e a variável guarda o `5`.

- Decimal usa **ponto**: `2.5` funciona, `2,5` dá erro.
- Um valor `float` sempre aparece com casa decimal: `5.0`, e não `5`.
- Às vezes aparece algo como `7.6499999999`. Isso não é erro, é como o computador guarda decimais (a formatação vem no Dia 7).

## Lendo erros

| Erro | Quando acontece | Exemplo |
|---|---|---|
| `TypeError` | o **tipo** não serve para a operação | `5 + "5"` |
| `ValueError` | o tipo serve, mas **aquele valor** não | `int("2.5")` |

A **última linha** do erro diz o tipo e o motivo. Comece a ler por ela.
