# Atualização e fontes

## Fluxo de atualização

```mermaid
flowchart LR
    A[Arquivo novo] --> B[Local de origem]
    B --> C[Power Query]
    C --> D[Tipagem e limpeza]
    D --> E[Modelo semântico]
    E --> F[Refresh do relatório]
    F --> G[Validação pós-carga]
```

O refresh segue uma sequência simples: localizar a entrada, transformar o
conteúdo, carregar as tabelas e atualizar as medidas.

## Fluxo visual da atualização

A imagem abaixo apresenta uma visão ilustrativa do caminho entre os arquivos de
origem, a sincronização intermediária, o modelo semântico e o relatório final.
Ela foi incluída como material demonstrativo e não contém valores operacionais,
credenciais ou dados de negócio.

![Fluxo visual da atualização do relatório DRE](../assets/fluxo-atualizacao-real.png)

## Etapas de transformação

### 1. Descoberta

As consultas procuram os arquivos esperados em uma área de origem. No case
público, os caminhos são descritos genericamente para não revelar estrutura
interna.

### 2. Leitura

Arquivos tabulares são abertos como planilhas ou CSVs. A primeira linha é
promovida a cabeçalho e as colunas são selecionadas conforme a necessidade
analítica.

### 3. Limpeza

As transformações observadas no modelo incluem:

- remoção de registros fora do escopo;
- retirada de colunas técnicas sem uso no relatório;
- renomeação de campos para nomes mais claros;
- extração de partes de textos compostos;
- substituição de rótulos inconsistentes;
- tratamento de erros de valores monetários.

### 4. Tipagem

Datas seguem uma regra explícita de localização e valores monetários recebem
tratamento decimal antes de entrar no modelo. Essa etapa evita que uma coluna
financeira seja interpretada como texto ou que uma data seja lida no formato
incorreto.

### 5. Validação

Antes de consumir o refresh, recomenda-se conferir:

| Verificação | Pergunta |
| --- | --- |
| Volume | A carga trouxe registros? |
| Datas | O período esperado está presente? |
| Chaves | Categorias e centros possuem correspondência? |
| Valores | Existem erros ou nulos inesperados? |
| Atualização | A data exibida representa a última carga? |

## Frequência

A frequência real depende do acordo operacional da organização. O padrão
recomendado é atualizar após a disponibilização dos arquivos de origem e
validar o período carregado antes do consumo executivo.

## Ponto importante

O Power BI não corrige uma fonte inconsistente sozinho. Se o arquivo muda nome
de coluna, formato de data ou regra de sinal, a consulta precisa capturar essa
mudança explicitamente ou o refresh pode falhar silenciosamente em uma camada
posterior.
