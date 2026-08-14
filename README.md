# carrosseis-ia

Repositório-cérebro para gerar automaticamente os carrosséis "IA na Educação" (LinkedIn/TikTok) de Sandra Lourenço, a partir do material da UNESCO.

Um agente na cloud (Claude Code) executa o `PLAYBOOK.md`, gera um carrossel por vez a partir do `calendario.md` e das `fontes/`, e entrega numa página privada.

## Estrutura
```
PLAYBOOK.md      → manual que o agente segue (passo a passo)
calendario.md    → 32 temas set–dez, com estado [ ]/[x] e mapa de fontes
template/
  slides_base.html → template visual fixo (CSS + componentes + exemplos)
  render.py        → renderiza slides.html → PNG (2x) + PDF (deteta os slides sozinho)
fontes/          → texto extraído dos PDFs da UNESCO (fonte de conteúdo)
outputs/         → carrosséis gerados (slides.html, PNGs, PDF, legenda)
```

## O que a Sandra precisa de fazer (uma vez)
1. **Criar um repositório privado** chamado `carrosseis-ia` na conta github.com/lsandra221-design.
2. **Enviar esta pasta** para lá (o Claude ajuda com os comandos `git`).
3. **Ligar o GitHub ao Claude Code**, para o ambiente da cloud poder aceder ao repositório privado.
4. Fazer **um teste** (correr o agente uma vez) para confirmar que ele renderiza e entrega bem — só depois se agenda a repetição 2x/semana.

## Como corre (depois de ligado)
- Agendamento 2x/semana (ter/qui) → cada execução gera o próximo carrossel `[ ]` do calendário.
- O agente **nunca publica nas redes**. Deixa tudo pronto numa página privada; a Sandra abre e publica.

## Estado atual
- Template, render, calendário e playbook: prontos.
- Fontes extraídas: 1 de 12 (`01_professores_competencias.txt`). As restantes são adicionadas à medida.
- Carrosséis 01 e 02 já foram feitos manualmente (fora deste repo) e servem de referência de qualidade.
