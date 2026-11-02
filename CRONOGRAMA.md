# Cronograma da Etapa 1: Fundamentos de Lógica com Python

**Duração:** 43 dias (6 semanas) · **Ritmo:** cerca de 1h por dia

### Regras do cronograma
- **"Dia" é uma sessão de estudo, não um dia do calendário.** Se pular um dia, continue de onde parou. Nada de culpa.
- **Só avança quando entregar os exercícios do dia.** Se travar, o mesmo dia pode durar duas sessões.
- **Todo dia começa com revisão sem consulta:** perguntas sobre os dias anteriores **e** um aquecimento (teste de mesa ou exercício básico) que sirva de **ponte para o tema do dia**: o resultado ou a dificuldade dele leva naturalmente ao conceito novo.
- **O último dia de cada semana é de revisão leve:** reler e completar a **cola** (um caderno de anotações escrito com as suas palavras) e refazer **um** exercício antigo sem olhar. Pode ser curto.
- **Toda semana termina com um mini-projeto** que junta tudo o que foi visto até ali.
- **Ferramentas entram aos poucos (🛠️), no momento em que fazem sentido**, e viram hábito a partir dali:
  - a partir do **Dia 4 (Git + GitHub)**, toda sessão termina com o **ritual de fechamento**: `git add`, `git commit` e `git push`, deixando o progresso do dia publicado no GitHub;
  - a partir do **Dia 19 (Debugger)**, quando um laço der resultado estranho, o primeiro passo é rodar com breakpoint;
  - a partir do **Dia 32 (Testes)**, toda função com `return` ganha pelo menos um teste.
- **Erros novos entram no dia em que podem acontecer (🐞)**, sem aula própria: nesse dia, a pasta da aula ganha uma subpasta `erros/` com programas quebrados para ler, entender e consertar. Os erros básicos (`SyntaxError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`) são treinados no Dia 5.

Legenda: ⚪ não iniciado · 🟡 em andamento · ✅ concluído · 🛠️ ferramenta de programador · 🐞 erro novo que aparece nesse dia

---

## Semana 1: A base (ambiente, variáveis, Git, erros, tipos)

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 1 | ✅ | Ambiente + Hello World | interpretador, terminal, PATH, VS Code, `print` | `ex01` a `ex04` |
| 2 | ✅ | Variáveis | o que é uma variável, `=` como "recebe", nomes válidos, teste de mesa | `ex01` a `ex04` + teste de mesa |
| 3 | ✅ | Entrada de dados | `input`, por que ele sempre devolve texto, converter com `int()` e `float()` | programa que pergunta e responde |
| 4 | ✅ | 🛠️ **Git + GitHub (parte 1): o ritual diário** | Git × GitHub, `git config`, `git init`, `.gitignore` (o que é público e o que é privado), `status`, `add`, `commit`, `log`, criar o repositório no GitHub, `remote`, `push`; README de apresentação do repositório | Dias 1 a 3 publicados no seu GitHub, com o primeiro commit |
| 5 | ✅ | 🔧 **Lendo e corrigindo erros** | treino prático, sem decorar definições: ler a mensagem de baixo para cima, achar a linha onde quebrou e a linha onde o problema começou; `SyntaxError`, `NameError`, `TypeError`, `ValueError` e `ZeroDivisionError` na prática | programas quebrados, consertados (uma pasta por erro) |
| 6 | ⚪ | Tipos e operadores aritméticos | `int`, `float`, `str`, `bool`, `type()`, `+ - * / // % **` | calculadora de operações |
| 7 | ⚪ | Trabalhando com texto | concatenação, **f-strings**, `len`, `upper`/`lower`; 🐞 `AttributeError` | cartão de apresentação formatado |
| 8 | ⚪ | 🧩 **Mini-projeto 1** | juntar tudo da semana | **Conversor**: moeda, temperatura e distância |
| 9 | ⚪ | Revisão leve | cola + refazer 1 exercício + `git log` da semana | cola da semana 1 completa |

