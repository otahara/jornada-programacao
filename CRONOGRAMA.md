# Cronograma da Etapa 1: Fundamentos de Lógica com Python

**Duração:** 43 dias (6 semanas) · **Ritmo:** cerca de 1h por dia

## 🎯 O que você vai fazer durante a Etapa 1

**Em toda sessão (cerca de 1h):**
1. **Revisão sem consulta** dos dias anteriores, mais um **aquecimento** que leva ao tema novo.
2. **Exemplo primeiro:** um código pequeno, explicado parte por parte.
3. **Exercícios que vão escalando**, digitados por você (sem autocompletar com IA) e com a saída exata pedida no enunciado.
4. **Ritual de fechamento:** `git add`, `git commit` e `git push`, deixando o dia publicado no GitHub.

**Ao longo das 6 semanas (43 dias):**

| Quantidade | O quê | Onde |
|---|---|---|
| 30 | dias de conteúdo novo, cada um com uma pasta em `aulas/` (exercícios + `resumo.md`) | todas as semanas |
| 6 | versões do **Organizador de estudos**, o projeto que cresce com você: uma por semana, só com o que você já aprendeu (veja a seção do projeto, logo abaixo) | Dias 8, 15, 23, 30, 38 e 39 a 42 |
| 5 | revisões leves: completar a cola (com as suas palavras) e refazer um exercício antigo sem olhar | Dias 9, 16, 24, 31 e 38 |
| 9 | tipos de erro treinados com programas quebrados para ler e consertar | Dia 5 + os dias marcados com 🐞 |
| 3 | ferramentas de programador: Git + GitHub, debugger do VS Code e pytest | Dias 4, 19, 32 e 37 |
| 1 | prova prática sem consulta + retrospectiva | Dia 43 |

## 🏁 Ao concluir a Etapa 1, você vai estar pronto para

Esta é a lista de conferência da prova e da retrospectiva do Dia 43: cada item é marcado só quando você consegue fazer **sem consulta**. Entre parênteses, os dias em que o assunto é ensinado.

**Escrever programas do zero**
- [ ] Criar um programa que conversa com o usuário: pergunta (`input`), converte para o tipo certo (`int` ou `float`), calcula e mostra o resultado formatado com f-string (Dias 3, 6 e 7).
- [ ] Fazer o programa **decidir**: `if`, `elif` e `else`, combinando condições com `and`, `or` e `not`, inclusive decisão dentro de decisão (Dias 10 a 14).
- [ ] Fazer o programa **repetir**: `while` quando não se sabe quantas vezes, `for` com `range` quando se sabe; contadores, acumuladores, `break`, `continue`, laço dentro de laço e menu que repete até o usuário escolher "sair" (Dias 17 a 22).
- [ ] **Guardar e organizar dados** em listas, dicionários, lista de dicionários e matrizes; percorrer, buscar, contar, filtrar e achar o maior e o menor (Dias 25 a 27 e 33 a 36).
- [ ] **Organizar o código em funções** com parâmetros e `return`, sabendo quando usar `print` e quando usar `return` (Dias 28 e 29).
- [ ] Pegar um problema grande, **quebrar em partes pequenas** e planejar em pseudocódigo antes de programar (Dia 39).

**Achar e consertar problemas**
- [ ] Ler uma mensagem de erro de baixo para cima e achar a linha que quebrou e a linha onde o problema começou (Dia 5).
- [ ] Reconhecer, na prática, `SyntaxError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`, `AttributeError`, `IndentationError`, `IndexError` e `KeyError` (Dia 5 e dias com 🐞).
- [ ] Descobrir por que um programa **roda sem erro, mas dá o resultado errado**: teste de mesa no papel e debugger com breakpoint, linha a linha (Dias 2 e 19).
- [ ] Escrever testes com pytest para provar que uma função faz o que promete, e entender o que um teste que falhou está dizendo (Dia 32).

**Trabalhar como programador**
- [ ] Versionar todo o trabalho com Git (`status`, `add`, `commit`, `push`, `log`, `diff`) e voltar atrás quando errar (`restore`, `revert`) (Dias 4 e 37).
- [ ] Fazer uma melhoria numa branch e juntar ao projeto por Pull Request; baixar um repositório com `clone` (Dia 37).
- [ ] Mostrar um **portfólio público** no GitHub: os exercícios de todos os dias e o **Organizador de estudos** em repositório próprio, com README, testes e um histórico de commits que mostra a evolução semana a semana.

