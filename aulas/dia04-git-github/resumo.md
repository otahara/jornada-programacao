# Dia 4: Git + GitHub (parte 1): o ritual diário

## ✅ O que aprendi neste dia

- **Git** é um programa de **controle de versão**: roda no meu computador e guarda o histórico do projeto em **commits** (fotos do projeto)
- **GitHub** é um site que **hospeda** repositórios Git: backup, vitrine e trabalho em equipe. Git está para o GitHub assim como um vídeo está para o YouTube
- `git init` transforma a pasta num **repositório**, criando a pasta oculta `.git`, onde fica todo o histórico
- `git status` mostra como está o projeto e quase sempre diz qual é o próximo comando
- O `.gitignore` lista o que o Git deve fingir que não existe (arquivos privados, arquivos gerados pelo Python)
- Commit em **dois tempos**: `git add` escolhe o que entra na foto (🔴 → 🟢) e `git commit -m "mensagem"` tira a foto
- `git log` mostra o histórico: **hash** (o "RG" do commit), autor, data e mensagem. `HEAD` = "você está aqui"
- **Remote** é uma cópia do repositório em outro lugar. `origin` é o apelido padrão dele, e `main` é o nome padrão da branch principal
- `git push` envia os commits para o GitHub. **Commit sozinho não publica nada**
- Markdown para escrever o `README.md`: `#` títulos, `**negrito**`, `-` listas, `[texto](link)` e tabelas
- Na revisão: todo dado tem **tipo** e **valor**, e aspas sempre querem dizer texto. `int(7.5)` dá `7`, mas `int("7.5")` dá erro

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- **TypeError × ValueError, de novo.** Troquei os dois na revisão. O que destravou foi separar **tipo** (que espécie de dado: `int`, `float`, `str`) de **valor** (o conteúdo). `"7.5"` tem aspas, então o tipo é **texto**. O `int()` aceita texto (tipo certo), mas não esse conteúdo (valor ruim): **ValueError**. Já `10 - "3"` não funciona com nenhum texto: **TypeError**.
- **Não preciso decorar o erro de cabeça.** Num programa grande, o Python diz o erro, a linha e o valor que causou o problema. O trabalho é **ler a mensagem de baixo para cima** e perguntar: "de onde veio esse valor ruim?"
- **"Subir" é para o GitHub (`push`), não para o Git.** O commit fica só no meu computador até o `push`.
- **O repositório no GitHub precisa nascer vazio** (sem README, `.gitignore` ou licença), quando o projeto já existe no computador. Senão, as duas versões entram em conflito.
- **Não saber o que escrever no README.** Responder perguntas simples (por que este repositório existe? quem sou eu? por que agora? por que público?) e transformar cada resposta numa seção resolveu.

---

## Por que versionar?

Um programa funcionava, eu "melhorei", ele quebrou e eu não lembro como era. Sem versionamento, não tem volta. Com Git, cada commit é uma **foto** do projeto que fica guardada para sempre.

## Os comandos do dia

| Comando | O que faz | Quando usar |
|---|---|---|
| `git init` | cria o repositório (a pasta `.git`) | uma vez por projeto |
| `git status` | mostra o estado dos arquivos | **sempre**, antes e depois de tudo |
| `git add .` | coloca tudo na próxima foto (o `.` = esta pasta para baixo) | antes do commit |
| `git commit -m "..."` | tira a foto, com uma mensagem | quando algo estiver pronto |
| `git log` | mostra o histórico de commits | para conferir |
| `git remote add origin URL` | salva o endereço do GitHub com o apelido `origin` | uma vez por projeto |
| `git push -u origin main` | envia e grava a ligação (`-u`) | no primeiro envio |
| `git push` | envia os commits novos | nos envios seguintes |

## Lendo o `git status`

```
Untracked files:          ← 🔴 fora da foto: o Git vê, mas não acompanha
        README.md

Changes to be committed:  ← 🟢 dentro da foto: vai entrar no próximo commit
        new file:   README.md
```

**Vermelho = fora da foto. Verde = dentro da foto.**

## O `.gitignore`

```
privado/      ← a pasta inteira (a barra no fim indica pasta)
__pycache__/  ← arquivos que o Python cria sozinho
*.pyc         ← * = qualquer nome: todo arquivo terminado em .pyc
```

O que vai para um repositório público fica **no histórico para sempre**, mesmo que seja apagado depois. Por isso: **`git status` antes de todo commit**.

## Boa mensagem de commit

- Curta, numa linha, dizendo **o que** foi feito
- ✅ `"Cria o README e publica os Dias 1 a 3"`
- ❌ `"coisas"`, `"atualização"`, `"agora vai"`

## Perguntas que surgiram

- **Se eu mudar a pasta de lugar, perco o histórico?** Não. O histórico mora em `.git`, **dentro** da pasta do projeto. Mova a pasta inteira, com o VS Code fechado.
- **Posso chamar o `origin` de `banana`?** Pode, mas não deve: é **convenção**, como o `snake_case`. Tutoriais, colegas e entrevistas assumem `origin` e `main`.
- **Em outro repositório continua `origin` e `main`?** Sim. Cada repositório tem os seus, guardados no seu próprio `.git`, e um não enxerga o outro.

## 🔁 O ritual de fechamento (a partir de hoje, em toda sessão)

```
git status                      ← conferir: nada de privado aparece?
git add .
git commit -m "mensagem clara"
git push
```

## Da revisão: tipo × valor

| No código | Tipo | Por quê |
|---|---|---|
| `7.5` | `float` | número com ponto |
| `"7.5"` | `str` | **tem aspas**: é texto, mesmo parecendo número |
| `int("30")` | `int` | o texto virou inteiro |

- `int(7.9)` → `7`: **corta**, não arredonda
- `int("7.5")` → `ValueError`: com texto, o `int()` só aceita um inteiro escrito
- `int(float("7.5"))` → `7`: os dois passos feitos de propósito, de dentro para fora
- `invalid literal for int() with base 10: 'dois'` = "o texto `'dois'` não serve para o `int()`, que lê dígitos de 0 a 9"
- `SyntaxError: unterminated string literal` = abri aspas e não fechei
