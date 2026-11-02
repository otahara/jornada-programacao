# Dia 5: Lendo e corrigindo erros

Um dia só de prática: programas curtos **quebrados de propósito** para rodar, ler a mensagem de erro e consertar. Nada de decorar definições. Para cada programa, três perguntas:

1. Em qual linha **quebrou**?
2. Em qual linha está o **problema de verdade**?
3. Qual é o **conserto**?

## ✅ O que aprendi neste dia

- Ler a mensagem de erro **de baixo para cima**: a última linha diz o nome do erro e o motivo; acima dela vêm o arquivo, a linha e o trecho do código
- O bloco que começa com `Traceback (most recent call last):` é o relatório do erro ("o mais recente por último")
- A linha que **quebra** nem sempre é a linha do **problema**: muitas vezes o dado ruim nasceu antes (num `input` sem conversão, numa variável com o valor errado)
- Com `SyntaxError` **nada roda**; com os outros erros, as linhas anteriores rodam normalmente
- **Rodar sem erro não quer dizer resultado certo** (`8 / 2.5` pessoas roda, mas não faz sentido)
- Os 5 erros do dia, classificados sozinho no teste final (5 de 5)

## ⚠️ Pontos de atenção (onde eu tropecei)

- **"Em qual linha está o problema?"** quando a resposta é "a linha certa está no lugar errado" (variável usada antes de ser criada): o problema é a **ordem**.
- **Previsão da linha que quebra:** é a linha da operação impossível (a soma, a divisão, a conversão).
- O `input` entrega **texto**: digitar `7.5` entrega `"7.5"`, não um `float`.
- **A conversão precisa combinar com o dado:** peso e nota podem ter decimal, então é `float`.

## Os blocos

| Bloco | Erro | Exemplo de mensagem | Resumo |
|---|---|---|---|
| 1 | `SyntaxError` | `unterminated string literal` | [01-syntaxerror](01-syntaxerror/resumo.md) |
| 2 | `NameError` | `name 'preco' is not defined` | [02-nameerror](02-nameerror/resumo.md) |
| 3 | `TypeError` | `can only concatenate str (not "int") to str` | [03-typeerror](03-typeerror/resumo.md) |
| 4 | `ValueError` | `invalid literal for int() with base 10: 'dois'` | [04-valueerror](04-valueerror/resumo.md) |
| 5 | `ZeroDivisionError` | `division by zero` | [05-zerodivisionerror](05-zerodivisionerror/resumo.md) |
| 6 | todos misturados | prever o erro antes de rodar | [06-misturados](06-misturados/resumo.md) |

## O que cada erro está dizendo (na prática)

| Erro | O que aconteceu no código | Onde costuma estar o conserto |
|---|---|---|
| `SyntaxError` | escrita errada: aspa, parêntese ou vírgula faltando | na própria linha apontada (a setinha `^` ajuda) |
| `NameError` | usou um nome que o Python não conhece | nome digitado errado, aspas faltando ou variável criada depois |
| `TypeError` | misturou tipos que não combinam (`str` + `int`) | onde o dado entrou sem conversão (`input`) |
| `ValueError` | o tipo é o esperado, mas o conteúdo não serve (`int("dois")`) | o valor ou a conversão escolhida (`int` × `float`) |
| `ZeroDivisionError` | dividiu por zero | onde o zero entrou (variável, conta ou usuário) |

## O aquecimento: onde tudo começou

```python
nome = input("Seu nome: ")
idade = input("Sua idade: ")
print("Olá,", nome)
daqui_10 = idade + 10        # linha 4: quebra aqui (TypeError)
print("Em 10 anos você terá", daqui_10)
```

O `Olá, Ana` aparece e o programa só para na linha 4. Mas o conserto é na linha 2: `int(input("Sua idade: "))`.

## Erros que vêm depois

Outros erros entram no cronograma no dia em que podem acontecer (🐞), cada um com uma pasta `erros/`: `AttributeError` (Dia 7), `IndentationError` (Dia 11), `IndexError` (Dia 25) e `KeyError` (Dia 34).