**Seguir em frente**
- [ ] Começar a Etapa 2 (Orientação a Objetos), que parte do princípio de que tudo o que está acima já está firme.

**O que a Etapa 1 ainda não cobre**, para não criar expectativa errada: todos os programas rodam no **terminal** e os dados **somem quando o programa fecha**. Classes e o tratamento básico de erros com `try`/`except` ficam para a Etapa 2; pilha, fila, árvores, grafos e os algoritmos clássicos, para a Etapa 3; ler e gravar arquivos, organizar as bibliotecas de um projeto (`venv` e `pip`), banco de dados e páginas web, para a Etapa 4.

## 🗂️ O projeto da jornada: Organizador de estudos

Em vez de vários mini-projetos soltos, **um único projeto que cresce do começo ao fim do curso**: um organizador de estudos que registra as sessões, mostra o desempenho e diz o que revisar.

- **Para quem:** qualquer pessoa que estuda para alguma coisa (concurso, faculdade, idioma, programação). Cada pessoa cadastra as **suas** matérias e assuntos; nada fica preso a um tema.
- **Só com o que já foi aprendido:** cada versão usa apenas o que foi ensinado até aquele dia. Ideias para o futuro vão para uma lista no README do projeto, não para o código.
- **Repositório próprio:** o projeto ganha um repositório separado no GitHub, criado no Dia 8, para que o histórico de commits conte a evolução dele.
- **Ele cresce nas quatro etapas:** na Etapa 1, com o básico de Python; na Etapa 2, os dicionários viram classes; nas Etapas 2 e 3, cada conceito e cada estrutura de dados entram no projeto **quando fazem sentido de verdade** (quando não fizerem, são treinados só nos exercícios do módulo); na Etapa 4, ele sai do terminal e vira um sistema web.

| Etapa | Versão | O que o Organizador ganha |
|---|---|---|
| 1 | v1 (Dia 8) | registrar uma sessão de estudo e mostrar o resumo formatado |
| 1 | v2 (Dia 15) | classificar o desempenho e conferir a meta do dia |
| 1 | v3 (Dia 23) | menu que repete e totais do dia |
| 1 | v4 (Dia 30) | várias sessões em listas, matérias da própria pessoa, código em funções |
| 1 | v5 (Dias 37 e 38) | sessões como dicionários, total por matéria, testes, trabalho em branch + Pull Request |
| 1 | **1.0** (Dias 39 a 42) | assuntos personalizados, situação de cada assunto, relatório e quadro da semana |
| 2 | **2.0** | classes no lugar dos dicionários, sessões de tipos diferentes (questões e leitura), correção de sessões, dados validados e testes refeitos |
| 3 | **3.0** | desfazer, fila de revisões, assuntos com subassuntos, ordenação por desempenho, pré-requisitos entre assuntos e plano de estudos sugerido |
| 4 | **4.0** | dados salvos de verdade, banco PostgreSQL, telas na web com JavaScript, API própria com testes, segurança, Docker e testes automáticos a cada `push` |

## ✨ Boas práticas desde o primeiro dia

Código que funciona é o **mínimo**. Do primeiro exercício ao projeto, todo código segue as boas práticas de programação em geral e as do Python (que tem um guia oficial de estilo, a **PEP 8**).

- **Cada prática entra quando o assunto aparece** e, a partir dali, vira hábito, como as ferramentas.
- **Toda correção olha duas coisas:** se o resultado está certo **e** se o código segue as boas práticas. O que pode melhorar é marcado com ✨, sempre com o **porquê**.
- **Quando houver mais de um jeito de fazer, você aprende qual é o recomendado e por quê.**
- **Os exercícios antigos ficam como estão**, como registro da jornada. Já o **Organizador de estudos é melhorado** a cada versão com as práticas novas.

