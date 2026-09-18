# Power BI DRE Case Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar um case publico e didatico que documente a construcao, atualizacao, modelagem e apresentacao de um relatorio Power BI DRE sem expor dados corporativos.

**Architecture:** O repositorio sera uma documentacao estatica organizada em README, documentos tecnicos e assets. Os documentos serao derivados dos metadados TMDL/PBIR do projeto local; imagens de referencia serao produzidas em uma camada separada de sanitizacao, nunca copiadas diretamente do ambiente original.

**Tech Stack:** Markdown, Mermaid, Git, Power BI PBIP/TMDL/PBIR como fonte de metadados local, Python/Pillow para imagens sanitizadas quando necessario.

**Spec:** `docs/superpowers/specs/2026-09-18-power-bi-dre-case-design.md`

## Global Constraints

- O repositorio publico nao pode conter `.pbix`, `.pbip`, caches, dumps, `.env`, dados brutos ou credenciais.
- Toda imagem publicada deve ter valores, nomes, identificadores, URLs, caminhos locais e referencias de tenant ofuscados ou substituidos.
- O README deve ser compreensivel sem acesso ao PBIP original.
- Fontes e ambientes corporativos devem ser descritos de forma generica.
- O texto deve separar fato, dimensao, medida, filtro, granularidade e atualizacao.
- O destino aprovado e `gcapodeferro02/Case-Power-BI-DRE-Logistica`.

---

### Task 1: Criar a estrutura publica e a camada de inventario

**Files:**
- Create: `README.md`
- Create: `docs/arquitetura.md`
- Create: `docs/atualizacao-e-fontes.md`
- Create: `docs/modelo-e-relacionamentos.md`
- Create: `docs/medidas-e-regras.md`
- Create: `docs/paginas-do-relatorio.md`
- Create: `docs/seguranca-e-limitacoes.md`
- Create: `.gitignore`
- Create: `tools/inventariar_pbip.py`

**Interfaces:**
- Consumes: caminho local do PBIP DRE, recebido por argumento de linha de comando.
- Produces: `artifacts/model-inventory.json`, contendo tabelas, colunas, medidas, particoes, expressoes, relacionamentos e paginas, sem valores de linhas.

- [ ] **Step 1: Write the failing inventory check**

Criar `tools/test_inventariar_pbip.py` com um fixture minimo de TMDL/PBIR e os testes:

```python
def test_inventory_lists_tables_relationships_and_pages(tmp_path):
    inventory = build_inventory(tmp_path / "pbip")
    assert inventory["tables"] == ["dCalendario", "fato"]
    assert inventory["relationships"][0]["from_table"] == "fato"
    assert inventory["pages"] == ["Resumo"]
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
python -m pytest tools/test_inventariar_pbip.py -q
```

Expected: FAIL because `build_inventory` does not exist.

- [ ] **Step 3: Implement the inventory parser**

Implement `build_inventory(pbip_root: Path) -> dict` using only filenames and declarative metadata. O parser deve:

1. ler `*.tmdl` em `BASE_OBZ.SemanticModel\definition\tables`;
2. extrair nomes de tabelas, colunas, medidas e particoes;
3. ler `relationships.tmdl` e separar tabela/coluna de origem e destino;
4. ler `pages.json` e `page.json` para obter nomes de paginas;
5. remover ou mascarar qualquer valor de conexao antes de serializar;
6. escrever JSON deterministico em `artifacts/model-inventory.json`.

- [ ] **Step 4: Run the focused test**

Run:

```powershell
python -m pytest tools/test_inventariar_pbip.py -q
```

Expected: PASS.

- [ ] **Step 5: Generate the real inventory**

Run:

```powershell
python tools/inventariar_pbip.py "C:\Users\guilherme.henrique\Desktop\Powerbi\Pasta_DRE" --output artifacts/model-inventory.json
```

Expected: JSON versionado apenas no working tree local de apoio; o arquivo nao devera ser publicado se ainda contiver nomes ou metadados sensiveis.

- [ ] **Step 6: Commit the public skeleton**

```powershell
git add README.md docs .gitignore tools artifacts
git commit -m "docs: scaffold Power BI DRE case"
```

### Task 2: Escrever a narrativa tecnica e os diagramas