## Semana 2: Decisão (o programa começa a "pensar")

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 10 | ⚪ | Comparações | `== != > < >= <=`, valores `True`/`False` | exercícios de "verdadeiro ou falso?" |
| 11 | ⚪ | `if` / `else` | decisão simples, **indentação**, bloco de código; 🐞 `IndentationError` | par ou ímpar, maior de idade |
| 12 | ⚪ | `elif` | várias condições em sequência, a ordem importa | faixa etária, conceito de nota (A/B/C) |
| 13 | ⚪ | Operadores lógicos | `and`, `or`, `not`, tabela-verdade | validação de login (usuário **e** senha) |
| 14 | ⚪ | Treino de decisão | combinar tudo, decisão dentro de decisão | maior de 3 números, triângulo válido |
| 15 | ⚪ | 🧩 **Mini-projeto 2** | juntar tudo até aqui | **Calculadora de IMC** com classificação |
| 16 | ⚪ | Revisão leve | cola + refazer 1 exercício + `git log` da semana | cola da semana 2 completa |

## Semana 3: Repetição e debugger (onde a maioria trava, e você não vai travar)

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 17 | ⚪ | `while` | repetir enquanto algo for verdade, **contador**, loop infinito (e como sair) | contar de 1 a 10, contagem regressiva |
| 18 | ⚪ | Acumuladores | somar e calcular média dentro do laço, validar entrada | média de N notas, "digite até acertar" |
| 19 | ⚪ | 🛠️ **Debugger do VS Code** | breakpoint, executar linha a linha (*step over* / *step into*), painel de variáveis: o **teste de mesa automático** | achar e corrigir o bug de 3 programas "quebrados" |
| 20 | ⚪ | `for` e `range` | repetir um número conhecido de vezes, `range(início, fim, passo)` | tabuada de um número |
| 21 | ⚪ | `break` e `continue` | sair do laço antes, pular uma volta | menu que repete até escolher "sair" |
| 22 | ⚪ | Laços aninhados | laço dentro de laço | tabuada completa de 1 a 10 |
| 23 | ⚪ | 🧩 **Mini-projeto 3** | juntar tudo até aqui | **Jogo de adivinhação** (número secreto, com dicas e tentativas) |
| 24 | ⚪ | Revisão leve | cola + refazer 1 exercício | cola da semana 3 completa |

## Semana 4: Listas e funções (organizando o código)

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 25 | ⚪ | Listas (parte 1) | criar, acessar por índice (começa no **0**), índice negativo, `append`, `len`; 🐞 `IndexError` | lista de compras |
| 26 | ⚪ | Percorrer listas | `for item in lista`, soma, maior e menor | estatísticas de uma lista de notas |
| 27 | ⚪ | Listas (parte 2) | `in`, `insert`, `remove`, `pop`, `index`, `sort`, fatiamento `[a:b]`; listas são **mutáveis** | fila de atendimento simples (entra no fim, sai do começo) |
| 28 | ⚪ | Funções (parte 1) | `def`, chamar, parâmetros, por que funções existem | funções de saudação e de conversão |
| 29 | ⚪ | Funções (parte 2) | `return`, diferença entre `print` e `return`, escopo | funções de cálculo reaproveitáveis |
| 30 | ⚪ | 🧩 **Mini-projeto 4** | juntar tudo até aqui | **Lista de tarefas** no terminal, com menu e funções |
| 31 | ⚪ | Revisão leve | cola + refazer 1 exercício | cola da semana 4 completa |

## Semana 5: Testes, dicionários e Git avançado

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 32 | ⚪ | 🛠️ **Testes automatizados** | `assert`, por que testar, instalar e rodar o **pytest**, arquivo `test_*.py`, ler um teste que falhou | testes para as funções do Dia 29 |
| 33 | ⚪ | Problemas clássicos | busca, contagem, filtro (o "kit básico" de todo programador), já com testes | buscar nome, contar aprovados, com pytest |
| 34 | ⚪ | Dicionários (parte 1) | pares chave → valor, acessar, adicionar, alterar, percorrer; 🐞 `KeyError` | agenda de contatos |
| 35 | ⚪ | Dicionários (parte 2) | `get`, `in`, `items`, `keys`/`values`, **lista de dicionários**, contar frequência | contar palavras de um texto; cadastro de produtos |
| 36 | ⚪ | Matrizes | lista de listas, linha e coluna | tabuleiro de jogo da velha (só exibir) |
| 37 | ⚪ | 🛠️ **Git + GitHub (parte 2): além do ritual** | `diff`, voltar atrás (`restore`, `revert`), **branches** e `merge`, `pull` e `clone`, Pull Request, README de projeto | mini-projeto 4 melhorado numa branch e juntado por Pull Request |
| 38 | ⚪ | Revisão leve | cola + refazer 1 exercício | cola da semana 5 completa |

