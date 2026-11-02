# Dia 1: Ambiente + Hello World

## ✅ O que aprendi neste dia
- Quem executa o código é o **interpretador** (`python.exe`), e o Windows só o encontra se ele estiver no **PATH**
- Para rodar um arquivo no terminal: `python arquivo.py` (e **salvar antes**)
- `print` mostra algo na tela, e texto vai entre aspas
- O Python diferencia maiúsculas de minúsculas (`Print` dá erro)
- Para juntar texto e número: use vírgula ou `str()`. Com `+` direto, dá `TypeError`
- Leia o erro **de baixo para cima**

## ⚠️ Pontos de atenção (onde eu tropecei)
- **`TypeError` ao juntar texto + número com `+`**: eu li o erro e resolvi de dois jeitos, com vírgula ou com `str()`. Esse erro volta muito.
- **Esqueci de salvar** antes de rodar, e o programa rodou a versão antiga. Fique de olho na bolinha ● na aba ou ative o Auto Save.
- `Print` ≠ `print`: o Python diferencia maiúsculas de minúsculas.

## O que é "instalar Python"
- O código é só texto. Quem executa esse texto é o **interpretador** (`python.exe`).
- `seu código (.py) → python.exe → resultado na tela`
- Para instalar do zero: baixe em python.org e marque **"Add python.exe to PATH"** no instalador.

## PATH
- É a lista de pastas onde o Windows procura programas quando você digita um comando.
- **"não é reconhecido como comando"** = o programa não está instalado ou não está no PATH.

## Terminal
- No VS Code ele abre com `Ctrl + '`
- `python --version` mostra a versão instalada

## Dois jeitos de rodar Python
| Jeito | Como | Pra quê |
|---|---|---|
| Interativo | digitar `python` → aparece `>>>` (para sair: `exit()`) | testes rápidos, "calculadora" |
| Arquivo | `python arquivo.py` | o jeito normal de trabalhar |

## VS Code: o mínimo
| O quê | Atalho |
|---|---|
| Explorer (arquivos) | `Ctrl + Shift + E` |
| Terminal | `Ctrl + '` |
| Salvar | `Ctrl + S` (bolinha ● na aba = não salvo) |

- Extensão necessária: **Python (Microsoft)**
- **Salve antes de rodar**, ou ative `File → Auto Save`

## Hello World
```python
print("Hello World")
```
| Parte | O que é |
|---|---|
| `print` | função que mostra algo na tela |
| `( )` | entregam o valor para a função |
| `"..."` | texto (*string*). As aspas dizem ao Python que aquilo é texto, não comando. |

## Erros comuns
```python
print("Hello)     # SyntaxError: faltou fechar as aspas
Print("Hello")    # NameError: Python diferencia maiúsculas de minúsculas
print "Hello"     # SyntaxError: faltaram os parênteses
```
- Leia o erro **de baixo pra cima**: a última linha diz *o que* aconteceu, as de cima dizem *onde*.
