# Dia 5 · Bloco 1: `SyntaxError`

## ✅ O que aprendi neste bloco

- `SyntaxError` aparece quando o código está **mal escrito**: uma aspa, um parêntese ou uma vírgula faltando
- Com `SyntaxError`, **nenhuma linha roda**, nem as que estão certas. O Python lê o arquivo inteiro antes de começar e, se a escrita estiver errada, nem começa
- A mensagem mostra a **linha**, o trecho do código e uma setinha `^` apontando o lugar do problema
- Nos casos deste bloco, a linha que quebrou e a linha do problema eram a mesma

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- Nenhum tropeço neste bloco: achei a linha e consertei os 3 exercícios de primeira.

## Os 3 casos

| Exercício | Código quebrado | Mensagem (última linha) | Conserto |
|---|---|---|---|
| [ex01](ex01.py) | `cidade = "Recife` | `SyntaxError: unterminated string literal (detected at line 2)` | fechar a aspa: `"Recife"` |
| [ex02](ex02.py) | `preco = float(input("Preço: ")` | `SyntaxError: '(' was never closed` | fechar o parêntese: `float(input("Preço: "))` |
| [ex03](ex03.py) | `print("Gols:" gols)` | `SyntaxError: invalid syntax. Perhaps you forgot a comma?` | pôr a vírgula: `print("Gols:", gols)` |

Tradução rápida das mensagens:

- *unterminated string literal*: texto (entre aspas) que não foi fechado
- *'(' was never closed*: um `(` que nunca foi fechado
- *Perhaps you forgot a comma?*: "talvez você tenha esquecido uma vírgula?"

## Repare: a linha 1 não apareceu

```python
print("Começando o programa")   # linha certinha...
cidade = "Recife                # ...mas o erro está aqui
print("Eu moro em", cidade)
```

Ao rodar, o terminal mostra **só o erro**. O `Começando o programa` não aparece.
Compare com um erro que acontece **durante** a execução (como somar texto com número): nesse caso, as linhas anteriores rodam normalmente e o programa só para quando chega na linha com problema.
