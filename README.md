# Case: desenvolvimento de um Power BI DRE

> Documentação de portfolio sobre a construção de um relatório de
> demonstração de resultado, com foco em atualização, modelagem semântica,
> relacionamentos e experiência final de análise.

> [!WARNING]
> Este é um case público e educativo. As imagens são demonstrativas e
> ofuscadas; não há dados brutos, credenciais, arquivos PBIX/PBIP ou conexões
> corporativas no repositório.

## Contexto

Um DRE precisa transformar lançamentos financeiros, orçamento e bases de apoio
em uma leitura simples para comparação entre realizado, orçamento e projeções.
O desafio não é apenas criar visuais: é organizar a entrada dos dados, aplicar
regras consistentes e garantir que cada filtro chegue à tabela correta.

Este case mostra essa trajetória com uma linguagem acessível, preservando a
confidencialidade do ambiente original.

## O que este case demonstra

- conexão de arquivos corporativos a uma camada de transformação;
- padronização de datas, valores, categorias e chaves;
- separação entre tabelas fato, dimensões e medidas;
- relacionamentos para filtrar o modelo de forma previsível;
- medidas para realizado, orçamento, variação e acompanhamento anual;
- navegação entre visão executiva e detalhamento por categoria;
- publicação segura de evidências visuais.

## Arquitetura em uma visão

```mermaid
flowchart LR
    A[Arquivos de origem] --> B[Power Query]
    B --> C[Modelo semântico]
    C --> D[Medidas DAX]
    D --> E[Relatório DRE]
    E --> F[Tomada de decisão]
```

![Fluxo de atualização do relatório DRE](assets/fluxo-atualizacao-real.png)

O fluxo visual detalhado entre origem, sincronização, modelo semântico e
relatório está documentado em
[Atualização e fontes](docs/atualizacao-e-fontes.md).

## Índice da documentação

| Documento | O que explica |
| --- | --- |
| [Arquitetura](docs/arquitetura.md) | Separação das camadas e responsabilidades |
| [Atualização e fontes](docs/atualizacao-e-fontes.md) | Como os dados entram, são tratados e chegam ao modelo |
| [Modelo e relacionamentos](docs/modelo-e-relacionamentos.md) | Fatos, dimensões, chaves e propagação de filtros |
| [Medidas e regras](docs/medidas-e-regras.md) | Organização das medidas e comparações do DRE |
| [Páginas do relatório](docs/paginas-do-relatorio.md) | Visão final, detalhamento e drillthrough |
| [Segurança e limitações](docs/seguranca-e-limitacoes.md) | Sanitização, exclusões e limites do case público |

## Stack utilizada

| Camada | Tecnologia | Finalidade |
| --- | --- | --- |
| Ingestão | Power Query | Conectar, combinar e tratar arquivos |
| Modelagem | Power BI Semantic Model | Organizar fatos, dimensões e medidas |
| Cálculo | DAX | Criar indicadores e comparações |
| Apresentação | Power BI Report | Exibir a visão executiva e os detalhes |
| Documentação | Markdown + Mermaid | Explicar decisões e fluxos |

## Resultado

O resultado é uma visão centralizada para responder perguntas como:

- quanto foi realizado em determinado período;
- como o realizado se compara ao orçamento;
- quais categorias explicam a variação;
- onde aprofundar a análise por centro de custo, fornecedor ou período.

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
