# Dia 13: Operadores lógicos (`and`, `or`, `not`)

Com `and`, `or` e `not`, uma condição só pode juntar duas ou mais comparações. Cada regra do enunciado vira uma linha da cadeia.

## ✅ O que aprendi neste dia

- **`and` ("e"):** dá `True` só quando **todos** os lados são `True`. Um lado `False` já derruba tudo.
- **`or` ("ou"):** dá `False` só quando **todos** os lados são `False`. Um lado `True` já basta.
- **`not` inverte:** `not True` é `False`, e `not False` é `True`.
- **Tabela-verdade:** a lista de todas as combinações possíveis (`True`/`True`, `True`/`False`...) e o resultado de cada uma. Com duas condições, são 4 linhas.
- **Variável que guarda `True` ou `False`:** `tem_ingresso = resposta.lower() == "s"` guarda o **resultado** da comparação, e o `if` usa a variável direto.
- **"3 ou mais" não é `or`:** é uma comparação só, `horas >= 3`. O `>=` já quer dizer "maior **ou** igual".
- **Cada regra vira uma linha da cadeia, na mesma ordem:** regra 1 no `if`, regra 2 no `elif`, o resto no `else`. Montar uma linha para cada **combinação** de dados deixa buracos.
- **Decisões independentes ficam em `if` separados:** no estacionamento, o passo 1 calcula o total das horas para todo mundo, e o passo 2 só tira o desconto de quem cumpre a regra.
- **O `else` é opcional:** ele só existe quando há algo para fazer no caso contrário. Se o "não" é só seguir em frente, o `if` fica sem `else`.
- **Quem decide se uma linha roda sempre é o recuo, não o `else`:** um `print` sem recuo, depois da cadeia, roda em qualquer caminho.
- **Hora começada é cobrada inteira:** `minutos // 60` dá as horas completas, e, se `minutos % 60 > 0`, soma 1.
- ✨ **`if tem_ingresso:` e `if not tem_ingresso:`**, e não `== True` ou `== False`: a variável já é `True` ou `False`.
- ✨ **Nome de variável `True`/`False` que soa como pergunta:** `tem_cadastro` e `tem_multa`, e não `cadastro` e `multa`. A linha fica legível como frase: `if not tem_cadastro:`.
- ✨ **Constante calculada a partir de outra:** `MEIA_ENTRADA = ENTRADA_INTEIRA / 2`. Se a inteira mudar, a meia acompanha sozinha.

---

## ⚠️ Pontos de atenção

- **Juntar todas as condições em cada conta:** no plano do estacionamento, escrevi uma conta para "mais de 1 hora e sem cartão" e outra para "mais de 1 hora, com cartão e 3 horas ou mais". A pessoa com cartão e 2 horas não cabia em nenhuma. O que destravou: separar em 2 passos, o total das horas (para todo mundo) e o desconto (só para quem cumpre a regra).
- **Trocar o número pela variável:** na conta do estacionamento com 6 horas, multipliquei por 6, e não por 5, cobrando a primeira hora duas vezes. O que destravou: um caso resolvido em outro cenário, com a coluna "a mais" (`aulas - 1`).
- **Um `else` que jogava fora o valor calculado:** no `ex02.py`, o `else` do desconto trocava o total por R$ 8. Sem desconto, o total tem que ficar como está, então o `else` sai.
- **Contar decisões:** um `if` com `else` é **1 pergunta** com 2 caminhos, e não 2 decisões.
- **Ler o enunciado até o fim:** constante `"Ana"` quando o enunciado pedia `ana`, o espaço depois de `(s/n)` e o `3` que o enunciado pedia como constante.

---

