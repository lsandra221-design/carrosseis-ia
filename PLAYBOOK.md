# PLAYBOOK — Manual do agente (gerar 1 carrossel)

Este ficheiro é a instrução completa para gerar UM carrossel por execução. Segue os passos pela ordem.

## Passo 0 — Ambiente
```
pip install playwright Pillow --quiet
python -m playwright install chromium
```

## Passo 1 — Escolher o carrossel
Abre `calendario.md`. Encontra a **primeira linha `[ ]`** cujo ficheiro de fonte (coluna "fonte (id)" → mapa de fontes) **exista** em `fontes/`. Anota: número (NN), tema, ficheiro de fonte, tema-Sandra. Se nenhuma linha `[ ]` tiver fonte disponível, para e regista isso no fim.

## Passo 2 — Ler a fonte
Lê o ficheiro `fontes/NN_....txt` indicado. São documentos grandes; lê por partes e extrai só o que serve ao tema: definições, dados concretos, listas, exemplos. **Nunca inventes dados.** Se um facto for incerto, não o afirmes. Os ficheiros podem ter acentos corrompidos (ex.: "�"); ignora isso e escreve em português europeu correto.

## Passo 3 — Montar os slides
1. Cria a pasta `outputs/carrossel_NN_slug/` (slug = 2-3 palavras do tema).
2. Copia `template/slides_base.html` para `outputs/carrossel_NN_slug/slides.html`.
3. Substitui SÓ o conteúdo dos `<div class="slide">`. **Não toques no CSS.** Usa os componentes documentados no topo do template.
4. Estrutura: **8 ou 9 slides** = capa (s1) + 6-7 de conteúdo + fecho (resumo). Numera as pílulas 01, 02, ... a partir do 2º slide.

### Regras para o texto CABER (o erro mais comum é transbordar)
- Título: 1 linha sempre que possível; se 2 linhas, usa `class="title sm"`.
- Máximo **2 blocos** por slide abaixo do título (ex.: 1 card, OU 2 colunas, OU lista + nota).
- Listas: 3 a 5 itens, cada um curto (1 linha; `<small>` opcional de 1 linha).
- Capa e fecho sempre presentes. Marca de água `@sandra.lourenco.ia` em todos.

### Estilo de escrita (preferências da Sandra) — CRÍTICO
- Português europeu. Frases curtas e diretas.
- Sem travessões longos para dramatizar. Sem a construção "não é A, é B".
- Sem emojis no texto corrido (emojis só como ícones nos cartões).
- Registo humano, um detalhe real. Nada de linguagem de folheto.
- Temas da Sandra: RH, Educação, Função Pública, Análise de Dados.

## Passo 4 — Renderizar e VERIFICAR
```
python template/render.py outputs/carrossel_NN_slug/slides.html outputs/carrossel_NN_slug carrossel_NN
```
Abre o PDF gerado e verifica CADA slide. Se algum transbordar em baixo: encurta o título, reduz itens ou remove um bloco, e volta a renderizar. Repete até caber.

## Passo 5 — Legenda
Escreve `outputs/carrossel_NN_slug/legenda.md` com duas legendas (LinkedIn e TikTok/Instagram), registo humano, **máximo 3 hashtags** cada, sem hashtags com acentos.

## Passo 5.5 — Guião de vídeo (HeyGen)
Escreve `outputs/carrossel_NN_slug/guiao_video.md` — um guião curto para a Sandra gravar um vídeo no HeyGen (voz clonada), a partir do tema do carrossel. Regras:
- **6 cenas** (Cena 1 a 6): gancho, 4 de conteúdo, fecho com chamada à ação (subscrever/seguir).
- Português europeu falado, frases curtas, ~60-80s no total. Sem inventar dados.
- Escreve "inteligência artificial" por extenso (soa melhor na voz); evita a sigla "IA" no texto falado.
- No fim, uma nota para o HeyGen: usar as PNGs do carrossel como fundo de cada cena, com o avatar a narrar.

## Passo 6 — Entrega (página privada)
Publica uma **página privada (Artifact)** com: as imagens do carrossel pela ordem, a legenda LinkedIn e TikTok com botão de copiar, e o **guião de vídeo (6 cenas) também com botão de copiar**. Guarda o URL no fim.
> Se a publicação de Artifact não estiver disponível neste ambiente, deixa o PDF + PNGs + legenda no repositório (Passo 7) e reporta o URL do GitHub.

## Passo 7 — Fechar
1. Em `calendario.md`, muda a linha desse carrossel de `[ ]` para `[x]`.
2. `git add -A && git commit -m "Carrossel NN — <tema>" && git push`
3. Reporta: número gerado, caminho, e o URL de entrega (Artifact ou GitHub).

## Notas
- Gera **um** carrossel por execução (o próximo `[ ]` disponível).
- Não republiques carrosséis já `[x]`.
- Não publiques nas redes sociais. A publicação final é sempre feita pela Sandra.
