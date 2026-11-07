# Dia 10: Comparações

O programa começa a fazer perguntas: `==`, `!=`, `>`, `<`, `>=` e `<=`, sempre com resposta `True` ou `False`. É a base das decisões que chegam no Dia 11.

## ✅ O que aprendi neste dia

- **Uma comparação é uma pergunta, e a resposta é um `bool`:** `minutos >= META_MINUTOS` vale `True` ou `False`, e essa resposta pode ser guardada em uma variável ou mostrada em uma f-string.
- **Os 6 operadores:** `==` igual, `!=` diferente, `>` maior, `<` menor, `>=` maior ou igual, `<=` menor ou igual.
- **Empate:** `120 >= 120` é `True`, mas `120 > 120` é `False`.
- **Um `=` guarda um valor; dois, `==`, perguntam se os valores são iguais.**
- **Texto comparado com número:** `"1234" == 1234` não quebra e responde `False`; `"20" >= 18` quebra com `TypeError`. Como o `input` devolve texto, o número digitado precisa ser convertido antes da comparação.
- **Maiúsculas importam:** `"Recife" == "recife"` é `False`. Para ignorar essa diferença, comparo os dois lados com `.upper()`.
- **F-string não é só para o `print`:** ela monta um texto comum, então funciona também no `input` ou em uma variável.
- ✨ **Meta em uma constante, usada também no texto:** com `{META_DE_APROVEITAMENTO}` dentro da f-string, trocar a meta exige editar uma linha só.
- ✨ **Comparar o dado direto:** para saber se errei alguma questão, `questoes_acertadas != questoes_feitas` é mais claro do que olhar o percentual.

---

## ⚠️ Pontos de atenção

- **Rodar sem erro não prova que o programa está certo:** `codigo == CODIGO_ARMARIO`, com `codigo` vindo de um `input` sem conversão, responde `False` até para o código certo.
- **Depois de corrigir, ler a saída:** troquei a constante para 80, a tela ainda dizia "meta de 70%", e eu disse que estava pronto.
- **Ler o enunciado até o fim:** o `ex01.py` pedia a meta em uma constante, e eu entreguei primeiro com o número solto.

---

## 🧑‍🏫 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Função × método: `len(cidade)`, `cidade.len()`, `cidade.upper()` e `upper(cidade)` | ⭐ | Previ as quatro e expliquei as duas que quebram |
| 2. `len(acertos) / len(questoes)` com `8` e `10` tirou o erro. Está consertado? | ⭐ | Não: a conta vira `1 / 2 * 100` e mostra `50.0%`. O conserto é `int(input(...))`, que mostra `80.0%`. Falei que não tinha certeza, mas o raciocínio estava certo |
| 3. `125 // 60`, `125 % 60` e `:02d` | ⭐ | `2h05min`; sem o `:02d`, `2h5min` |

### Aquecimento

⭐ `META_MINUTOS - minutos`, com meta de 120 e 135 minutos estudados, mostra `Faltam -15 minutos`. Disse que a frase não faz sentido, porque a meta já foi batida. Faltava o programa saber se 135 é maior ou igual a 120: é para isso que servem as comparações.

### Previsões, respondidas sem rodar

| Previsão | Resultado | Correção |
|---|---|---|
| 1. Cinco comparações com `idade`, `nota` e `cidade` | ⭐ | Todas certas, inclusive `"Recife" == "recife"`. ⚠️ Escrevi "igual 18" no lugar de `7.5`, sem mudar o resultado |
| 2. `input` comparado com `1234` usando `==` | ⭐ | `Abriu? False`: `"1234"` é texto, e `1234` é número |
| 3. `input` comparado com `18` usando `>=` | ⭐ | `TypeError`: não dá para comparar maior ou igual entre `str` e `int` |

### Exercícios

- **`ex01.py`, aproveitamento e meta:** ✅ As saídas ficaram exatas de primeira, mas sem ⭐, porque faltou a constante pedida. O número continuava solto na mensagem depois da primeira correção, com a tela mostrando "70%" e a constante em 80. Na segunda correção, ficou certo. ✨ Corrigi `aproveitamento < 100.0` para comparar as questões direto, e um erro de digitação no nome da constante.
- **`ex02.py`, capital do Ceará:** ⭐ Usei `.upper()` sem dica para aceitar qualquer combinação de maiúsculas e testei casos além dos pedidos.

### Experimento fora do roteiro (`experimento.py`)

- > *Perguntei:* existe f-string para `input`?

  Testei e funcionou. Não é um recurso do `input`: a f-string monta o texto primeiro, e o `input` recebe esse texto pronto.

- > *Perguntei:* dá para digitar a UF e o programa perguntar a capital daquela UF?

  Usei `if`/`elif` antes da aula e cheguei a 27 UFs e 89 linhas. O professor apontou o trabalho braçal, e eu não consegui visualizar a primeira dica sobre manter um único `print`; com um exemplo pequeno, entendi e apliquei. Depois, tirei as constantes usadas uma vez só, e o arquivo caiu para 61 linhas. ⚠️ Com uma UF que não existe, ele mostra `ERRO` e depois quebra com `NameError`. Fica como registro: `if` e `elif` têm aula própria, e o dicionário é o jeito recomendado para esse tipo de tabela.

### Cola

✅ 6 de 6. Na pergunta 6b, reescrevi um programa maior do que o pedido, usando o `ex01.py`, mas o objetivo foi cumprido: trocar a meta exige editar uma linha só.
