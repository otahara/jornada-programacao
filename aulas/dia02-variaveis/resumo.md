# Dia 2: Variáveis

## ✅ O que aprendi neste dia
- `=` é **"recebe"**, e o lado direito é calculado primeiro
- A variável guarda o **resultado**, e não a fórmula
- Regras de nomes e o **snake_case**
- **Teste de mesa:** o que é **e para que serve**
- A **troca com variável auxiliar** (*swap*), um algoritmo clássico, e cheguei nele sozinho
- A lição extra: **saída certa ≠ programa certo**

## ⚠️ Pontos de atenção (onde eu tropecei)
- **A variável não se recalcula sozinha:** mudei `ano_atual` e `anos_formado` continuou 8. Para atualizar, a conta precisa rodar de novo.
- **snake_case é convenção, não regra:** uma vez esqueci essa parte. `salarioMensal` funciona, só não é o padrão do Python.
- **Teste de mesa:** errei anotações intermediárias no 1º. O segredo é anotar **toda** linha, mesmo as que parecem óbvias.
- **Saída certa ≠ estado certo:** no `ex03` mostrei `copo3` na tela em vez de trocar o `copo2` de verdade.
- **Swap:** a `aux` guarda o valor da variável que vai ser sobrescrita **primeiro**. Os dois jeitos (`aux = cor_a` ou `aux = cor_b`) funcionam se a ordem bater.

## O que é uma variável
- É um **nome** que aponta para um **valor** guardado na memória, como uma etiqueta colada numa caixa.
```python
ano_atual = 2026
nome = "Gabriel"
print("Olá,", nome)   # Olá, Gabriel
```

## O `=` é "recebe", e não "igual"
- `ano_atual = 2026` se lê **"ano_atual recebe 2026"**
- **Regra de ouro:** o Python calcula **primeiro o lado direito** e **depois** guarda o resultado no nome da esquerda.
- Do lado esquerdo só pode ficar um nome: `2026 = ano_atual` dá erro.

## Reatribuição
- Uma variável guarda **um valor por vez**. Um valor novo **substitui** o antigo.
```python
ano_atual = 2026
ano_atual = 2027
print(ano_atual)   # 2027
```
- `a = a + b` faz sentido: o Python calcula `a + b` com os valores **atuais** e só depois guarda em `a`.

## A variável guarda o resultado, e não a fórmula
```python
ano_atual = 2026
ano_formatura = 2018
anos_formado = ano_atual - ano_formatura   # guarda 8
ano_atual = 2030
print(anos_formado)   # continua 8, porque a conta não roda de novo sozinha
```
- Para atualizar, é preciso executar a conta de novo.
- **DRY** (*Don't Repeat Yourself*): guarde o valor num lugar só e corrija uma vez só.

## Regras de nomes
| Regra | ✅ | ❌ |
|---|---|---|
| Só letras, números e `_` | `ano_atual`, `_total` | `ano-atual` (o `-` é subtração) |
| Não pode começar com número | `nota1` | `1nota` |
| Sem espaço | `nome_completo` | `nome completo` |
| Não pode ser palavra reservada | `classe` | `class`, `if`, `for` |

**Convenções** (não dão erro, mas todo mundo segue):
- *snake_case*: minúsculas com `_` (`salario_mensal`). O *camelCase* (`salarioMensal`) é do Java/JS.
- Sem acento.
- Nomes que explicam o conteúdo.
- `idade` e `Idade` são variáveis **diferentes** (*case-sensitive*).

## Teste de mesa
Simular o código no papel, **linha por linha**, anotando o valor de cada variável a cada passo.
```python
a = 5
b = 3
a = a + b
b = a - b
print(a, b)
```
| Linha | `a` | `b` | Saída |
|---|---|---|---|
| 1 | 5 | – | |
| 2 | 5 | 3 | |
| 3 | 8 | 3 | |
| 4 | 8 | 5 | |
| 5 | 8 | 5 | `8 5` |

- Na linha 4, o `a` já vale 8. O valor depende de **em que ponto do código** você está.
- Vai ser essencial na Semana 3 (repetição), quando as mesmas linhas rodam várias vezes.

**Para que serve:** rodar o código mostra **o resultado**. O teste de mesa mostra **o caminho** até ele.
- **Achar erro:** a tabela mostra a linha exata em que um valor se perdeu.
- **Entender código** que você não escreveu, ou quando não dá para rodar (prova, entrevista).
- **Laços:** as mesmas linhas rodam várias vezes, e a tabela mostra volta por volta.

## Troca de valores (*swap*)
Sem uma variável auxiliar, um dos valores se perde:
```python
copo1 = copo2   # o "suco" sumiu: ninguém mais guarda ele
copo2 = copo1   # resultado: água água
```
Com um "terceiro copo" (costuma se chamar `aux` ou `temp`):
```python
aux = copo1     # guarda o suco
copo1 = copo2   # copo1 recebe a água
copo2 = aux     # copo2 recebe o suco guardado
```

## Saída certa ≠ programa certo
- Mostrar `água suco` na tela não prova que os copos trocaram. Confira o **valor guardado** nas variáveis, porque ele vai ser usado depois.
