# Dia 12: `elif`

Com `elif`, uma decisão pode ter mais de dois caminhos. O Python confere as condições de cima para baixo, e a ordem delas muda o resultado.

## ✅ O que aprendi neste dia

- **`elif` quer dizer "senão, se":** ele faz parte da mesma decisão do `if`, em vez de começar uma nova.
- **Cadeia e bloco:** `if`, `elif` e `else` ligados formam uma **cadeia**; as linhas recuadas embaixo de cada um formam o **bloco** dele.
- **O Python para na primeira condição `True`:** só aquele bloco roda e o resto da cadeia é pulado. Numa cadeia, roda **exatamente 1 bloco** (o do `else`, se nenhuma condição der `True`).
- **Dois `if` separados são duas decisões:** o segundo é conferido sempre, mesmo que o primeiro já tenha rodado. Por isso uma nota `9.5` recebia conceito A **e** B.
- **A ordem importa:** quando as faixas se sobrepõem, a condição mais exigente vem primeiro (`>= 9` antes de `>= 7`). Também funciona do menor para o maior, mas aí mudam três coisas juntas: a ordem, a comparação (`<=` no lugar de `>=`) e os limites (idade **máxima** no lugar de idade **mínima**).
- **Uma condição de cima pode "engolir" a de baixo:** com `>= 7` antes de `>= 9`, o bloco do conceito A nunca roda, e o Python não avisa nada.
- **Tabela progressiva** (conta de luz, Imposto de Renda): cada faixa cobra só os kWh que caem dentro dela. As faixas de baixo entram cheias; a última entra com `consumo - limite`.
- **Para montar a fórmula de um caminho:** fazer a conta à mão com dois valores diferentes, um embaixo do outro. O que não muda entre as duas contas é fixo (constante); o que muda vem do `consumo`.
- **Contar de 101 a 200 dá 100, não 99:** o jeito seguro é subtrair os limites (`200 - 100`).
- ✨ **Limites e preços em constantes** (`IDADE_MINIMA_ADULTO`, `LIMITE_FAIXA_1`): se a regra mudar, muda uma linha.
- ✨ **Uma variável em cada bloco e um `print` só, fora da cadeia:** cada bloco decide o valor, e a frase fica num lugar só.
- ✨ **Cada nome diz uma coisa só:** `preco`, `preco_kwh` e `PRECO_FAIXA_1` no mesmo programa confundem; `valor_conta` diz o que a variável guarda.

---

## ⚠️ Pontos de atenção

- **Montar a fórmula de um caminho foi o mais difícil do dia.** Fazer a conta com números eu consigo; trocar o número pela variável (`consumo`) foi onde travei. O que destravou: a tabela com dois consumos lado a lado e a fórmula com lacunas para preencher.
- **Na primeira conta da luz, cobrei todo o consumo pelo preço da última faixa** (150 × 0,90). A pista de que estava errado: 1 kWh a mais faria a conta pular de R$ 60,00 para R$ 90,90.
- **Ordem das operações:** `consumo - LIMITE * 0.90` multiplica antes de subtrair. A subtração precisa de parênteses: `(consumo - LIMITE) * 0.90`.
- **Inverter a ordem de uma cadeia não é só trocar as linhas de lugar:** no `exemplo.py`, troquei `>=` por `<=` sem trocar os conceitos, e o B e o C saíram invertidos.
- **Numa previsão, responder antes de rodar:** assim dá para saber se o raciocínio bateu com o programa.

---

## 🧑‍🏫 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Limite de saque de 500 com `>`: o que aparece com `500` e com `501`? | ⭐ | `500` não é maior que 500, então cai no `else`; o `Retire seu cartão` aparece nos dois casos porque está fora do bloco |
| 2. Padaria com o desconto calculado na calculadora e o dono pedindo 15% | ✅ | Propus a constante `DESCONTO`, o preço vindo do `input` e a f-string, sem dica. No `revisao2.py`, a primeira versão tinha `DESCONTO = 0.90` (✨ o nome dizia "desconto", mas o valor era o que se paga) e continuava em 10%; a segunda passou a calcular `preco - (preco * (DESCONTO / 100))`, com o desconto em percentual |
| 3. `nothing added to commit but untracked files present` | ✅ | Achei na mensagem a linha `use "git add"`. Faltou dizer que o `commit` precisa ser repetido depois do `add` |

### Aquecimento

✅ Dois `if` separados para dar conceito: previ `Conceito A` e `Conceito B` para `9.5`, `Conceito B` para `8` e `Conceito C` para `5`. Rodei antes de responder, por isso sem ⭐.

### Previsões

- **Previsão 1:** ✅ O `Conceito B` aparece também para `9.5` porque cada `if` é uma decisão independente, conferida mesmo que a anterior tenha rodado.
- **Previsão 2:** ✅ Com `>= 7` antes de `>= 9`, o `9.5` para no B, e nenhuma nota recebe A. A segunda parte veio depois de a pergunta ser repetida.
- **Experimento no `exemplo.py`:** troquei a primeira condição por `nota <= 7` sem trocar os conceitos, e as notas 8 e 5 saíram com C e B. Voltei à ordem com a condição mais exigente primeiro.

### Exercícios

- **`ex01.py`, faixa etária do cinema:** ⭐ Saída exata de primeira, inclusive nas bordas (11, 12, 59, 60), com a ordem do menor para o maior e `<=`. ✨ O mesmo `print` aparecia 4 vezes e os limites eram números soltos; na segunda versão, ficou um `print` só e as constantes `IDADE_MAXIMA_...`. Por conta própria, fiz uma terceira versão do maior para o menor, trocando junto a comparação (`>=`) e os limites (`IDADE_MINIMA_...`).
- **Problema de lógica, conta de luz em faixas (`ex02.py`):** ✅ Depois de muitas dicas.
  - À mão: acertei 80 kWh; em 150 e 250, cobrei o consumo inteiro pelo preço da última faixa. Depois, acertei 150 (105,00) e, em 250, contei 99 e 49 kWh nas faixas; com a subtração dos limites, cheguei a 210,00.
  - Plano em português: dados e caminhos certos; nas contas, travei em trocar o número pela variável. Destravei com dois consumos lado a lado (o que muda × o que não muda) e com a fórmula do caminho 3 com lacunas.
  - Programa: certo em todas as bordas (100 → 60,00; 101 → 60,90; 200 → 150,00; 201 → 151,20). ✨ `preco` guardava o valor da conta; `valor_conta` diz isso melhor.
  - Perguntei se, com 100 faixas, o programa não viraria uma bagunça. Vira: o jeito de simplificar usa listas e laços, que vêm nas próximas semanas.

### Cola

✅ 6 de 6. ⭐ Na pergunta 3 (conta de luz de 230 kWh, o código da cadeia completo e o porquê da faixa 2 cheia), sem consulta. Na 1b, eu não lembrava o que era bloco; montei um exemplo próprio com `if`, `elif`, `elif` e `else` todos `True` e vi que só o primeiro bloco roda.

⭐ **Pergunta extra, por conta própria:** perguntei o nome das linhas do `if`, `elif` e `else` (**cabeçalho**) e concluí sozinho que, sem o bloco, o cabeçalho não teria razão de existir. O Python concorda: cabeçalho sem bloco dá `IndentationError`.