| Quando | Boas práticas que entram |
|---|---|
| Dias 1 a 5 (já vistas) | nomes descritivos em `snake_case`; commits pequenos com mensagem clara (Conventional Commits); `.gitignore` para o que não deve ser publicado; ler a mensagem de erro antes de mexer no código |
| Dia 6 | espaço ao redor dos operadores (`total = a + b`); parênteses para deixar a conta clara |
| Dia 7 | f-string em vez de juntar texto com `+` |
| Dia 8 | constantes em MAIÚSCULAS (`META_MINUTOS = 120`) em vez de números soltos no meio do código; comentário que explica o **porquê**, não o quê |
| Dia 11 | indentação de 4 espaços |
| Dias 12 a 14 | condições fáceis de ler: `if aprovado:` em vez de `if aprovado == True:`; decisão dentro de decisão só quando for necessário |
| Dias 17 e 18 | nunca confiar no que o usuário digitou: validar antes de usar |
| Dia 20 | `for` quando se sabe quantas vezes repetir, `while` quando não se sabe |
| Dias 28 e 29 | funções pequenas que fazem uma coisa só; nome com verbo (`calcular_media`); docstring dizendo o que a função faz; copiou e colou código, vira função; função de cálculo devolve com `return` em vez de imprimir |
| Dia 32 | `if __name__ == "__main__":`, para que o teste use as funções do arquivo sem rodar o programa inteiro; um teste para cada comportamento, com um nome que diz o que ele confere |
| Dia 37 | uma branch para cada melhoria; Pull Request com descrição; README de projeto |
| Dia 39 | planejar antes de programar |
| Etapa 2 | nomes de classe em `PascalCase`; anotação de tipos (`def media(notas: list[float]) -> float:`); uma classe com uma responsabilidade só; criar todos os atributos no `__init__`; atributo simples até precisar de regra, e só então `@property`; `__repr__` que ajude a depurar; levantar o erro mais específico e nunca usar `except` sem dizer qual erro; herança só quando for mesmo "é um" |
| Etapa 3 | escolher a estrutura de dados pelo custo (Big-O) |
| Etapa 4 | projeto organizado em pastas e módulos; `venv` e `requirements.txt`; log em vez de `print` para registrar erros; senhas e chaves fora do código; um **verificador automático de estilo** rodando no projeto e no CI |

### Regras do cronograma
- **"Dia" é uma sessão de estudo, não um dia do calendário.** Se pular um dia, continue de onde parou. Nada de culpa.
- **Só avança quando entregar os exercícios do dia.** Se travar, o mesmo dia pode durar duas sessões.
- **Todo dia começa com revisão sem consulta:** perguntas sobre os dias anteriores **e** um aquecimento (teste de mesa ou exercício básico) que sirva de **ponte para o tema do dia**: o resultado ou a dificuldade dele leva naturalmente ao conceito novo.
- **O último dia de cada semana é de revisão leve:** reler e completar a **cola** (um caderno de anotações escrito com as suas palavras) e refazer **um** exercício antigo sem olhar. Pode ser curto.
- **Toda semana tem dia de projeto (🧩):** o Organizador de estudos ganha uma versão nova com o que foi visto naquela semana.
- **Ferramentas entram aos poucos (🛠️), no momento em que fazem sentido**, e viram hábito a partir dali:
  - a partir do **Dia 4 (Git + GitHub)**, toda sessão termina com o **ritual de fechamento**: `git add`, `git commit` e `git push`, deixando o progresso do dia publicado no GitHub;
  - a partir do **Dia 19 (Debugger)**, quando um laço der resultado estranho, o primeiro passo é rodar com breakpoint;
  - a partir do **Dia 32 (Testes)**, toda função com `return` ganha pelo menos um teste.
- **Erros novos entram no dia em que podem acontecer (🐞)**, sem aula própria: nesse dia, a pasta da aula ganha uma subpasta `erros/` com programas quebrados para ler, entender e consertar. Os erros básicos (`SyntaxError`, `NameError`, `TypeError`, `ValueError`, `ZeroDivisionError`) são treinados no Dia 5.
- **Cada etapa tem um repositório novo e uma pasta nova**, ao lado da pasta da etapa anterior, nunca dentro dela. O repositório anterior continua público, como registro da jornada, e só recebe os links de navegação (veja abaixo). O **Organizador de estudos** fica no repositório próprio dele, que não muda de etapa para etapa, para o histórico de commits contar a evolução.
- **No último dia de cada etapa, a IA monta um kit de passagem** para o repositório novo, levando só o que importa:
  - `CLAUDE.md` com as regras permanentes (boas práticas, estrela e alerta), sem o histórico de quando e por que cada regra nasceu, mais as notas da memória da IA que ainda valerem, porque essa memória fica presa à pasta antiga;
  - diário novo e enxuto: quem é o aluno, método de ensino, organização da pasta e um **Ponto de partida** (a lista "pronto para" marcada, as boas práticas que já podem ser cobradas, os assuntos em alerta 🚨 e as observações sobre o aluno que continuam valendo), sem detalhes aula por aula;
  - painel de atenção só com os alertas abertos, com os links trocados pelos endereços do repositório antigo no GitHub;
  - `CRONOGRAMA.md` só da etapa nova, com um resumo de uma linha por etapa (as anteriores com link para o repositório delas, as futuras como esboço);
  - `ETAPAS-FUTURAS.md` com os rascunhos detalhados das próximas etapas, lido só no último dia da etapa;
  - README novo, com a navegação entre as etapas.
  
  A cola fica na pasta da etapa em que foi escrita e não é copiada nem resumida.
