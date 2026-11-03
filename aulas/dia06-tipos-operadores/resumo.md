# Dia 6: Tipos e operadores aritméticos

## ✅ O que aprendi neste dia

- Os quatro tipos básicos: `int` (inteiro), `float` (com casas decimais), `str` (texto) e `bool` (`True` ou `False`)
- `type()` mostra o tipo de um valor: `type(10 / 2)` → `<class 'float'>`
- A divisão com `/` **sempre** devolve `float`, mesmo quando a conta é exata: `10 / 2` → `5.0`
- `//` (divisão inteira) e `%` (resto) andam juntos: 135 minutos são `135 // 60` = 2 horas e `135 % 60` = 15 minutos
- `% 2` diz se um número é par (resto `0`) ou ímpar (resto `1`)
- `**` é potência: `2 ** 3` = 2 × 2 × 2 = `8`
- Se um dos lados da conta é `float`, o resultado também é: `7.0 // 2` → `3.0`
- `"ha" * 3` repete o texto: `hahaha`
- `True` (sem aspas) é `bool`; `"True"` (com aspas) é `str`
- ✨ Boa prática nova (PEP 8): **um espaço de cada lado do operador** (`total = a + b`)

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- **`5.0` e não `5`:** previ `10 / 2` como `5`. A divisão com `/` sempre dá `float`. Para um resultado inteiro, use `//`.
- **`3.5` e não `3.50`:** o Python não mostra zeros sobrando no fim do número. Isso conta para a saída exata.
- **Saída exata na calculadora:** saiu `17 / 5 - 3.4` no lugar de `17 / 5 = 3.4`. O programa rodou sem erro, mas a saída estava errada: só quem confere com atenção percebe.
- **`=` no Python é "recebe", não "igual":** `200 // 60 = 3` serve como anotação de matemática, mas como código dá `SyntaxError`. O certo é `horas = minutos // 60`.
- **Nomes:** se um nome precisa de comentário para ser entendido (`primeiro_num  # num é número`), use o nome completo (`primeiro_numero`).

---

## Os quatro tipos

| Tipo | Exemplos | Para que serve |
|---|---|---|
| `int` | `10`, `-3`, `0` | quantidades inteiras: idade, pessoas, balas |
| `float` | `2.5`, `5.0` | valores com casas decimais: preço, peso, área |
| `str` | `"Ana"`, `"True"`, `"30"` | texto (tudo o que está **entre aspas**) |
| `bool` | `True`, `False` | verdadeiro ou falso; é o que faz o programa **decidir** (`if`, a partir do Dia 10) |

O `bool` se escreve com letra **maiúscula** e **sem aspas**. Curiosidade: por dentro, o Python trata `True` como `1` e `False` como `0` (`True + True` dá `2`). Na prática, use sempre `True` e `False`, que são muito mais claros.

## Os operadores aritméticos

| Operador | Nome | Exemplo | Resultado |
|---|---|---|---|
| `+` | soma | `17 + 5` | `22` |
| `-` | subtração | `17 - 5` | `12` |
| `*` | multiplicação | `17 * 5` | `85` |
| `/` | divisão | `17 / 5` | `3.4` (sempre `float`) |
| `//` | divisão inteira | `17 // 5` | `3` (joga fora a parte depois da vírgula) |
| `%` | resto | `17 % 5` | `2` (o que sobra) |
| `**` | potência | `17 ** 2` | `289` |

## `//` e `%`: minutos em horas

```python
minutos = 135

horas = minutos // 60
resto = minutos % 60

print(minutos, "minutos são", horas, "hora(s) e", resto, "minuto(s)")
```

```
135 minutos são 2 hora(s) e 15 minuto(s)
```

60 cabe **2 vezes inteiras** em 135 (`//`) e **sobram 15** (`%`).

## ✨ Boa prática: espaço ao redor dos operadores

```python
total = preco * quantidade    # ✅ recomendado (PEP 8)
total=preco*quantidade        # ❌ funciona, mas é difícil de ler
```

## Variável ou conta direto no `print`?

Os dois jeitos estão certos:

```python
soma = primeiro_numero + segundo_numero
print(primeiro_numero, "+", segundo_numero, "=", soma)
```

```python
print(primeiro_numero, "+", segundo_numero, "=", primeiro_numero + segundo_numero)
```

Use **variável** quando o resultado for usado de novo ou quando o nome ajudar a entender. Se o resultado aparece uma vez só e a conta é simples, fazer direto no `print` também serve.

## Divisão por zero

Na calculadora, digitar `0` como segundo número quebra o programa na **primeira** divisão (`/`), com `ZeroDivisionError`. Como os `print` vêm depois das contas, nada aparece na tela. Impedir isso pede uma decisão ("se for zero, avise"), que é o assunto da Semana 2.

## Exercícios do dia