**Files:**
- Modify: `README.md`
- Modify: `docs/arquitetura.md`
- Modify: `docs/atualizacao-e-fontes.md`
- Modify: `docs/modelo-e-relacionamentos.md`
- Modify: `docs/medidas-e-regras.md`
- Modify: `docs/paginas-do-relatorio.md`
- Modify: `docs/seguranca-e-limitacoes.md`
- Create: `assets/arquitetura-dados.mmd`
- Create: `assets/relacionamentos.mmd`
- Create: `assets/fluxo-atualizacao.mmd`

**Interfaces:**
- Consumes: `artifacts/model-inventory.json` e os TMDL/PBIR locais.
- Produces: documentacao navegavel, com links relativos e diagramas sem dados reais.

- [ ] **Step 1: Document the business context**

No README, incluir objetivo, desafio, publico do case, escopo e resultado. Explicar DRE como uma visao de receitas/despesas e planejamento, sem citar empresa, centro de custo ou valores reais.

- [ ] **Step 2: Document the update flow**

Em `docs/atualizacao-e-fontes.md`, explicar o fluxo generico:

```text
Arquivos corporativos -> area de origem -> Power Query -> modelo semantico -> paginas do relatorio
```

Descrever descoberta de arquivos, tipagem, filtros, renomeacoes, tratamento de erro, carga e validacao pos-refresh. Nao copiar URLs ou nomes de arquivos reais.

- [ ] **Step 3: Document the model**

Em `docs/modelo-e-relacionamentos.md`, separar:

| Grupo | Explicacao |
| --- | --- |
| Fatos | Lancamentos, orcamento e bases operacionais |
| Dimensoes | Calendario, categoria, subcategoria, centro de custo e fornecedor |
| Medidas | Calculos reutilizados no relatorio |
| Relacionamentos | Chaves que propagam filtros para as tabelas fato |

Incluir um diagrama Mermaid com fatos no centro e dimensoes ao redor.

- [ ] **Step 4: Document measures and report pages**

Em `docs/medidas-e-regras.md`, explicar medidas por finalidade, nao por valores reais. Em `docs/paginas-do-relatorio.md`, documentar pagina principal, detalhamento por categoria, drillthrough e pagina tecnica oculta.

- [ ] **Step 5: Add security guidance**

Em `docs/seguranca-e-limitacoes.md`, explicar ofuscacao, exclusoes, limites de inferencia e diferenca entre o ambiente real e o case publico.

- [ ] **Step 6: Link every document from README**

Adicionar indice, stack, arquitetura Mermaid, imagens, decisoes, seguranca, resultado e proximos passos seguindo o padrao dos cases existentes.

- [ ] **Step 7: Validate Markdown links**

Run:

```powershell
rg -n "\]\(([^)]+)\)" README.md docs
```

Expected: todos os destinos locais referenciados devem existir; URLs internas nao podem aparecer.

- [ ] **Step 8: Commit the documentation**

```powershell
git add README.md docs assets
git commit -m "docs: explain Power BI DRE architecture and model"
```

### Task 3: Produzir e sanitizar os assets visuais

**Files:**
- Create: `tools/sanitizar_assets.py`
- Create: `tools/test_sanitizar_assets.py`
- Create: `assets/arquitetura-dados.png`
- Create: `assets/modelo-relacionamentos.png`
- Create: `assets/fluxo-atualizacao.png`
- Create: `assets/telas-ofuscadas/01-resumo.png`
- Create: `assets/telas-ofuscadas/02-detalhamento.png`

**Interfaces:**
- Consumes: diagramas Mermaid e imagens de referencia selecionadas pelo usuario.
- Produces: PNGs publicaveis com blur/cobertura aplicada e nenhum texto operacional legivel.

- [ ] **Step 1: Write the failing sanitizer tests**

Criar testes que verifiquem dimensoes, formato e mascara:

```python
def test_sanitize_blurs_declared_regions(tmp_path):
    output = sanitize_image(source, tmp_path / "out.png", regions=[(0, 0, 40, 40)])
    assert output.exists()
    assert image_has_changed(source, output)
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
python -m pytest tools/test_sanitizar_assets.py -q
```

Expected: FAIL because `sanitize_image` does not exist.

- [ ] **Step 3: Implement deterministic sanitization**

Implement `sanitize_image(source: Path, destination: Path, regions: list[tuple[int, int, int, int]]) -> Path` with Pillow. Aplicar blur forte ou bloco opaco nas regioes declaradas, remover metadados EXIF e salvar PNG/RGB.