## Semana 6: Fechamento da etapa

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 39 | ⚪ | Decompor problemas | quebrar um problema grande em funções pequenas | planejamento do projeto final, em pseudocódigo |
| 40 | ⚪ | 🏁 **Projeto final (parte 1)** | cadastro (lista de dicionários) | **Sistema de notas**: cadastrar alunos e notas |
| 41 | ⚪ | 🏁 **Projeto final (parte 2)** | cálculo, com testes pytest | média e situação (aprovado/recuperação/reprovado) |
| 42 | ⚪ | 🏁 **Projeto final (parte 3)** | relatório + publicação | relatório da turma, melhor aluno, validações, projeto no GitHub |
| 43 | ⚪ | 🎓 **Prova + retrospectiva** | revisão geral sem consulta | prova prática + detalhar dia a dia a Etapa 2 |

---

# Etapa 2: Estruturas de dados e algoritmos (rascunho)

**Por que:** é a base cobrada em entrevistas técnicas e em provas de concurso, e muda o jeito de pensar em problemas.
**Duração estimada:** ~45 dias · **O dia a dia será detalhado no Dia 43**, ajustado ao seu ritmo na Etapa 1.

**Hábitos que continuam:** toda estrutura é **implementada por você** (primeiro na mão, depois comparando com o que o Python já oferece), testada com **pytest** e versionada com **Git**.

| Módulo | Tema | Conteúdo | Exercícios típicos |
|---|---|---|---|
| 0 | Preparação: classes básicas | `class`, `__init__`, atributos, métodos, objeto que aponta para outro objeto (o "nó") | classe `ContaBancaria`, classe `No` |
| 1 | Complexidade (Big-O) | contar passos, O(1), O(n), O(n²), O(log n), por que isso importa | comparar duas soluções do mesmo problema |
| 2 | Pilha | LIFO, `push`/`pop`/`peek`, implementar com lista | parênteses balanceados, botão "desfazer" |
| 3 | Fila | FIFO, `enqueue`/`dequeue`, por que `pop(0)` é lento, `collections.deque` | fila de atendimento, fila de impressão |
| 4 | Recursão | caso base e caso recursivo, **pilha de chamadas**, fatorial, Fibonacci (e por que fica lento: memoização), somar uma lista, inverter texto | desenhar a pilha de chamadas no papel (teste de mesa recursivo) |
| 5 | Busca e ordenação | busca linear × **busca binária**; bubble, selection e insertion sort; merge sort (recursão em ação) | medir quantas comparações cada um faz |
| 6 | Lista encadeada | nós ligados, inserir, remover, percorrer (a ponte para árvores) | implementar a pilha e a fila com nós |
| 7 | Árvores | árvore binária de busca: **inserir, buscar, percorrer** (pré, em e pós-ordem), altura, percurso em largura usando **fila** | dicionário de palavras em árvore |
| 8 | Grafos | vértices e arestas, representar com dicionário (lista de adjacência), **busca em largura (BFS)** com fila, **busca em profundidade (DFS)** com pilha e com recursão, menor caminho sem peso | rotas entre cidades, amigos em comum |
| 9 | 🏁 Projeto da etapa | juntar tudo | **Resolvedor de labirinto** (BFS × DFS) com testes |

Repare como as peças se encaixam: a **pilha** explica a recursão, a **fila** faz o percurso em largura da árvore e do grafo, e a **recursão** faz o percurso em profundidade.

---

# Etapa 3: Projetos reais (esboço)

**Por que:** sair do terminal e construir um sistema com tudo que um projeto de verdade tem.
**Será detalhada no fim da Etapa 2.**

| Módulo | Tema | Conteúdo |
|---|---|---|
| 1 | Projeto Python de verdade | estrutura de pastas, módulos e `import`, ambiente virtual (`venv`), `pip` e `requirements.txt`, tratamento de erros (`try`/`except`) |
| 2 | Arquivos e dados | ler e escrever arquivos, CSV, **JSON** |
| 3 | HTTP | como a web funciona: requisição e resposta, métodos (GET, POST...), status (200, 404, 500), consumir uma API pública com `requests` |
| 4 | SQL | banco relacional, tabelas, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, começando com **SQLite** e usando pelo Python |
| 5 | HTML e CSS | estrutura de uma página, formulários, estilo, layout básico |
| 6 | Back-end | criar a sua própria API (Flask ou FastAPI) ligando HTTP + SQL + HTML |
| 7 | Docker | imagem, container, `Dockerfile`, subir app + banco com `docker compose` |
| 8 | 🏁 Projeto final | um sistema completo, versionado no GitHub, com testes, README e rodando em Docker |