| Arquivo | O que faz |
|---|---|
| [aquecimento.py](aquecimento.py) | prever `10 + 2`, `10 * 2`, `10 / 2` e `7 / 2` |
| [exemplo.py](exemplo.py) | minutos → horas e minutos, com `//` e `%` |
| [ex01.py](ex01.py) | dividir balas entre crianças (`//` e `%`) |
| [ex02.py](ex02.py) | área do quadrado (`**` com `float`) |
| [ex03.py](ex03.py) | 🎯 calculadora com as 7 operações (entrega do dia) |

---

## 🧑‍🏫 Relatório do professor

Registro das perguntas do dia, das minhas respostas (do jeito que escrevi, só com os erros de digitação corrigidos) e da correção.

### Revisão (sem consulta)

**1. Teste de mesa.** Depois de `preco_antigo = 50`, `preco_novo = preco_antigo` e `preco_antigo = 65`, o que mostra `print(preco_novo)`?

> *Minha resposta:* "o print(preco_novo) ainda vai retornar 50, pois não fiz alteração na variável preco_novo"

✅ **Certa.** `preco_novo = preco_antigo` copia o valor uma vez só. No Dia 5 eu tinha errado esse tipo de pergunta. ✨ Variável não "retorna": ela **guarda** ou **recebe** um valor. "Retornar" tem outro sentido em Python (o `return`, no Dia 29).

**2. Prever o erro.** `peso = int(input("Seu peso em kg: "))`, digitando `72.5`. Quebra? Qual erro, em que linha? Como consertar?

> *Minha resposta:* "Sim o programa quebra, pois o valor "72.5" não é um valor que a função int() aceita. A mudança que eu deveria fazer é usar float() ao invés de int()"

✅ **Certa, faltou um pedaço:** o nome do erro e a linha (**ValueError, linha 1**). O motivo e o conserto estão certos.

**3. Git.** Depois de `git add .` e `git commit`, o arquivo não aparece no GitHub. O que faltou?

> *Minha resposta:* "Faltou o git push, o ritual está prontinho (mesmo você não tendo incluido o git status antes de git add .)"

✅ **Certa.** O `commit` salva só no computador; quem leva para o GitHub é o `push`. E a observação também estava certa: o ritual começa com `git status`.

### Aquecimento

Prever sem rodar: `10 + 2`, `10 * 2`, `10 / 2` e `7 / 2`.

> *Minha resposta:* "12, 20, 5, 3.50"

⚠️ **As contas certas, o formato não.** Saiu `5.0` (a divisão com `/` sempre dá `float`) e `3.5` (sem zero sobrando). No `>>>`, descobri a regra com `type(10 + 2)` → `<class 'int'>` e `type(10 / 2)` → `<class 'float'>`.

**Termo:** eu já sabia o que é um operador (`+` soma, `*` multiplicação, `/` divisão, `-` subtração).

### Parte 1: `//`, `%` e `**`

Prever o resultado de `135 // 60` e `135 % 60`.

> *Minha resposta:* "60 cabe 2x inteira em 135 e sobra 15 minutos, total de 2h15"

✅ **Certa.** Faltou prever a segunda linha (`2 ** 3` = `8`). **Fui além:** transformei o exemplo num programa com `int(input(...))`, sem mudar a saída pedida.

### Parte 2: tipos e mais operadores

| Código | Minha previsão | Correção |
|---|---|---|
| `7 // 2` | `3`, `int` | ✅ |
| `7 % 2` | `1`, `int` | ✅ |
| `10 % 2` | `0`, `int` | ✅ |
| `7.0 // 2` | `3.0`, `float` | ✅ |
| `2 ** 10` | `1024`, `int` | ✅ |
| `True` | "o resultado é True?", `bool` | ✅ |
| `"ha" * 3` | `"hahaha"`, `str` | ✅ |

✅ **7 de 7.** Lembrei sozinho que o `bool` tem relação com `1` e `0`, e está certo: `True + True` dá `2`.

### Exercícios

- **`ex01`** ✅ saída exata. ✨ O nome `balar_criancas` tinha erro de digitação e era pouco claro: `balas_por_crianca` diz melhor o que guarda.
- **`ex02`** ✅ saída exata, com `float` e `**`. Usei comentários por conta própria. ✨ PEP 8: um espaço depois do `#` e dois antes, quando o comentário fica na mesma linha do código.
- **`ex03`** ⚠️ → ✅ Primeiro saiu `17 / 5 - 3.4` (um `-` no lugar do `=`). Consertei, e também troquei `primeiro_num` por `primeiro_numero`. Usei variáveis para cada resultado, com nomes claros.

### Desafio: e se o segundo número for 0?

> *Minha resposta:* "Nesse meu programa já acusa erro na linha 7, já quebra logo na linha 7"

✅ **Certa.** A linha 7 é a primeira divisão (`/`), e o programa para com `ZeroDivisionError`.
