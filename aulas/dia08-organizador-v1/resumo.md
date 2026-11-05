# Dia 8: Organizador de estudos v1

Primeiro dia do projeto que vai crescer durante todo o curso. O código está em um repositório próprio: **[organizador-de-estudos](https://github.com/otahara/organizador-de-estudos)**.

## ✅ O que aprendi neste dia

- **Transformar minutos em horas:** `minutos // 60` dá as horas completas, e `minutos % 60` dá os minutos que sobram.
- **`:.1f` na f-string:** mostra um `float` com 1 casa depois do ponto: `77.777...` → `77.8`.
- **`:02d` na f-string:** mostra um inteiro com pelo menos 2 dígitos, completando com zero: `5` → `05`.
- **O formato muda só a aparência:** a variável continua com o valor completo.
- **Testar com outros valores:** um programa pode rodar sem erro e, mesmo assim, mostrar algo estranho.
- **Criar um repositório novo:** `git init`, `add`, `commit`, criar o repositório vazio no GitHub, `git remote add origin URL` e `git push -u origin main`.
- **`feat:` nos commits:** o tipo usado quando entra uma funcionalidade nova.
- ✨ Boa prática nova: **constantes em MAIÚSCULAS** no lugar de números soltos.
- ✨ Boa prática nova: **comentário que explica o porquê**, não o quê.

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- **Copiar em vez de resolver:** criei um segundo arquivo só para testar outros valores. Bastava trocar os valores e rodar de novo, ou usar `input`. Antes de copiar, a pergunta é: "o que muda entre as cópias?".
- **`git init` na pasta errada:** rodei o comando na pasta de cima, e o Git passou a enxergar outro repositório dentro do novo. O prompt mostrava isso. O conserto foi apagar só o `.git` criado por engano, já que ainda não havia commit, e repetir o `init` na pasta certa.
- **Excluir antes de diagnosticar:** apaguei pastas que não tinham relação com o problema. A mensagem nem as citava. Elas ainda estavam na Lixeira.
- **`git push` antes da hora:** tentei enviar sem o `origin` e, depois, sem o `-u`. As duas mensagens de erro diziam exatamente o que fazer.
- **Comentário que repete o código:** "completa com 0 à esquerda" dizia o que o `:02d` faz. O motivo era evitar que `2h5` parecesse um erro.

---

## Formatando números na f-string

```python
percentual = 7 / 9 * 100
minutos_restantes = 5

print(f"Acertos: {percentual:.1f}%")
print(f"Tempo: 2h{minutos_restantes:02d}")
print(percentual)
```

```
Acertos: 77.8%
Tempo: 2h05
77.77777777777779
```

| Formato | Significado | Exemplo |
|---|---|---|
| `:.1f` | `float` com 1 casa depois do ponto | `77.777...` → `77.8` |
| `:.2f` | `float` com 2 casas depois do ponto | `77.777...` → `77.78` |
| `:02d` | inteiro com pelo menos 2 dígitos, completando com zero | `5` → `05`, `15` → `15` |

**Arredondar:** para mostrar na tela, o recomendado é `:.1f`, porque ele sempre mostra a quantidade de casas pedida. `round(80.0, 2)` mostra `80.0`, e `:.2f` mostra `80.00`.

## ✨ Boas práticas que apareceram

**Constante em MAIÚSCULAS:** um valor que não muda durante o programa fica no começo do arquivo, com um nome.

```python
# A loja só vende caixas fechadas, então a caixa incompleta fica no estoque.
UNIDADES_POR_CAIXA = 12

unidades = 30

caixas = unidades // UNIDADES_POR_CAIXA
sobra = unidades % UNIDADES_POR_CAIXA

print(f"{caixas} caixas e sobram {sobra} unidades")
```

- O nome explica o número, e uma mudança acontece em uma linha só.
- O Python não impede a alteração: as maiúsculas são um combinado entre programadores.
- Nem todo número precisa de constante. O `100` de um percentual é óbvio na conta.

**Comentário que explica o porquê:**

| Comentário | Avaliação |
|---|---|
| `# divide as unidades por 12` | ❌ só repete o código |
| `# A loja só vende caixas fechadas...` | ✅ explica o motivo |

**Nome que diz o que a variável guarda:** `minutos_restantes` em vez de `resto_horas`, porque o valor são minutos.

## Criando o repositório de um projeto

| Passo | Comando ou ação |
|---|---|
| 1. Conferir a pasta | ler o final do prompt |
| 2. Criar o repositório | `git init` |
| 3. Conferir os arquivos | `git status` |
| 4. Primeiro commit | `git add .` e `git commit -m "feat: ..."` |
| 5. Criar no GitHub | repositório vazio, sem README nem `.gitignore` |
| 6. Ligar os dois | `git remote add origin URL` |
| 7. Primeiro envio | `git push -u origin main` |

**`.gitignore` antes de precisar:** o programa ainda não gera `__pycache__/`, mas as regras já ficam prontas para quando isso acontecer. É prevenção, e custa só 3 linhas.

## Arquivos do dia

| Onde | O que faz |
|---|---|
| [aquecimento.py](aquecimento.py) | minutos em horas e percentual de acertos, com os formatos novos |
| [organizador.py](https://github.com/otahara/organizador-de-estudos/blob/main/organizador.py) | 🎯 registra uma sessão de estudo e mostra o resumo (entrega do dia) |

---

## 🧑‍🏫 Relatório do professor

Registro das perguntas do dia, das minhas respostas (do jeito que escrevi, só com os erros de digitação corrigidos) e da correção.

### Revisão (sem consulta)

**1. Método que não altera a variável.** Com `materia = "matemática"`, `materia.upper()` e `print(materia)`: a) o que aparece, e por quê? b) Como fazer aparecer `MATEMÁTICA`?

