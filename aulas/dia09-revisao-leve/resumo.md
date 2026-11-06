# Dia 9: Revisão leve

Revisão completa de Git e GitHub, na prática, em pastas de treino. Depois: backup das minhas anotações privadas em um repositório separado, cola da semana, um exercício antigo refeito sem olhar e leitura do `git log` da semana.

## ✅ O que aprendi neste dia

- **Um repositório é uma pasta com um `.git` dentro.** Ele vale para aquela pasta e para tudo o que está dentro dela. O Git procura o `.git` na pasta atual e nas de cima.
- **`git add` recebe um caminho:** um arquivo, vários arquivos, uma pasta ou `.`. `git add banana` só funciona se existir algo chamado `banana`.
- **O `.` significa "esta pasta aqui"**, não "o projeto inteiro". O resultado depende de onde o terminal está.
- **Tirar um arquivo da lista do próximo commit:** `git rm --cached <arquivo>` antes do primeiro commit e `git restore --staged <arquivo>` depois dele. O `git status` mostra o certo para cada momento.
- **`-m` é a opção da mensagem do commit.** Sem ela, o Git abre o editor; se a mensagem ficar vazia, o commit é cancelado. As opções são fixas: `-laranja` dá erro.
- **Mensagem de commit:** descreve o motivo único da mudança, não a lista de arquivos. Se precisar de um "e" para resumir, provavelmente são dois commits.
- **`origin` é o apelido de um endereço.** É uma convenção: o primeiro remote quase sempre se chama assim, mas um repositório pode ter vários.
- **Os dois erros do primeiro `push`:** `No configured push destination` pede `git remote add origin URL`; `no upstream branch` pede `git push -u origin main`, necessário uma vez por branch.
- **Hash × mensagem:** `9f04043` é a identificação do commit, criada pelo Git. A mensagem é a descrição, escrita por mim.
- **Branch é um nome que aponta para o último commit de uma linha.** Os nomes andam: `main` com o commit, `origin/main` com o `push`. Nomes separados no `git log --oneline` indicam commit ainda não enviado.
- **`git init` na pasta errada:** o conserto é apagar só o `.git` (`Remove-Item -Recurse -Force .git`) e repetir o `init` na pasta certa. Os arquivos continuam na pasta; o que se perde é o histórico que só existia localmente.
- **O Git para no primeiro `.git` que encontra.** Sem `.git` na pasta atual, ele sobe para a pasta de cima. Por isso, `git status` sem erro não prova que aquela pasta tem repositório próprio. `git remote -v` mostra a qual remote o repositório encontrado está ligado.
- **Cada repositório tem os próprios remotes.** Um repositório novo não tem nenhum, mesmo dentro da pasta de outro.
- **`git status` não lista todos os arquivos:** mostra só o que está diferente do último commit. Depois do commit, o arquivo some da lista porque não tem pendência.
- **Backup com Git:** funciona bem para poucos arquivos de texto, com histórico, mas é manual: só está protegido o que chegou ao GitHub com `push`. Senha nunca entra, nem em repositório privado, porque quem entra na conta vê e ela continua nos commits antigos.
- ✨ **Nome de arquivo também é documentação:** `refazer_dia03_ex04_dividir_conta.py` diz o que é e de onde veio; `refazer_ex04.py` não diz.
- ✨ **`git add`:** rodar `git status` primeiro. Usar `.` na raiz quando tudo pertence à mesma mudança, e o nome do arquivo quando só uma parte pertence.

---

## ⚠️ Pontos de atenção

- **O `add .` em uma subpasta não dá erro:** adiciona só o que está lá dentro, e por isso passa despercebido.
- **Antes de apagar um `.git`, ler o prompt:** o comando apaga o histórico do repositório da pasta atual, e os commits não enviados se perdem.
- **Commit e branch são coisas diferentes:** precisei ver os nomes andando no `git log --oneline` para entender.
- **`git restore --staged` não funciona antes do primeiro commit:** dá `fatal: could not resolve 'HEAD'`. Antes dele, o comando é `git rm --cached`, que o próprio `git status` mostra.
- **Ler com atenção a linha certa do `git log`:** peguei o commit logo abaixo do que procurava.

---

## 🧑‍🏫 Relatório do professor

### Formato

Revisão guiada, a meu pedido: o professor explica, eu executo no terminal e provoco os erros, e resolvemos cada um passo a passo. Não houve perguntas de cobrança.

### Blocos guiados

**Bloco 1: pasta e `git init`.** ✅ Todos os passos certos. Rodei o `ls` comum antes do `ls -Force` e vi o `.git` aparecer só no segundo.

**Bloco 2: `git add`.** ✅ Provoquei o `pathspec` com `banana` e o `add .` em subpasta. No fim, usei o nome do único arquivo que faltava em vez do `.`.

> *Perguntei:* "se eu quiser tirar o programa.py do repositório antes de commitar tem jeito?"

Tem, e o comando já estava no `git status`: `git rm --cached`. O arquivo ainda não estava no repositório, só na lista do próximo commit. Testei, e ele continuou na pasta.