- **O kit é montado na pasta nova do computador**, porque a pasta `privado/` não vai para o GitHub. O `.gitignore` novo continua escondendo `privado/` e `CLAUDE.md`. Antes de fechar a etapa, a IA lembra de fazer o **backup** da pasta `privado/` da etapa que terminou: é a única cópia da cola.
- **Na pasta nova, a IA lê só os arquivos daquela pasta** e não busca nada no repositório antigo, a não ser que o aluno peça. Os links entre os repositórios são para as pessoas navegarem.
- **Os repositórios conversam entre si, nos dois sentidos**, sempre com o endereço completo do GitHub, porque um link relativo não sai do próprio repositório:
  - **README de cada etapa:** no topo, a linha `⬅️ Etapa anterior · ➡️ Próxima etapa`; na seção "A jornada", a mesma tabela em todos os repositórios, com o link de cada etapa e a indicação de qual é a atual;
  - **Topo do `CRONOGRAMA.md` de cada etapa:** a mesma navegação;
  - **Última e primeira aula:** o `resumo.md` do último dia aponta para o primeiro dia da etapa seguinte, e o do primeiro dia aponta de volta;
  - **Conceito retomado:** quando um `resumo.md` usa algo de outra etapa, ele traz o link para a aula em que o assunto foi ensinado;
  - **Organizador de estudos:** o README dele tem uma tabela com cada versão e a etapa em que ela nasceu, com link, e o README de cada etapa aponta para o Organizador;
  - **Ordem no último dia:** criar o repositório novo no GitHub (para ter o endereço), fazer no repositório antigo um último commit só com os links para a etapa nova, montar o kit e fazer o backup.

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
| 6 | ✅ | Tipos e operadores aritméticos | `int`, `float`, `str`, `bool`, `type()`, `+ - * / // % **` | calculadora de operações |
| 7 | ✅ | Trabalhando com texto | concatenação, **f-strings**, `len`, `upper`/`lower`; 🐞 `AttributeError` | cartão de apresentação formatado |
| 8 | ✅ | 🧩 **Organizador de estudos v1** | criar o repositório do projeto (repetindo o ritual do Dia 4) e juntar tudo da semana: `input`, tipos, `//` e `%` para transformar minutos em horas, f-strings | **registrar uma sessão de estudo** (matéria, minutos, questões feitas e acertadas) e mostrar o resumo formatado, com horas e percentual de acertos |
| 9 | ✅ | Revisão leve | cola + refazer 1 exercício + `git log` da semana | cola da semana 1 completa |

## Semana 2: Decisão (o programa começa a "pensar")

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 10 | ⚪ | Comparações | `== != > < >= <=`, valores `True`/`False` | exercícios de "verdadeiro ou falso?" |
| 11 | ⚪ | `if` / `else` | decisão simples, **indentação**, bloco de código; 🐞 `IndentationError` | par ou ímpar, maior de idade |
| 12 | ⚪ | `elif` | várias condições em sequência, a ordem importa | faixa etária, conceito de nota (A/B/C) |
| 13 | ⚪ | Operadores lógicos | `and`, `or`, `not`, tabela-verdade | validação de login (usuário **e** senha) |
| 14 | ⚪ | Treino de decisão | combinar tudo, decisão dentro de decisão | maior de 3 números, triângulo válido |
| 15 | ⚪ | 🧩 **Organizador de estudos v2** | decisão aplicada ao projeto | **classificar o desempenho** da sessão (ex.: abaixo de 60% de acertos = revisar logo), conferir a meta de minutos do dia e recusar dados impossíveis (mais acertos do que questões) |
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
| 23 | ⚪ | 🧩 **Organizador de estudos v3** | repetição aplicada ao projeto | **menu que repete** (registrar sessão, ver totais do dia, sair), total de horas e média de acertos do dia, pedir de novo quando a entrada for inválida |
| 24 | ⚪ | Revisão leve | cola + refazer 1 exercício | cola da semana 3 completa |

