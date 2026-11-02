# Dia 5 · Bloco 6: Misturados

## ✅ O que aprendi neste bloco

- Dá para **prever o erro só lendo o código**, antes de rodar: os 5 erros do dia foram classificados certo, 5 de 5
- A linha que **quebra** é a linha onde a operação impossível acontece (a soma, a divisão, a conversão). A linha do **problema** é onde o dado ruim nasceu
- Às vezes existe mais de um conserto certo (no `ex03`, dava para mudar `km` ou a conta de `litros`)

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- **Previsão da linha que quebra:** no `ex01` e no `ex03` eu previ uma linha diferente da real. O erro aparece na linha da **operação** (`peso + taxa`, `km / litros`), não na linha seguinte nem na anterior.
- **Peso pode ter decimal.** Consertei o `ex01` com `int(input(...))`, que funciona com `2`, mas quebra com `1.5` (`ValueError`). Para peso, `float` combina melhor com o dado.

## Previsão × realidade

| Exercício | Erro previsto | Erro real | Linha que quebra | Linha do problema |
|---|---|---|---|---|
| [ex01](ex01.py) frete | `TypeError` ✅ | `TypeError` | 4 (`peso + taxa`) | 2 (`input` sem conversão) |
| [ex02](ex02.py) boletim | `NameError` ✅ | `NameError` | 3 | 3 (`nota_Final` × `nota_final`) |
| [ex03](ex03.py) consumo | `ZeroDivisionError` ✅ | `ZeroDivisionError` | 4 (`km / litros`) | 3 (`litros` vira 0) |
| [ex04](ex04.py) mercado | `SyntaxError` ✅ | `SyntaxError` | 3 | 3 (aspa não fechada) |
| [ex05](ex05.py) cachorro | `ValueError` ✅ | `ValueError` | 3 (`int(texto)`) | 2 (`"3 anos"` não é um número) |

## O `ex05` refeito do meu jeito

Em vez de deixar o número fixo no código, o programa passou a perguntar:

```python
print("Idade do cachorro")
idade_cachorro = input("Quantos anos de cachorro: ")
idade = int(idade_cachorro)
print("Em anos humanos:", idade * 7)
```

Digitando `3`, mostra `Em anos humanos: 21`. Se alguém digitar `3 anos`, o mesmo `ValueError` volta: agora o "dado ruim" viria do usuário, e não do código.