**Bloco 3: `git commit`.** ✅ Testei `-laranja` e o `commit` sem `-m`. ⚠️ Não rodei o `git commit -m` sem mensagem, que estava no roteiro.

**Bloco 4: primeiro erro do `push`.** ✅ Resolvido com `git remote add`.

> *Perguntei:* "Se origin é a convenção por que o comando do console não aparece origin já recomendado ao invés de `<name>`? 101% dos git remote add terão origin?"

Não são 101%: um repositório pode ter mais de um remote, como `origin` e `upstream`, e cada um precisa de um apelido. O professor também corrigiu uma fala dele: o comando estava no meio da mensagem, não na última linha.

**Bloco 5: segundo erro do `push`.** ✅ Resolvido com o comando da mensagem. Depois, o `git push` sozinho funcionou, e sem nada novo respondeu `Everything up-to-date`.

### Treino sem roteiro

Repetir sozinho, do zero, em outra pasta: criar o repositório, fazer o commit, provocar e resolver os dois erros.

⭐ **Feito sem dica.** Saí da pasta anterior, conferi com `git status` antes do `init`, resolvi os dois erros e usei `git push -u origin main` em vez de copiar o comando. Por conta própria, criei um segundo arquivo e enviei só com `git push`. ✨ Em um projeto real, a mensagem deve dizer o que o programa ganhou, não o nome do arquivo, que o Git já registra.

Prova dos alertas "conferir a pasta" e "ler a mensagem de erro do Git": 1 de 2 em cada. A segunda precisa ser em outra sessão.

### Bloco 7: `git init` na pasta errada

✅ Provoquei o erro em uma pasta de treino, apaguei só o `.git` e refiz na pasta certa.

⚠️ Na cola, escrevi que perderia "tudo" ao apagar o `.git`. Corrigido: os arquivos continuam na pasta e o que já foi enviado continua no GitHub; o que se perde é o histórico que só existia localmente.

### Commit × branch

> *Perguntei:* o que é branch e se isso importa, e depois: "9f04043 e d6eee30 são commits e branch é a main? por que aparece o nome do endereço do repositório e a main em 9f04043 e não aparece em d6eee30?"

Sim, são commits, e `main` é a branch. O parêntese do `log` mostra para onde cada nome aponta agora, e `origin/main` é a `main` que está no `origin`, não o endereço. Testei um commit sem enviar: os nomes ficaram separados e, depois do `push`, juntos de novo. Branches em si ficam para o Dia 37.

### Backup das anotações privadas

Criei um repositório privado para guardar as anotações que não vão para o repositório público. ✅ Feito com orientação passo a passo; conferi em janela anônima que o endereço dá 404.

> *Perguntei:* por que aquele nome, e se esse é o jeito certo de fazer backup.

O nome sugerido era genérico, e o professor reconheceu: troquei por um que indica de qual projeto é o par. Git serve para poucos arquivos de texto, mas é manual e não é lugar para senha; a alternativa seria um serviço de sincronização, que copia sozinho e guarda menos histórico. Escolhi o Git.

⚠️ Não previ o que o `git remote -v` mostraria depois do `git init`, e achei que não tinha entendido as saídas. A leitura estava certa: faltava saber que o Git para no primeiro `.git` que encontra.

### Cola da semana

Duas perguntas saíram ambíguas ou incompletas por erro do professor, que as reescreveu com a situação completa e um item para cada pergunta.

| Pergunta | Resultado | Correção |
|---|---|---|
| 1. `git add .` em subpasta | ✅ | Motivo e comandos certos; o prompt mostrava a pasta |
| 2. Tirar arquivo da lista antes do primeiro commit | ⚠️ depois ✅ | Respondi `git restore --staged`, que falha nesse momento; o certo é `git rm --cached`, escrito na saída |
| 3. Nomes no `git log` | ✅ | O Git gera o código, e a mensagem é de quem faz o commit; falta `push` para os nomes se juntarem |
| 4. Dois motivos, dois commits | ✅ | Dois commits com os motivos certos; corrigi uma aspa sobrando. ✨ Mensagem no presente, dizendo o que mudou |
| 5. Repositório dentro de outro | ⚠️ depois ✅ | Só completei depois da explicação do professor |
| 6. Arquivo que some do `git status` | ⭐ | Expliquei o motivo e previ que ele volta como `modified` se for editado |
| 7. PC queimado e senha no GitHub | ✅ | Só o que chegou com `push` volta. O motivo sobre a senha veio da explicação do professor |

### Refazer um exercício sem olhar

✅ Refiz o `ex04` do Dia 3 em `refazer_dia03_ex04_dividir_conta.py`, com a saída exata nos dois testes e `:.2f`, que não existia para mim no Dia 3. ✨ `quantidade_pessoas` é mais claro do que `qtde_pessoas`.

### `git log` da semana

- **Quantidade de commits:** ✅ 10.
- **Commit que conclui o Dia 8:** ⚠️ respondi `e86b206`, que é o commit logo abaixo; o certo é `9f4410b`.
- **Mensagem menos clara:** escolhi `fc9d403`, porque foge do padrão. ✨ O problema mais concreto é o "e": a mensagem junta dois motivos. O `2608019` é o que realmente está fora do padrão, sem o `docs:`.