## Semana 4: Listas e funções (organizando o código)

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 25 | ⚪ | Listas (parte 1) | criar, acessar por índice (começa no **0**), índice negativo, `append`, `len`; 🐞 `IndexError` | lista de compras |
| 26 | ⚪ | Percorrer listas | `for item in lista`, soma, maior e menor | estatísticas de uma lista de notas |
| 27 | ⚪ | Listas (parte 2) | `in`, `insert`, `remove`, `pop`, `index`, `sort`, fatiamento `[a:b]`; listas são **mutáveis** | fila de atendimento simples (entra no fim, sai do começo) |
| 28 | ⚪ | Funções (parte 1) | `def`, chamar, parâmetros, por que funções existem | funções de saudação e de conversão |
| 29 | ⚪ | Funções (parte 2) | `return`, diferença entre `print` e `return`, escopo | funções de cálculo reaproveitáveis |
| 30 | ⚪ | 🧩 **Organizador de estudos v4** | listas e funções aplicadas ao projeto | **várias sessões guardadas em listas**, matérias cadastradas pela própria pessoa, código organizado em funções (registrar, relatório, percentual) |
| 31 | ⚪ | Revisão leve | cola + refazer 1 exercício | cola da semana 4 completa |

## Semana 5: Testes, dicionários e Git avançado

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 32 | ⚪ | 🛠️ **Testes automatizados** | `assert`, por que testar, instalar e rodar o **pytest**, arquivo `test_*.py`, ler um teste que falhou | testes para as funções do Dia 29 |
| 33 | ⚪ | Problemas clássicos | busca, contagem, filtro (o "kit básico" de todo programador), já com testes | buscar nome, contar aprovados, com pytest |
| 34 | ⚪ | Dicionários (parte 1) | pares chave → valor, acessar, adicionar, alterar, percorrer; 🐞 `KeyError` | agenda de contatos |
| 35 | ⚪ | Dicionários (parte 2) | `get`, `in`, `items`, `keys`/`values`, **lista de dicionários**, contar frequência | contar palavras de um texto; cadastro de produtos |
| 36 | ⚪ | Matrizes | lista de listas, linha e coluna | tabuleiro de jogo da velha (só exibir) |
| 37 | ⚪ | 🛠️ **Git + GitHub (parte 2): além do ritual** | `diff`, voltar atrás (`restore`, `revert`), **branches** e `merge`, `pull` e `clone`, Pull Request, README de projeto | uma melhoria pequena no Organizador de estudos, feita numa branch e juntada por Pull Request |
| 38 | ⚪ | Revisão leve + 🧩 **Organizador de estudos v5** | cola + dicionários e testes aplicados ao projeto, numa branch nova juntada por Pull Request (o projeto faz o papel do "exercício antigo"; o dia pode levar duas sessões) | cola da semana 5 completa + **cada sessão vira um dicionário** (lista de dicionários), total de horas por matéria e testes pytest das funções de cálculo |

## Semana 6: Fechamento da etapa

| Dia | Status | Tema | O que você vai aprender | Entrega |
|---|---|---|---|---|
| 39 | ⚪ | Decompor problemas | quebrar um problema grande em funções pequenas | planejamento do Organizador de estudos 1.0, em pseudocódigo |
| 40 | ⚪ | 🏁 **Organizador de estudos 1.0 (parte 1)** | cadastro personalizado (lista de dicionários) | **matérias e assuntos** cadastrados pela pessoa, para qualquer tipo de estudo |
| 41 | ⚪ | 🏁 **Organizador de estudos 1.0 (parte 2)** | cálculo, com testes pytest | desempenho por assunto e situação (dominado / em progresso / revisar) |
| 42 | ⚪ | 🏁 **Organizador de estudos 1.0 (parte 3)** | relatório + publicação | relatório da semana, quadro dias × matérias (matriz), validações, README do projeto e versão 1.0 publicada no GitHub |
| 43 | ⚪ | 🎓 **Prova + retrospectiva** | revisão geral sem consulta | prova prática + marcar a lista "pronto para" (no topo) + detalhar dia a dia a Etapa 2 (Orientação a Objetos) + montar o kit de passagem para a Etapa 2 (o dia pode levar duas sessões) |