- [ ] **Step 4: Run the sanitizer tests**

Run:

```powershell
python -m pytest tools/test_sanitizar_assets.py -q
```

Expected: PASS.

- [ ] **Step 5: Generate architecture images**

Renderizar os tres diagramas a partir dos arquivos `.mmd` usando uma ferramenta Mermaid disponivel localmente ou exportacao manual. Conferir que labels sao genericos.

- [ ] **Step 6: Sanitize report captures**

Usar somente capturas autorizadas para o case. Antes de copiar cada imagem, cobrir numeros, nomes, filtros, URLs, IDs, caminhos, logos nao autorizados e qualquer texto operacional. Registrar as regioes sanitizadas em `tools/assets-manifest.json` sem salvar a imagem original.

- [ ] **Step 7: Commit the visual assets**

```powershell
git add tools assets
git commit -m "docs: add sanitized Power BI DRE visuals"
```

### Task 4: Validar seguranca, consistencia e experiencia de leitura

**Files:**
- Create: `tools/validar_publicacao.py`
- Create: `tools/test_validar_publicacao.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: todo o repositorio local.
- Produces: exit code 0 apenas quando o conteudo esta publicavel.

- [ ] **Step 1: Write the failing publication checks**

Testar bloqueio de extensoes, padroes de segredo, URLs corporativas, caminhos locais e arquivos fora da allowlist:

```python
def test_rejects_pbix_and_sensitive_patterns(tmp_path):
    (tmp_path / "report.pbix").write_bytes(b"x")
    assert validate_publication(tmp_path).errors
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
python -m pytest tools/test_validar_publicacao.py -q
```

Expected: FAIL because `validate_publication` does not exist.

- [ ] **Step 3: Implement the validator**

Bloquear:

- extensoes `.pbix`, `.pbit`, `.pbip`, `.abf`, `.bak`, `.env`;
- termos `password`, `secret`, `token`, `client_secret`;
- URLs SharePoint, tenant IDs e caminhos `C:\Users\`;
- arquivos de imagem fora de `assets/` e arquivos nao listados na documentacao.

- [ ] **Step 4: Run the validator and tests**

Run:

```powershell
python -m pytest tools -q
python tools/validar_publicacao.py .
```

Expected: tests PASS and validator exits 0.

- [ ] **Step 5: Review the rendered README**

Verificar manualmente headings, Mermaid, imagens, links, acentos, alt text e leitura em tela estreita. Corrigir links quebrados e qualquer texto que permita reidentificacao.

- [ ] **Step 6: Commit the validation layer**

```powershell
git add README.md tools
git commit -m "chore: validate public DRE case safety"
```

### Task 5: Preparar a publicacao no GitHub

**Files:**
- Modify: `.gitignore`
- No public source artifacts from the local PBIP

**Interfaces:**
- Consumes: repositorio local validado e conta GitHub autenticada.
- Produces: repositorio remoto `gcapodeferro02/Case-Power-BI-DRE-Logistica` com branch principal contendo apenas o case sanitizado.

- [ ] **Step 1: Confirm clean publication set**

Run:

```powershell
git status --short
git ls-files
```

Expected: apenas README, docs, assets, tools e arquivos de configuracao publicaveis.

- [ ] **Step 2: Run final secret scan**

Run:

```powershell
rg -n -i "password|secret|token|client_secret|sharepoint|tenant|C:\\Users\\|\\.pbix|\\.pbip|\\.env" --glob '!docs/superpowers/**' .
```

Expected: nenhum match sensivel; referencias genericas permitidas devem ser revisadas manualmente.

- [ ] **Step 3: Create the remote repository**

Criar o repositorio publico com nome `Case-Power-BI-DRE-Logistica`, descricao curta e sem adicionar README automatico para evitar conflito com o arquivo local.

- [ ] **Step 4: Push the validated branch**

```powershell
git branch -M main
git remote add origin https://github.com/gcapodeferro02/Case-Power-BI-DRE-Logistica.git
git push -u origin main
```

- [ ] **Step 5: Verify the public result**

Abrir o README no GitHub, verificar renderizacao dos assets e confirmar que o repositorio remoto nao contem arquivos excluidos pela politica de seguranca.
