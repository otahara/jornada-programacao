# Dia 5 · Bloco 5: `ZeroDivisionError`

## ✅ O que aprendi neste bloco

- `ZeroDivisionError` aparece quando o programa tenta **dividir por zero**, que não existe nem na matemática
- A mensagem é direta: `ZeroDivisionError: division by zero`
- O erro aparece na linha da divisão, mas o problema está **onde o zero entrou**: numa variável do código ou no que o usuário digitou
- Quando o zero vem do usuário, o código não tem nada escrito errado. Impedir esse valor exige uma decisão (`if`), que vem no Dia 11

---

## ⚠️ Pontos de atenção (onde eu tropecei)

- Nenhum tropeço neste bloco.
- Descoberta: com `pessoas = 2.5`, o programa roda e mostra `3.2`, mas não existe 2,5 pessoas. **Rodar sem erro não quer dizer que o resultado faz sentido.**

## Os 2 casos

| Exercício | Origem do zero | Quebra na | Problema na | Conserto |
|---|---|---|---|---|
| [ex01](ex01.py) | `pessoas = 0` no código | linha 4 | linha 3 | outro valor para `pessoas` (ex.: `2` → `Cada um come: 4.0`) |
| [ex02](ex02.py) | usuário digitou `0` jogos | linha 4 | linha 3 | hoje: rodar de novo com um número válido; no Dia 11: impedir com `if` |