---

# Etapa 2: Orientação a Objetos (rascunho)

**Por que:** organizar programas maiores juntando dados e comportamento, e preparar a Etapa 3, em que cada estrutura de dados é uma classe.
**Duração estimada:** ~40 dias (cerca de 6 semanas, com as revisões leves) · **O dia a dia será detalhado no Dia 43**, ajustado ao seu ritmo na Etapa 1.

**Hábitos que continuam:** todo método com regra ganha teste no **pytest**; **Git** em toda sessão, com branch e Pull Request em cada melhoria do projeto; o **debugger** mostra os atributos do objeto no painel de variáveis; e toda correção segue olhando resultado e **boas práticas**. O **Organizador de estudos troca os dicionários por classes**: cada conceito entra no projeto quando faz sentido de verdade; quando não faz, é treinado só nos exercícios do módulo.

| Módulo | Tema | Conteúdo | Exercícios típicos | No Organizador de estudos |
|---|---|---|---|---|
| 1 | Classe e objeto | classe × objeto, `__init__`, `self`, atributos, métodos, parâmetro com valor padrão, `PascalCase`, anotação de tipos | `Livro`, depois `ContaBancaria` com `depositar`. 🐞 `TypeError` por faltar o `self` ou um argumento; `AttributeError` por escrever `nome = nome` sem `self` | `Sessao` substitui o dicionário da sessão, com `percentual()` |
| 2 | Objetos juntos | lista de objetos, objeto guardando outros objetos | `Turma` com vários `Aluno` e a média da turma. 🐞 `AttributeError` por pedir `.nome` à lista; `print` que mostra `<__main__.Aluno object at 0x...>` (a ponte para o Módulo 4) | `Assunto` guarda sessões e `Materia` guarda assuntos; acaba a lista de dicionários |
| 3 | Atributo de instância × atributo de classe | quando o valor é de cada objeto e quando é de todos | `Funcionario` com a empresa em comum; contador de objetos criados. 🐞 sem mensagem de erro: lista como atributo de classe, compartilhada por todos os objetos | limites da situação (`LIMITE_REVISAR`) como atributos de classe de `Assunto` |
| 4 | Métodos especiais | `__str__`, `__repr__`, `__eq__` | `Produto` com `print` legível; `Aluno` igual por matrícula. 🐞 `TypeError` porque o `__str__` não devolveu texto; `TypeError: unhashable type` depois de criar o `__eq__` | `__str__` no lugar das funções de exibir; `__eq__` recusa "matemática" quando "Matemática" já existe |
| 5 | Levantar e tratar erros | `raise`, `try`/`except` básico, `pytest.raises` | `sacar` acima do saldo levanta `ValueError`; o menu trata e pergunta de novo. 🐞 sem mensagem de erro: `try` grande demais, que esconde o erro verdadeiro | `Sessao` recusa dados impossíveis (mais acertos do que questões) e o menu trata o erro |
| 6 | Encapsulamento | convenção do `_` e do `__`, `@property`, setter com validação | `Termometro` que recusa valor abaixo do zero absoluto; `saldo` só para leitura. 🐞 `AttributeError` em `__saldo` e em property sem setter; `RecursionError` do setter que chama a si mesmo (só reconhecer) | `percentual` vira property; nova opção "corrigir sessão", validada pelo setter; `_sessoes` passa a ser interno |
| 7 | `@classmethod` e `@staticmethod` | outra forma de criar o objeto; função que pertence ao assunto da classe; quando uma função comum é melhor | `Temperatura.de_fahrenheit(212)`, `Data.de_texto("04/11/2026")`, `Data.eh_bissexto(2028)`. 🐞 `TypeError` por esquecer o `cls` ou o decorador | `Sessao.de_horas(...)`; o `@staticmethod` fica só nos exercícios, porque no projeto uma função comum resolve |
| 8 | Herança e `super()` | classe filha, sobrescrever método, `super()`, exceção própria como exemplo; retomar o `cls` do Módulo 7 | `Funcionario` e `Gerente`; `Veiculo` e `Moto`. 🐞 `AttributeError` por esquecer o `super().__init__()`; `TypeError` por faltar argumento no `super()` | `SessaoDeQuestoes` e `SessaoDeLeitura`: agora dá para registrar videoaula ou leitura, sem questões |
| 9 | Polimorfismo | o mesmo método se comportando diferente em cada classe; `isinstance` e por que evitá-lo | `area()` em várias formas; folha de pagamento com tipos misturados. 🐞 `AttributeError` quando uma classe não tem o método | o relatório chama `sessao.resumo()` sem um `if` para cada tipo |
| 10 | Classes abstratas com `abc` | `ABC`, `@abstractmethod`, obrigar as classes filhas a implementar um método | `Pagamento` com `Pix` e `Cartao`. 🐞 `TypeError: Can't instantiate abstract class` | `Sessao` vira abstrata: toda sessão é de um tipo |
| 11 | Composição × herança | "é um" × "tem um", como decidir | `Carro` tem `Motor`; `Playlist` herdando de `list` × guardando uma lista. 🐞 sem mensagem de erro: métodos herdados de `list` furam a regra da playlist | `Organizador` guarda as matérias; `Relatorio` sai dele (uma responsabilidade só) |
| 12 | Dataclasses | `@dataclass`, `field(default_factory=list)`, `__post_init__`; comparar com a versão escrita à mão | reescrever `Produto` e contar as linhas. 🐞 `ValueError` por lista como valor padrão; `TypeError` por campo sem padrão depois de campo com padrão | só `Materia` vira dataclass; `Sessao` continua como está por causa dos setters, e essa comparação é a lição |
| 13 | 🏁 Projeto da etapa | juntar tudo, numa branch com Pull Request | | **Organizador de estudos 2.0**: por dentro, tudo em classes; por fora, sessões de questões e de leitura, correção de sessões e recusa de assunto repetido; os testes garantem que o que já funcionava continua funcionando |

