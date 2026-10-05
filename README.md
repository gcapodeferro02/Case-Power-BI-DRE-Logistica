# Case: desenvolvimento de um Power BI DRE

> **Nó Pai:** [[05_PROJETOS/DRE/HUB_DRE|Voltar ao HUB DRE]] | [[00_INDICE_MESTRE|Índice Mestre]]  
> Documentação pública e sanitizada de uma solução de Business Intelligence
> para acompanhar realizado, orçamento, variações e detalhamento financeiro.

> [!WARNING]
> Esta é uma documentação pública e sanitizada de uma solução desenvolvida em
> ambiente corporativo. As imagens são demonstrativas e ofuscadas; não há dados
> brutos, credenciais, arquivos PBIX/PBIP ou conexões corporativas no
> repositório.

## Contexto e problema

Um DRE precisa transformar lançamentos financeiros, orçamento e bases de apoio
em uma leitura simples para comparação entre realizado, orçamento e projeções.
O desafio não é apenas criar visuais: é organizar a entrada dos dados, aplicar
regras consistentes e garantir que cada filtro chegue à tabela correta.

Sem uma estrutura padronizada, a comparação entre realizado, orçamento e
projeções fica sujeita a fontes dispersas, regras duplicadas e dificuldade para
explicar a origem das variações. O objetivo foi organizar essa análise em um
modelo semântico reutilizável e compreensível.

## Solução

A solução conecta as fontes, aplica transformações no Power Query, organiza
fatos e dimensões no modelo semântico, centraliza medidas DAX e apresenta uma
visão executiva com caminhos para o detalhamento.

## Minha atuação

Atuei nas etapas documentadas no case:

- **Negócio:** entendimento das perguntas sobre realizado, orçamento e variação;
- **Dados:** tratamento, padronização e organização das fontes;
- **Analytics:** definição das medidas e regras de comparação;
- **Visualização:** estruturação da visão executiva e dos detalhamentos;
- **Entrega:** validação, documentação e publicação de evidências sanitizadas.

## O que este case demonstra

- conexão de arquivos corporativos a uma camada de transformação;
- padronização de datas, valores, categorias e chaves;
- separação entre tabelas fato, dimensões e medidas;
- relacionamentos para filtrar o modelo de forma previsível;
- medidas para realizado, orçamento, variação e acompanhamento anual;
- navegação entre visão executiva e detalhamento por categoria;
- publicação segura de evidências visuais.

![Fluxo de atualização do relatório DRE](assets/fluxo-atualizacao-real.png)

## Modelagem analítica

```text
Dimensões
    ↓
Tabelas fato
    ↓
Medidas DAX
    ↓
Indicadores
    ↓
Relatório
```

## Índice da documentação

| Documento | O que explica |
| --- | --- |
| [Arquitetura](docs/arquitetura.md) | Separação das camadas e responsabilidades |
| [Atualização e fontes](docs/atualizacao-e-fontes.md) | Como os dados entram, são tratados e chegam ao modelo |
| [Modelo e relacionamentos](docs/modelo-e-relacionamentos.md) | Fatos, dimensões, chaves e propagação de filtros |
| [Medidas e regras](docs/medidas-e-regras.md) | Organização das medidas e comparações do DRE |
| [Páginas do relatório](docs/paginas-do-relatorio.md) | Visão final, detalhamento e drillthrough |
| [Segurança e limitações](docs/seguranca-e-limitacoes.md) | Sanitização, exclusões e limites do case público |
| [Plano de Engenharia](docs/superpowers/plans/2026-09-18-power-bi-dre-case.md) | Plano de implementação e fases do dashboard |
| [Especificação de Design](docs/superpowers/specs/2026-09-18-power-bi-dre-case-design.md) | Especificação técnica completa de arquitetura e design |

## Perguntas de negócio respondidas

- Quanto foi realizado em determinado período?
- Qual é a variação contra o orçamento?
- Quais categorias explicam a variação?
- Como o resultado evoluiu ao longo do tempo?
- Onde aprofundar a análise por centro de custo, fornecedor ou período?

## Stack utilizada

| Camada | Tecnologia | Finalidade |
| --- | --- | --- |
| Ingestão | Power Query | Conectar, combinar e tratar arquivos |
| Modelagem | Power BI Semantic Model | Organizar fatos, dimensões e medidas |
| Cálculo | DAX | Criar indicadores e comparações |
| Apresentação | Power BI Report | Exibir a visão executiva e os detalhes |
| Documentação | Markdown + Mermaid | Explicar decisões e fluxos |

## Impacto / resultado

O resultado é uma visão centralizada que padroniza a leitura do DRE, facilita a
comparação entre realizado e orçamento e cria um caminho consistente entre a
visão executiva e o detalhamento.

Os números exibidos nas imagens foram removidos ou ofuscados. O foco do case é
mostrar o raciocínio de engenharia e análise, não reproduzir dados reais.

## Segurança por padrão

O repositório foi desenhado para publicar somente documentação e evidências
sanitizadas. Antes de qualquer publicação, são verificados arquivos proibidos,
segredos, caminhos locais, URLs corporativas e imagens não ofuscadas.

## Próximos passos

- adicionar testes de qualidade para chaves e datas;
- documentar um contrato de atualização para cada fonte;
- incluir métricas de duração e falha do refresh;
- evoluir o modelo para uma camada analítica governada.
