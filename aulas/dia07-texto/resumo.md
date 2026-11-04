# Dia 7: Trabalhando com texto

## ✅ O que aprendi neste dia

- **f-string:** um `f` antes das aspas e os valores entre chaves: `f"{nome} tem {idade} anos"`
- Na f-string, número não precisa de `str()`, e dá para fazer conta dentro das chaves: `{idade + 10}`
- Sem o `f`, as chaves aparecem na tela como texto comum: `Olá, {nome}!`
- `len(texto)` conta os caracteres, e o espaço também conta: `len("Ana Maria")` → `9`
- **Métodos de texto**, chamados com um ponto: `upper()` (maiúsculas), `lower()` (minúsculas), `capitalize()` (só a primeira letra do texto) e `title()` (a primeira letra de cada palavra)
- Esses métodos **não alteram a variável**: eles devolvem um texto novo. Para guardar, é preciso atribuir: `cidade = cidade.upper()`
- **Função comum × método:** `len(cidade)` tem o valor dentro dos parênteses; `cidade.upper()` tem o valor antes do ponto
- 🐞 **`AttributeError`:** aparece quando se pede a um valor algo que ele não tem, como `"casa".len()` ou `(5).upper()`
- ✨ Boa prática nova: **f-string em vez de juntar texto com `+`**

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- **Sem o `f`:** previ que `print("Produto: {produto}")` mostraria `Produto: caderno`, mas ele mostra `Produto: {produto}`. Não dá erro, por isso é fácil não perceber.
- **`palavra.len()` não é erro de sintaxe:** a escrita é válida, igual à de `palavra.upper()`. Por isso, o programa começa a rodar e só quebra quando procura `len` no texto e não encontra. Prova disso: a linha 1 chegou a perguntar `Palavra:`.
- **Tirar o erro não é consertar o programa:** troquei `nome.upper()` por `str(nome).upper()`, o erro sumiu, mas a saída foi `5` em vez de `BRUNO`. O conserto de verdade estava na linha 2, que apagava o nome.
- **Saída exata:** escrevi `Maiúscula:` e `Minúscula:` no lugar de `Maiúsculas:` e `Minúsculas:`.
- **Ler o enunciado até o fim:** digitei a linha de `=` à mão, quando o pedido era usar `*`; e, na anotação sobre f-string, primeiro respondi com `+` e `str()`.

---

## f-string: o jeito recomendado

```python
nome = "Ana"
idade = 30
altura = 1.65

print(f"{nome} tem {idade} anos e {altura}m de altura.")
```

```
Ana tem 30 anos e 1.65m de altura.
```

| Jeito | Código | Avaliação |
|---|---|---|
| `+` | `nome + " tem " + str(idade) + " anos"` | exige `str()` e espaços manuais; sem o `str()`, dá `TypeError` |
| vírgulas | `print(nome, "tem", idade, "anos")` | simples, mas sempre coloca um espaço entre as partes e só funciona dentro do `print` |
| **f-string** | `f"{nome} tem {idade} anos"` | ✅ **recomendado:** dá para ler a frase como ela vai aparecer |

## `len` e os métodos de texto

```python
nome = "ana maria"

print(len(nome))
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())
print(nome)
```

```
9
ANA MARIA
ana maria
Ana maria
Ana Maria
ana maria
```

A última linha mostra que `nome` continua igual: nenhum método alterou a variável.

## 🐞 `AttributeError`

| Programa | Mensagem (última linha) | Conserto |
|---|---|---|
| `cidade.uper()` | `'str' object has no attribute 'uper'. Did you mean '.upper' instead of '.uper'?` | corrigir o nome: `cidade.upper()` |
| `palavra.len()` | `'str' object has no attribute 'len'` | `len` é função comum: `len(palavra)` |
| `nome = len(nome)` seguido de `nome.upper()` | `'int' object has no attribute 'upper'` | `nome` virou número na linha 2: não sobrescrever a variável |

Como ler a mensagem: `'str' object` é um valor do tipo `str`, e `has no attribute 'len'` quer dizer que esse valor não tem nada chamado `len`.

## ✨ Boas práticas que apareceram

- **Variável com nome que diz o que ela guarda:** `separador = "=" * 30`, e não `espaco = "="`.
- **Mudar em um lugar só:** com `separador`, trocar o tamanho das três linhas do cartão exige alterar uma única linha.
- **Código que nada usa sai do programa:** no `erros/ex03.py`, a linha `len(nome)` não servia para a saída pedida, e o recomendado foi excluí-la. Se a quantidade fosse necessária, ela iria para outra variável, como `quantidade_caracteres = len(nome)`.

## Exercícios do dia

| Arquivo | O que faz |
|---|---|
| [aquecimento.py](aquecimento.py) | juntar texto e número com `+` e `str()` |
| [exemplo.py](exemplo.py) | a mesma frase com f-string |
| [exemplo2.py](exemplo2.py) | `len`, `upper`, `lower` e testes com `capitalize` |
| [exemplo3.py](exemplo3.py) | teste de `capitalize` × `title` |
| [ex01.py](ex01.py) | nome e idade, com conta dentro das chaves |
| [ex02.py](ex02.py) | um nome em maiúsculas e minúsculas, com a quantidade de caracteres |
| [ex03.py](ex03.py) | 🎯 cartão de apresentação (entrega do dia) |
| [erros/ex01.py](erros/ex01.py) | 🐞 método com nome errado (já consertado) |
| [erros/ex02.py](erros/ex02.py) | 🐞 `len` escrito como método (já consertado) |
| [erros/ex03.py](erros/ex03.py) | 🐞 variável de texto que virou número (já consertado) |