---

# Etapa 3: Estruturas de dados e algoritmos (rascunho)

**Por que:** é a base cobrada em entrevistas técnicas e em provas de concurso, e muda o jeito de pensar em problemas.
**Duração estimada:** ~42 dias · **O dia a dia será detalhado no fim da Etapa 2**, ajustado ao seu ritmo até ali.

**Hábitos que continuam:** toda estrutura é **implementada por você** (primeiro na mão, depois comparando com o que o Python já oferece), testada com **pytest** e versionada com **Git**. E o **Organizador de estudos continua crescendo**: em cada módulo, a estrutura nova entra no projeto (coluna da direita).

| Módulo | Tema | Conteúdo | Exercícios típicos | No Organizador de estudos |
|---|---|---|---|---|
| 1 | Complexidade (Big-O) | contar passos, O(1), O(n), O(n²), O(log n), por que isso importa | comparar duas soluções do mesmo problema | comparar duas formas de achar o assunto com pior desempenho |
| 2 | Pilha | LIFO, `push`/`pop`/`peek`, implementar com lista | parênteses balanceados, botão "desfazer" | **desfazer** o último registro |
| 3 | Fila | FIFO, `enqueue`/`dequeue`, por que `pop(0)` é lento, `collections.deque` | fila de atendimento, fila de impressão | **fila de revisões**: o assunto estudado entra no fim e o próximo a revisar sai do começo |
| 4 | Recursão | caso base e caso recursivo, **pilha de chamadas**, fatorial, Fibonacci (e por que fica lento: memoização), somar uma lista, inverter texto | desenhar a pilha de chamadas no papel (teste de mesa recursivo) | **assuntos com subassuntos** (ex.: matéria → tema → tópico) e o total de horas de um assunto somando todos os de dentro |
| 5 | Busca e ordenação | busca linear × **busca binária**; bubble, selection e insertion sort; merge sort (recursão em ação) | medir quantas comparações cada um faz | **ordenar** os assuntos pelo desempenho (o pior primeiro) e buscar um assunto pelo nome |
| 6 | Lista encadeada | a classe `No`, o objeto que aponta para outro objeto, nós ligados, inserir, remover, percorrer (a ponte para árvores) | implementar a pilha e a fila com nós | trocar a pilha do "desfazer" e a fila de revisões por versões feitas por você, com nós |
| 7 | Árvores | árvore binária de busca: **inserir, buscar, percorrer** (pré, em e pós-ordem), altura, percurso em largura usando **fila** | dicionário de palavras em árvore | o conteúdo de estudo (edital, ementa) como **árvore**: exibir com os percursos e buscar assuntos |
| 8 | Grafos | vértices e arestas, representar com dicionário (lista de adjacência), **busca em largura (BFS)** com fila, **busca em profundidade (DFS)** com pilha e com recursão, menor caminho sem peso | rotas entre cidades, amigos em comum | **pré-requisitos** entre assuntos ("para estudar X, antes preciso de Y") e o menor caminho até um assunto |
| 9 | 🏁 Projeto da etapa | juntar tudo | | **Organizador de estudos 3.0**: plano de estudos sugerido, que respeita os pré-requisitos e prioriza as revisões dos assuntos com pior desempenho, com testes |