## 🧑‍🏫 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Academia com `>= 18` antes de `>= 60`: quanto paga quem tem 65 anos? Como consertar? | ⭐ | Previ `Mensalidade: R$ 100` e consertei pondo `>= 60` primeiro. Não escrevi o porquê, mas o conserto mostrou que entendi: 65 passa no primeiro teste e a cadeia para ali |
| 2. Estacionamento (1ª hora R$ 8, cada hora a mais R$ 3): a) 1 e 4 horas; b) a conta com `horas`; c) quantas decisões | ⚠️ | a) ✅ R$ 8 e R$ 17. b) Não entendi o enunciado; reformulado com 4 e 6 horas lado a lado, errei a de 6 (multipliquei por 6). Depois de um caso resolvido em outro cenário, cheguei a `8 + (3 * (horas - primeira_hora))`. c) Respondi "2 decisões: um `if` e um `else`"; com dois programas para comparar, concluí que é 1 pergunta, e o `else` cuida do "não" |

### Aquecimento

⭐ **Previsão 3:** festa com dois `if` separados (idade e ingresso). Previ `Pode entrar` para 15 anos com ingresso e para 20 anos sem ingresso, e, na c), listei sozinho os 4 casos possíveis, que é a tabela-verdade do `and`.

### Previsões e exemplo

- **`exemplo.py`:** o programa da festa com `and`. Acrescentei `.lower()` por conta própria, para aceitar `S` maiúsculo, e testei os limites 18 e 17.
- **Previsão 4:** ⭐ Tabela-verdade do `or` (aniversário ou convite VIP), 4 de 4.
- **Previsão 5:** ⭐ `not` com variável `True`/`False`, inclusive o `S` maiúsculo virando `True` por causa do `.lower()`.

### Exercícios

- **`ex01.py`, login:** ✅ Lógica certa (`and`, constantes, os 4 casos da tabela testados). A constante ficou `"Ana"`, e o enunciado pedia `ana`; foi automático, por ser nome próprio, e ajustei.
- **Problema de lógica, estacionamento (`ex02.py`):** ✅ Com ajuda.
  - Plano: dados certos e a conta das horas certa, mas cada conta juntava todas as condições, e o caso "com cartão e 2 horas" ficou de fora. Também achei que o "3 horas ou mais" precisaria de um `or`, e não: é `horas >= 3`.
  - Programa: na primeira versão, o desconto exigia `horas > 1`, e não `>= 3`, e o `else` do desconto trocava o total por R$ 8. Corrigidos os dois, os 7 testes deram certo, inclusive casos que eu mesmo inventei (1 hora com cartão e 100 horas).
- **`ex03.py`, cinema:** ✅ Com ajuda. Comecei montando uma linha para cada combinação e travei; com a tabela "cada regra vira uma linha da cadeia" e a regra 1 traduzida (`and not`), escrevi o `elif` com `or` e o `else`. Usei `print` provisórios para testar o caminho e criei `MEIA_ENTRADA = ENTRADA_INTEIRA / 2`.
- **`ex04.py`, desafio dos minutos (ideia minha):** ✅ Com ajuda. Minha primeira ideia era somar 1 hora quando o resto fosse ímpar; a pista do `121 % 60 = 1` levou a `minutos_restantes > 0`. Achei que o `else` vazio era necessário para o `print` aparecer, e testei: o `print` sem recuo roda sempre. Reaproveitei os dois passos do `ex02.py` trocando só `horas` por `horas_cobradas`.
- **`ex05.py`, biblioteca:** ⭐ A cadeia saiu de primeira e sem dica: `not` na regra 1 e `or` na regra 2, na ordem do enunciado. ✨ Faltou a constante do `3`, e os nomes `cadastro`/`multa` viraram `tem_cadastro`/`tem_multa`.

### Cola

✅ 4 perguntas. ⭐ Na 2a (expliquei o `not` e ainda disse o que aconteceria com `s`) e na 4c (o `else` só existe quando há algo para fazer no caso contrário). Na 4a, descrevi o caminho certo (entra no 1º `if` e no 2º `else`), mas não consegui chegar ao valor fazendo a conta de cabeça. Com um teste de mesa em tabela (o `valor` depois de cada linha que roda), cheguei a R$ 11.00 depois do 1º `if` e R$ 8.00 depois do 2º `else`: o programa mostra R$ 8.00, e o certo seria R$ 11.00. Desde então, as perguntas da cola que pedem um valor vêm com essa tabela.