> *Minha resposta:* "a) matemática; b) na linha 2 eu colocaria materia = materia.upper()"

✅ **Certa, sem ⭐:** o "por quê" ficou sem resposta. `upper()` devolve um texto novo, e ninguém o guardou.

**2. `curso.upper()` × `curso.len()`.** Com o programa e o `AttributeError` completos: a) por que a linha 2 funcionou e a linha 3 quebrou? b) Como corrigir a linha 3?

> *Minha resposta:* "a) eu não me lembro muito bem o que é AttributeError de forma técnica e literal, mas a linha 2 funcionou porque o método upper() foi usado da forma correta, mas a função len() foi usada de forma incorreta. O programa tenta chamar .len() como método, mas ele não é um método. b) o certo seria print(len(curso))"

⭐ **Certa e com o motivo.** A definição do erro não foi pedida.

**3. Correção depois do `push`.** Quais comandos, em ordem, levam a correção de um arquivo até o GitHub?

> *Minha resposta:* "a ordem é git status para ver a alteração, git add . para adicionar os arquivos com alteração, git commit -m "mensagem" e git push para subir para o github. Um detalhe importante é conferir, na hora de dar os comandos, se estou no repositório equivalente ou na raiz."

⭐ **Certa**, com dois hábitos acrescentados: o `git status` antes e a conferência da pasta.

### Aquecimento

Com `minutos = 135`, `feitas = 10` e `acertadas = 7`, mostrar `Tempo: 2h15` e `Acertos: 70.0%`, sem digitar os resultados no código.

⭐ **Saída exata de primeira**, com `//`, `%` e parênteses na conta, sem dica. ✨ `horas_exatas` e `resto_horas` viraram `horas` e `minutos_restantes`, que dizem melhor o que as variáveis guardam.

### Parte 1: testando com outros valores

Com `minutos = 125` e `feitas = 9`: prever a saída, rodar e olhar como usuário.

> *Minha resposta:* "acho que vai aparecer 2 horas e 5 minutos... se não arredondar, vai aparecer uma dízima periódica. [Depois de rodar:] Ficou estranho, né: apareceu 2 horas e 5 minutos, mas 2h5 fica estranho, o certo seria 2h05. E a dízima também: o Python não arredonda. Agora só me resta saber se, em um sistema de correção de provas, o correto é arredondar para cima ou para baixo."

⭐ **Achei os dois problemas sozinho**, em um programa que não dava erro. **Sobre arredondar:** quem decide é a regra de cada prova; no projeto, usamos o valor mais próximo. Além disso, `77.77777777777779` não é uma dízima de verdade: o `float` guarda um número limitado de dígitos.

### Parte 2: formatos

**Previsão de `{percentual:.2f}%`:**

> *Minha resposta:* "Eu conhecia o :.1f, que arredonda o float com uma casa após a vírgula, então com o :.2f eu imagino que arredonda com 2 casas, ficando 77.78%"

⭐ **Certa**, deduzida pela regra.

**Consertar o aquecimento:** ✅ saídas exatas com os dois conjuntos de valores. ⚠️ Criei um segundo arquivo só para trocar os valores: foi trabalho a mais, e depois o apaguei. Refiz o aquecimento com `input`, um rótulo que diz a unidade e a constante `MINUTOS_POR_HORA`. 🚨 É a segunda vez em que faço à mão algo que o programa resolveria, depois da linha de `=` do Dia 7.

### Entrega: `organizador.py`

Perguntar matéria, minutos, questões feitas e acertadas e mostrar o resumo com tempo e percentual, usando constantes e um comentário que explica um porquê.

⭐ **Saída exata de primeira, com todos os requisitos.** **Fui além:** usei `.title()` na matéria, para quem digita tudo minúsculo. ✨ O comentário do `:02d` explicava o quê, e foi reescrito. ✨ O `.title()` estraga nomes como `Direito Do Trabalho` e `Html E Css`, e decidi tirá-lo.

**Perguntei:** por que preencher o `.gitignore`, se ainda não há nada para ignorar? Tinha razão quanto a hoje: o programa não gera `__pycache__/`. O professor recomendou preencher como prevenção, por custar só 3 linhas, e eu preenchi.

### Publicação

⚠️ `git init` na pasta de cima, depois `git add .`. Excluí outras pastas achando que eram a causa, sem relação com o problema. 🚨 Conferir a pasta antes de usar o Git entrou em alerta, com o tropeço do Dia 4. Consertei apagando só o `.git` errado e repetindo o `init` na pasta certa.

⚠️ Rodei `git push` antes do `origin` e, depois, sem o `-u`, mesmo com o aviso. As mensagens traziam o comando. ✅ Repositório publicado, com o commit `feat: cria a v1 com registro de sessão e resumo`.

🚨 Na cola, ainda não consegui explicar esses dois erros, e o assunto entrou em alerta. Fica para a próxima sessão.