Repare como as peças se encaixam: cada estrutura é uma **classe** (Etapa 2), a **pilha** explica a recursão, a **fila** faz o percurso em largura da árvore e do grafo, e a **recursão** faz o percurso em profundidade.

---

# Etapa 4: Projetos reais (esboço)

**Por que:** sair do terminal e construir um sistema com tudo que um projeto de verdade tem.
**Será detalhada no fim da Etapa 3.**

| Módulo | Tema | Conteúdo | No Organizador de estudos |
|---|---|---|---|
| 1 | Projeto Python de verdade | estrutura de pastas, módulos e `import`, ambiente virtual (`venv`), `pip` e `requirements.txt`, tratamento de erros em um projeto maior (o `try`/`except` básico vem da Etapa 2), **logs** (registrar o que aconteceu e o que deu errado), verificador automático de estilo (PEP 8) | o projeto é dividido em pastas e módulos, e os erros tratados ficam registrados num log |
| 2 | Arquivos e dados | ler e escrever arquivos, CSV, **JSON** | os dados são salvos em JSON e **param de sumir** quando o programa fecha; relatório exportado em CSV |
| 3 | HTTP | como a web funciona: requisição e resposta, métodos (GET, POST...), status (200, 404, 500), consumir uma API pública com `requests` | buscar dados de uma API pública (ex.: feriados, para montar o calendário de revisões) |
| 4 | SQL com **PostgreSQL** | banco relacional, instalar o PostgreSQL, tabelas, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, usar o banco pelo Python; o SQL aprendido aqui vale, quase igual, para os outros bancos | o JSON é trocado por um banco PostgreSQL |
| 5 | Front-end (parte 1): HTML e CSS | estrutura de uma página, formulários, estilo, layout que funciona também no **celular** | as telas do organizador |
| 6 | Back-end | criar a sua própria API (Flask ou FastAPI) ligando HTTP + SQL + HTML; **migrações** (mudar as tabelas sem perder dados); **testes da API** com pytest | a API do organizador, ligando as telas ao banco, com testes |
| 7 | Front-end (parte 2): **JavaScript** | a linguagem que roda no navegador: a lógica é a mesma do Python, muda a escrita; mexer na página, reagir a cliques, chamar a sua própria API | telas que respondem na hora, sem recarregar a página |
| 8 | 🔒 **Segurança** | senhas e chaves **fora do código** (variáveis de ambiente), validar tudo no back-end, os ataques mais comuns (SQL injection, XSS) e como se proteger | revisão de segurança do organizador inteiro |
| 9 | Docker | imagem, container, `Dockerfile`, subir app + banco com `docker compose` | o organizador e o PostgreSQL rodando com `docker compose` |
| 10 | **CI** (integração contínua) | o GitHub roda os testes e o verificador de estilo sozinho a cada `push` e avisa quando algo quebrou (GitHub Actions) | todo `push` do organizador passa pelos testes e pela verificação de estilo automaticamente |
| 11 | 🏁 Projeto final | um sistema completo, versionado no GitHub, com testes rodando no CI, README e rodando em Docker | **Organizador de estudos 4.0** na web |

---

# Etapa 5: SaaS (esboço)

**Por que:** transformar um sistema web num **serviço de verdade**, usado por outras pessoas pela internet. O produto ainda não está definido: pode ser o Organizador de estudos ou outra ideia.
**Será detalhada no fim da Etapa 4.**

| Tema | Conteúdo |
|---|---|
| Usuários | criar conta, login, senhas guardadas com hash, cada pessoa vendo só os seus dados, recuperar a senha por e-mail |
| Hospedagem | colocar o sistema na internet, domínio próprio, conexão protegida (HTTPS) |
| Pagamento | planos e assinatura |
| Lei e privacidade | LGPD, política de privacidade e termos de uso |
| Manter vivo | backup do banco, monitorar erros e desempenho, e-mails automáticos (ex.: lembrete de revisão) |
