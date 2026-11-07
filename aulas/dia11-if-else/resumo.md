# Dia 11: `if` / `else`

O programa começa a decidir: com `if` e `else`, cada caminho mostra só o que faz sentido naquele caso. A indentação passa a definir o que pertence a cada bloco.

## ✅ O que aprendi neste dia

- **`if` faz a pergunta:** o bloco abaixo dele só roda se a condição der `True`.
- **`else` não tem condição:** o bloco dele só roda se a condição do `if` der `False`.
- **Os `:` terminam a linha do `if` e a do `else`** e abrem o bloco.
- **A indentação define o bloco:** em C, quem faz isso são as chaves `{ }`; em Python, mudar o recuo pode mudar o resultado do programa.
- **O que fica fora do bloco sempre roda.**
- 🐞 **`IndentationError`:** `expected an indented block` quando falta um recuo depois do `if`, e `unexpected indent` quando sobra um recuo onde nada abriu um bloco.
- **`SyntaxError` e `IndentationError` impedem o programa de começar:** nem o `input` da primeira linha roda. Já o `ValueError` acontece com o programa em andamento.
- **Testar um `if`:** usar pelo menos um valor para cada caminho, mais o valor exato do limite.
- ✨ **Indentação de 4 espaços.** A tecla Tab do VS Code já coloca os 4.
- ✨ **Constante não muda:** o que muda de um caso para outro fica em uma variável comum, que recebe um valor em cada bloco. Assim, a linha do `Total` aparece uma vez só.
- ✨ **O nome diz o que a variável guarda:** `taxa_cobrada`, e não `desconto`, para um valor que é somado.
- ✨ **Comentário longo fica acima da linha,** não no fim dela.

---

## ⚠️ Pontos de atenção

- **`else` não evita todo erro:** com `abc`, `int("abc")` quebra na linha do `input`, com `ValueError`, e o `if` nem roda. `int("7")` funciona, porque o conteúdo do texto pode virar número. Tratar esse erro é assunto de `try`/`except`, na Etapa 2.
- **"A partir de 100" inclui o 100:** usei `>` onde o certo era `>=`.
- **Rodar sem erro não prova que está certo:** na cola, um programa com a conta invertida rodou, e eu disse que estava certo. Comparar com o resultado esperado revelou a diferença.
- **Testes repetidos não testam mais:** vários números ímpares passam sempre pelo mesmo bloco.

---

## 🧑‍🏫 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Trocar `conta / pessoas` por `conta / 2` conserta o programa? | ⭐ | Não: o erro some, mas o número de pessoas digitado é ignorado. O conserto é `int(input(...))` |
| 2. Trinta arquivos de recibo copiados à mão | ✅ | Propus um arquivo só, com `input`, sem dica. ⚠️ O código tinha aspas sem fechar e um `print` sem `f`; corrigi na segunda tentativa |
| 3. O mesmo `print` com e sem `f`, com uma comparação dentro | ⭐ | Previ as duas saídas. Ajuste: sem o `f`, o texto é mostrado, não rodado |

### Aquecimento

⭐ `Faltam {faltam} minutos` seguido de `Meta batida!`, com `90` e com `135`. Previ as saídas e disse que falta uma condição: as duas frases sempre aparecem.

### Exemplo

⭐ `Até amanhã!` aparecia também para quem não bateu a meta. Sem que isso fosse pedido, movi essa linha para o bloco do `if` e acrescentei uma mensagem no `else`.

### Previsão

⭐ **Previsão 1:** com `nota = 5`, o programa com a última linha fora do bloco mostra só `Parabéns`, e o outro não mostra nada. Comparei com as chaves de C.

### Exercícios

- **`ex01.py`, par ou ímpar:** ✅ Testei com `abc` por conta própria e vi que o `else` não evita esse erro. O `else` que eu tinha colocado nunca rodava, porque `numero % 2` só dá `0` ou `1`. Depois, deixei só `if` e `else`. ⚠️ Fiz vários testes só com números ímpares.
- **`ex02.py`, frete:** ✅ Depois de correções. Primeiro, a compra de exatamente `100` pagava frete, e eu alterava a constante dentro do bloco para ter um único `Total`. Na segunda versão, a constante ficou intacta, mas o `Total` foi repetido. Não consegui visualizar a solução e pedi ajuda; com um exemplo de ingresso, usei uma variável em cada bloco. ✨ Depois, troquei `desconto_frete` por `frete`, porque o valor é somado e não é um desconto.
- **`erros/ex01.py`:** ✅ Vi o defeito antes de rodar. ⚠️ Disse que quebrou na linha 3, mas foi na 4; a 3 é a do `if` citado na mensagem.
- **`erros/ex02.py`:** ⭐ Linha 4 e `unexpected indent`, com o sentido certo.

### Cola

✅ 6 de 6, depois de correções. Na 1b, o motivo tinha sido copiado da 1a. Na 4a, chamei de `TypeError` e, com ajuda, cheguei ao motivo certo: `"abc"` não é um valor aceito para virar inteiro. Na 6b, a primeira versão subtraía a taxa em vez de somar; comparando com o programa original, corrigi e troquei o nome da variável.
