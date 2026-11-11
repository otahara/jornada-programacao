# Dia 14.1: Reforço de lógica (o plano em 4 partes)

Primeiro dia de reforço: uma revisão curta sobre regras e decisões independentes e, depois, um jeito organizado de escrever o plano antes do código, separando dados, contas, decisões e o que depende do quê.

## ✅ O que aprendi neste dia

- **O programa segue a regra do cliente, não a do mundo real:** se a regra diz "matrícula, uma vez só, e R$ 70 por mês", cada mês custa R$ 70, mesmo que muitas academias façam diferente. Se a regra deixar dúvida, pergunto antes de programar, em vez de supor.
- **Conferir se a regra é a mesma antes de reaproveitar uma fórmula:** a fórmula do estacionamento (`primeira hora + demais × (horas − 1)`) só serve quando o primeiro item tem um preço diferente dos outros.
- **Dois `if` × `elif`:** dois `if` fazem duas perguntas independentes. No `elif`, a cadeia para no primeiro `True` e o resto nem é testado. Regras que valem juntas (frete grátis e desconto VIP) ficam em `if` separados.
- **O plano em 4 partes** (é a primeira camada do método das camadas), escrito em português, com `#`, antes de qualquer código:

| Parte | Pergunta que ela responde | Como achar no enunciado |
|---|---|---|
| **Dados** | O que o programa precisa saber? | O que a pessoa digita (vira `input`) e os números fixos da regra (viram constantes) |
| **Contas** | O que o programa precisa calcular? | A conta em palavras, com os nomes no lugar dos números, sem fazer a conta |
| **Decisões** | Onde o programa escolhe um caminho? | "se", "até", "a partir de", "só para": cada um vira uma decisão |
| **Depende?** | Essa decisão só faz sentido depois de outra? | **Sim** → fica dentro do `else` da outra. **Não** → é um `if` separado |

## ⚠️ Pontos de atenção

- **Supor uma regra que o enunciado não dá:** na academia, achei que a matrícula já pagava o primeiro mês. A minha fórmula estava certa para a regra que eu imaginei, mas não para a regra que foi dada.
- **Pular o plano:** no caixa da loja, comecei direto pelo código, e a pergunta do VIP ficou antes da conferência do valor inválido. Esse é o tipo de erro que a parte "Depende?" do plano pega.
- **Método sem os parênteses:** `input(...).lower == "s"` não chama o método e dá sempre `False`, sem nenhuma mensagem de erro. O certo é `.lower()`.

## 📋 Relatório do professor

### Revisão

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. Academia: R$ 90,00 de matrícula, uma vez só, e R$ 70,00 por mês. a) quanto paga quem fica 3 meses; b) e 5 meses; c) a linha `total = ...` com `MATRICULA`, `MENSALIDADE` e `meses` | ⚠️ → ✅ | Respondi R$ 230,00 e R$ 370,00, com `total = MATRICULA + (MENSALIDADE * (meses - PRIMEIRO_MES))`. Supus que a matrícula já pagava o primeiro mês, como em muitas academias, mas o enunciado não dizia isso: o programa segue a regra do cliente, e, na dúvida, se pergunta antes de programar. A fórmula batia com as minhas contas à mão. Certo: R$ 300,00 e R$ 440,00, com `total = MATRICULA + (MENSALIDADE * meses)`, que reescrevi sozinho |
| 2. `nota = 9` com `if nota >= 7` e `if nota >= 9`: o que aparece com dois `if` (A) e trocando o segundo por `elif` (B) | ⭐ | A: `Aprovado` e `Com louvor`, porque os dois `if` são independentes. B: só `Aprovado`, porque a cadeia para no primeiro `True` |

### Aquecimento

- **Previsão 3:** ⭐ Loja com frete grátis a partir de R$ 200,00 (`if`) e 10% de desconto para VIP (`elif`), as duas regras valendo juntas. Compra de R$ 250,00 de cliente VIP: previ que só aparece `Frete grátis`, porque o `if` dá `True` e o `elif` nem é testado, e disse sozinho que o certo seriam dois `if` separados, para a cliente receber os dois benefícios.

### O plano em 4 partes

- **Primeira tentativa (caixa da loja):** comecei pelo código, sem o plano. Depois, usei os títulos "Dados", "Contas" e "Decisões" como etiquetas em cima do código. Eu ainda não tinha aprendido esse formato e pedi para aprender antes de ser cobrado.
- **`exemplo.py`:** o plano em 4 partes montado para o estacionamento com tolerância do Dia 14, que eu já conhecia, com a tabela acima. O caixa da loja fica para o Dia 14.2, começando por esse plano.
