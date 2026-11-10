# Dia 14: Treino de decisão (decisão dentro de decisão)

Um `if` dentro de outro: a segunda pergunta só é feita para quem passou pela primeira. E, para programas com várias peças, montar em camadas em vez de escrever tudo de uma vez.

## ✅ O que aprendi neste dia

- **Decisão dentro de decisão:** um `if` (ou uma cadeia inteira) dentro do bloco de outro. Ele só é olhado quando o caminho de fora deixa passar. Na festa, só quem tem 18 anos ou mais ouve a pergunta do ingresso.
- **O que só faz sentido para um caminho vai dentro dele:** no estacionamento, a pergunta do cartão, as contas e os `print` do total só existem para quem paga, então ficam dentro do `else`.
- **A conferência vem primeiro:** no triângulo, primeiro se confere se os lados formam um triângulo; a classificação (equilátero, isósceles, escaleno) fica dentro dela.
- **O recuo decide onde a linha roda:** um `print` sem recuo, depois da cadeia, roda em todos os caminhos. Se ele usa uma variável criada só dentro do `else`, os outros caminhos quebram com `NameError`.
- **Decisões independentes ficam em `if` separados:** frete grátis e cupom de desconto são regras que não dependem uma da outra. Com `elif`, a segunda nem é olhada quando a primeira dá `True`.
- **Campeão provisório:** para achar o maior, começa supondo que o maior é o primeiro e compara cada número seguinte só com o campeão, trocando quando aparece alguém maior. Cada número novo é só mais um `if`, sem `else`.
- **Especificador de formato:** em `f"{resto:02d}"`, o que vem depois dos `:` diz como mostrar o valor. `02d` = inteiro com pelo menos 2 dígitos, completando com 0 à esquerda (`5` vira `05`).
- **Resto de número negativo:** em Python, `-5 % 60` dá `55`. Por isso a cadeia do estacionamento confere o tempo total (`minutos`), e não o resto.
- **Montar em camadas (desenvolvimento incremental):**
  1. o plano em português vira comentário no arquivo;
  2. esqueleto: só os `if` / `elif` / `else`, com um `print` provisório em cada caminho, e um teste para cada caminho;
  3. recheio: um pedaço de código por vez, rodando depois de cada um;
  4. limpeza: saem os `print` provisórios e os comentários que só repetem o código.

  Cada linha demora um pouco mais, mas o programa termina antes, porque o erro fica no pedaço que acabou de ser escrito.
- ✨ **Nome que diz o que o número é:** o 30 do estacionamento é o **máximo** de minutos grátis; um nome com "mínimos" diz o contrário.
- ✨ **Nomes de variáveis que só mudam pela ordem:** `lado1`, `lado2`, `lado3`, curtos e iguais ao que aparece na tela.

---

## ⚠️ Pontos de atenção

- **Escrever tudo de uma vez:** no `ex01.py`, juntei as peças do estacionamento num arquivo só e me perdi (a cadeia olhava o resto da divisão, os `print` estavam fora do `else` e faltava somar a hora começada). O que destravou: montar em camadas, testando cada uma.
- **Um `else` que joga fora o valor:** na primeira versão do campeão provisório, o `else` trocava o campeão pelo terceiro número sem comparar. Com 9, 2 e 5, saía `Maior: 5`.
- **Esquecer uma decisão inteira:** no triângulo, escrevi a classificação e esqueci de conferir se os lados formavam um triângulo. Pulei o plano, que é justamente onde as decisões são listadas.

---

## 🧑‍🏫 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Loja com frete grátis a partir de R$ 100 e R$ 10 de desconto com cupom, escrita com `if`/`elif`. Compra de R$ 150 com cupom: a) quanto o programa cobra; b) quanto deveria cobrar; c) como consertar | ✅ | O primeiro formato (tabela com uma coluna "Roda?") não funcionou para mim, e passamos a seguir o código linha por linha na conversa. Previ que o `elif` não roda porque o `if` já deu `True`, que o programa cobra R$ 150.00 e que o certo seria R$ 140.00. O conserto saiu sozinho: separar em dois `if`, porque são decisões independentes |
| 2. `125 // 60`, `125 % 60` e `f"{horas}h{resto:02d}min"` | ⭐ | Respondi `2h05min`, com as duas contas, e expliquei que o `:02d` completa com 0 à esquerda. O nome do recurso é especificador de formato |

### Aquecimento

✅ Estacionamento com tolerância (negativo é inválido, até 30 minutos é grátis): para quem ficou 20 minutos, o programa precisa calcular as horas e conferir o cartão? Respondi que não, porque a pessoa não paga e nem chegou às 3 horas do desconto. É a ponte para a decisão dentro de decisão: as contas só fazem sentido no caminho de quem paga.

### Exemplo e previsão

- **Previsão 1:** ⭐ Na festa, com idade 15, previ que o programa nem pergunta do ingresso e mostra `Entrada proibida`, porque o `else` inteiro é pulado.
- **`exemplo.py`:** os 3 caminhos testados (15; 20 com ingresso; 20 sem ingresso).

### Exercícios

- **Problema de lógica, `ex01.py`, estacionamento com tolerância:** ✅ Com ajuda, em camadas.
  - Plano: a cadeia com as 3 regras na ordem certa e a pergunta do cartão dentro da regra 3 saíram sozinhas. Simplifiquei a conta: `8 + 3 * (horas_cobradas - 1)` já dá 8 para 1 hora, então o `if`/`else` da primeira hora não era mais necessário. Faltava calcular as horas cobradas antes da conta do valor.
  - Código: tentei escrever tudo de uma vez e me perdi. Montamos em camadas: primeiro o esqueleto com `print` provisório (que mostrou que `-5 % 60` dá 55 e que a cadeia precisava olhar `minutos`), depois o recheio. O `NameError` dos `print` fora do `else` e a hora começada que não era somada apareceram nos testes, um de cada vez.
  - Mantive de propósito a saída `Primeiros 30 minutos são grátis` no lugar de `Grátis`, para mostrar o motivo; esqueci de propor antes, e o enunciado foi ajustado.
- **`ex02.py`, maior de 3 números:** ✅ A lógica saiu sozinha e de primeira: cada número comparado com os outros dois com `>=`, o que resolve os empates. A saída `Maior:` precisou de ajuste. Perguntei se havia um jeito melhor.
- **`ex03.py`, campeão provisório:** ✅ Primeiro tentei uma versão com decisões aninhadas para 4 números, que ficava sem resposta com 5, 3, 9 e 1. Depois, com o começo pronto, a primeira versão tinha um `else` que jogava fora o campeão. Corrigi e estendi sozinho para 7 números. Respondi que, com 100 números, usaria um laço.
- **`ex04.py`, triângulo válido:** ✅ Com ajuda. A classificação saiu certa (equilátero antes de isósceles), mas esqueci a conferência de que os lados formam um triângulo; com 2, 3 e 10, mostrava `Triângulo escaleno`. Com a estrutura e a primeira comparação prontas, escrevi as outras duas comparações e todos os testes deram certo.

### Cola

✅ 5 perguntas. ⭐ Na 1 (o que aparece e por que o `input` do ingresso fica dentro do `else`). Na 5a, a primeira versão repetia o texto da aula; reescrevi com as minhas palavras.
