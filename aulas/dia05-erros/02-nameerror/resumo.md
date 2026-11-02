# Dia 5 · Bloco 2: `NameError`

## ✅ O que aprendi neste bloco

- `NameError` aparece quando o código usa um **nome que o Python não conhece**: uma variável que ainda não existe ou um nome digitado errado
- A mensagem diz exatamente qual nome é o problema: `name 'preco' is not defined`
- Às vezes ela ainda sugere o nome certo: `name 'idad' is not defined. Did you mean: 'idade'?`
- Diferente do `SyntaxError`, aqui o programa **começa a rodar**: as linhas antes do erro aparecem na tela normalmente
- O Python lê o código **de cima para baixo**: uma variável só existe depois da linha que a cria

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- Texto **sem aspas** vira nome de variável. `cidade = Recife` faz o Python procurar uma variável chamada `Recife`.
- No `ex02` não havia uma linha "escrita errada": o problema era a **ordem** das linhas. Fiquei na dúvida sobre como dizer "em qual linha está o problema" quando a resposta é "a linha certa está no lugar errado".

## Os 3 casos

| Caso | Código quebrado | Mensagem (última linha) | Conserto |
|---|---|---|---|
| nome digitado errado | `idade = 30` … `print(idad)` | `NameError: name 'idad' is not defined. Did you mean: 'idade'?` | corrigir para `idade` |
| [ex01](ex01.py): faltaram aspas | `cidade = Recife` | `NameError: name 'Recife' is not defined` | `cidade = "Recife"` |
| [ex02](ex02.py): usada antes de existir | `total = preco * 2` antes de `preco = 10` | `NameError: name 'preco' is not defined` | criar `preco` **antes** de usar |

## A ordem importa

```python
print("Bem-vindo à loja")
total = preco * 2      # linha 2: quebra aqui, porque preco ainda não existe
preco = 10             # linha 3: a variável só nasce aqui
print("Total:", total)
```

O erro aponta a linha 2, mas o conserto é **trocar a ordem**: `preco = 10` precisa vir antes de `total = preco * 2`.
