# Dia 5 · Bloco 7: Traceback

## ✅ O que aprendi neste bloco

- **Traceback** é a mensagem de erro inteira que aparece quando o programa **quebra no meio da execução**
- Ele tem 4 partes: o cabeçalho, o arquivo e a linha (`File ..., line N`), o trecho do código daquela linha e, por último, o **nome do erro e o motivo**
- `most recent call last` = "a chamada mais recente fica por último". Por isso se lê **de baixo para cima**
- `in <module>` quer dizer que o erro aconteceu no corpo principal do arquivo (um arquivo `.py` é um **módulo**)
- Quando o código passa por uma função, o Traceback mostra **uma camada para cada chamada**: a de cima é onde o meu programa principal chamou a função, e a de baixo é onde o erro aconteceu de fato
- O Traceback não serve só para dar o nome do erro: ele aponta a **linha exata**, e assim dá para conferir em vez de deduzir

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- No `ex01` expliquei o motivo como "texto somado com número", mas o Traceback apontava a **linha 2**, a da conversão `int("vinte")`. A soma estava na linha 3, que nem chegou a rodar. **Ler a linha que o Traceback aponta antes de concluir.**
- Não sabia o que era **módulo** nem **chamada de função**.

## As 4 partes

```
Traceback (most recent call last):                             ← cabeçalho: o programa começou e quebrou no meio
  File "C:\...\ex01.py", line 2, in <module>                   ← arquivo e linha
    idade = int(input("Idade: "))                              ← trecho do código
ValueError: invalid literal for int() with base 10: 'vinte'    ← o erro e o motivo (ler primeiro)
```

## Várias camadas ([ex02](ex02.py))

```python
def dividir_conta(total, pessoas):
    return total / pessoas

print("Conta do bar")
valor = dividir_conta(90, 0)
print("Cada um paga:", valor)
```

```
Traceback (most recent call last):
  File "...ex02.py", line 5, in <module>          ← camada 1: o programa principal chamou a função
    valor = dividir_conta(90, 0)
  File "...ex02.py", line 2, in dividir_conta     ← camada 2 (a mais recente): onde a divisão aconteceu
    return total / pessoas
           ~~~~~~^~~~~~~~~
ZeroDivisionError: division by zero
```

- Quebra na **linha 2**, dentro da função, mas a divisão está escrita certa.
- O zero entrou na **linha 5**, na chamada `dividir_conta(90, 0)`. O conserto é ali: `dividir_conta(90, 2)`.
- Mesma ideia do resto do dia, agora entre camadas: **onde quebra ≠ onde o problema começou**.