---

## 🧑‍🏫 Relatório do professor

Registro das perguntas do dia, das minhas respostas (do jeito que escrevi, só com os erros de digitação corrigidos) e da correção.

### Revisão (sem consulta)

**1. Cartelas de ovos.** Com `ovos = 50`, o que mostram `print(ovos // 12)` e `print(ovos % 12)`?

> *Minha resposta:* "como 50/12 é 4.166666666, provavelmente 50 // 12 vai ser 4 e a sobra é 0.1666666, que nessa operação ficaria 2"

✅ **Certa.** `4` e `2`. Sem calculadora, é mais rápido assim: `4 × 12 = 48`, e de 48 até 50 sobram 2.

**2. Dividindo a conta.** Com `por_pessoa = 20 / 4`, o que mostram `print(por_pessoa)` e `print(type(por_pessoa))`?

> *Minha resposta:* "print(por_pessoa) aparece 5.0; print(type(por_pessoa)) aparece float"

⚠️ **Uma linha certa e outra quase.** O tipo é mesmo `float`, mas a saída exata é `<class 'float'>`.

**3. Git.** Rodei `git add .` e `git commit` dentro de `aulas/dia06-tipos-operadores`, e o `README.md`, que fica na raiz, ficou de fora. Por quê? Como consertar?

> *Minha resposta:* "o README.md ficou de fora porque eu dei os comandos na pasta \dia06-tipos-operadores e o README.md fica na pasta \algoritmo; para corrigir, eu preciso dar cd .. duas vezes até chegar nessa pasta e dar git add . novamente"

⚠️ **O motivo está certo, mas o conserto ficou incompleto.** O `add` só separa o arquivo: faltaram um novo `git commit` e o `git push`.

### Aquecimento

Com `nome`, `idade` e `altura`, mostrar `Ana tem 30 anos e 1.65 m de altura.` em um único `print`, usando só `+`.

✅ **Saída exata**, com 5 `+` e 2 `str()`. **Fui além:** deixei comentado o jeito com vírgulas.

### Parte 1: f-string

| Código | Minha previsão | Correção |
|---|---|---|
| `print(f"{quantidade} x {produto}")` | `3 x caderno` | ✅ |
| `print(f"Total: {preco * quantidade}")` | `Total: 37.5` | ✅ |
| `print("Produto: {produto}")` | `Produto: caderno` | ❌ sem o `f`, sai `Produto: {produto}` |

**Termo:** eu não conhecia f-string.

**`ex01`** ✅ saída exata, com uma f-string e a conta dentro das chaves. **Fui além:** testei `{altura}m` no `exemplo.py`.

### Parte 2: `len`, `upper` e `lower`

| Código | Minha previsão | Correção |
|---|---|---|
| `print(len(nome))` | "9: Ana Maria tem 8 letras, mas tem 1 espaço" | ✅ |
| `print(nome.upper())` | `ANA MARIA` | ✅ |
| `print(f"{nome.lower()} tem {len(nome)} caracteres")` | `ana maria tem 9 caracteres` | ✅ |

**Termo:** eu não sabia o que é método.

**`ex02`** ⚠️ → ✅ Primeiro saiu `Maiúscula:` e `Minúscula:`, sem o `s` pedido. Consertei.

**Fui além:** lembrei que existia o `capitalize()` e testei por conta própria, e depois testei o `title()` com `"ana maria"`.

### Parte 3: 🐞 `AttributeError`

**`erros/ex01`** (`cidade.uper()`)

> *Minha resposta:* "o programa quebrou na linha 2; o problema está na linha 2: não existe o método uper(), e sim upper(); substituí uper() por upper()"

✅ **Certa.**

**`erros/ex02`** (`palavra.len()`)

> *Minha resposta:* "o programa quebrou na linha 2; o problema é que não se usa o método len() dessa forma; na minha cabeça seria um erro de sintaxe, mas não é, né, hahaha, então eu não consigo entender de maneira teórica esse erro; substituí palavra.len() por len(palavra)"

✅ **Certa na linha e no conserto.** A escrita é válida, igual à de `palavra.upper()`, e por isso a linha 1 rodou. Só que `len` é uma função comum, não um método.

**`erros/ex03`** (`nome = len(nome)` seguido de `nome.upper()`)

> *Minha resposta:* "o programa quebrou na linha 3; o problema vem da linha 2, que agora a variável nome recebe um valor do tipo inteiro, que é o número de caracteres; na minha cabeça, o jeito mais simples de resolver é substituindo print(nome.upper()) por print(str(nome).upper())"

⚠️ → ✅ **O diagnóstico estava certo, mas o conserto não.** O erro sumiu e a saída foi `5`, não `BRUNO`. Excluí a linha 2, e a saída ficou certa. A dica do professor ("o que precisa mudar nela") dava a entender que a linha 2 tinha que continuar. Também daria para mantê-la, guardando a quantidade em outra variável, mas nada usaria esse valor.

**Termos:** eu não sabia o que são objeto e atributo.

### Entrega: `ex03`, o cartão de apresentação

⚠️ → ✅ A saída estava exata desde a primeira versão, inclusive digitando `ANA MARIA`, mas a linha de `=` tinha sido digitada à mão. Passei para `espaco*30` e, com os ✨ da correção (espaço ao redor do `*` e nome que diz o que a variável guarda), cheguei a `separador = "=" * 30`.
