# Especificacao do case Power BI DRE

## Objetivo

Criar um repositorio publico de portfolio que explique, de forma didatica,
como um relatorio de DRE foi estruturado no Power BI: ingestao, atualizacao,
tratamento, modelo semantico, relacionamentos, medidas e experiencia final.

O material deve ser compreensivel para recrutadores, analistas de dados e
profissionais de BI sem exigir conhecimento previo do ambiente corporativo.

## Estrutura proposta

```text
Case-Power-BI-DRE-Logistica/
|-- README.md
|-- docs/
|   |-- arquitetura.md
|   |-- atualizacao-e-fontes.md
|   |-- modelo-e-relacionamentos.md
|   |-- medidas-e-regras.md
|   |-- paginas-do-relatorio.md
|   `-- seguranca-e-limitacoes.md
|-- assets/
|   |-- arquitetura-dados.png
|   |-- modelo-relacionamentos.png
|   |-- fluxo-atualizacao.png
|   `-- telas-ofuscadas/
`-- .gitignore
```

O README sera a porta de entrada narrativa. Os arquivos em `docs/` terao
detalhes tecnicos ligados por um indice. Os diagramas Mermaid serao usados
quando a informacao puder ser entendida como fluxo ou relacao.

## Conteudo tecnico

O case sera baseado apenas nos metadados versionaveis do projeto PBIP local:

- fontes e funcoes de importacao;
- etapas de tratamento no Power Query;
- tabelas fato, dimensoes e tabela de medidas;
- relacionamentos e direcoes de filtro;
- paginas, drillthrough e recursos visuais;
- medidas e regras de negocio que possam ser explicadas sem dados reais.

O texto deve distinguir claramente fato, dimensao, medida, filtro, granularidade
e atualizacao. Sempre que um detalhe depender de ambiente corporativo, ele sera
descrito de forma generica e marcado como limitacao do case publico.

## Politica de seguranca visual

Nenhuma captura original sera publicada diretamente. Cada imagem destinada ao
repositorio devera passar por uma etapa de sanitizacao:

- desfocar ou cobrir valores, nomes, identificadores e textos operacionais;
- remover URLs, caminhos locais, nomes de usuarios e referencias de tenant;
- substituir dados reais por rótulos genericos quando o blur prejudicar a
  explicacao;
- verificar visualmente a imagem final antes de adiciona-la ao Git;
- nao incluir arquivos `.pbix`, `.pbip`, caches, dumps, `.env` ou dados brutos.

O README explicara que as imagens sao demonstrativas e ofuscadas para
preservar confidencialidade.

## Resultado esperado

O leitor deve conseguir responder:

1. Qual problema de negocio o DRE resolve?
2. De onde os dados sao carregados e como a atualizacao funciona?
3. Como as tabelas se relacionam?
4. Onde ficam as regras de negocio e medidas?
5. Como o usuario navega pelas paginas finais?
6. Quais cuidados de seguranca foram aplicados para publicar o case?

## Validacao

Antes da publicacao, executar:

- busca por segredos, URLs internas, caminhos locais e nomes sensiveis;
- verificacao de que apenas arquivos publicaveis estao no repositorio;
- conferencia de links relativos, imagens e diagramas do README;
- revisao visual das imagens ofuscadas;
- checagem de que o README explica o fluxo sem depender do PBIP original.

## Publicacao

O destino aprovado e o repositorio publico
`gcapodeferro02/Case-Power-BI-DRE-Logistica`. A criacao do repositorio e o
push so devem ocorrer depois da validacao de seguranca e da aprovacao final do
conteudo.
