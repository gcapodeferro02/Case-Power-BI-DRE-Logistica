# Segurança e limitações

> **Nó Pai:** [[05_PROJETOS/DRE/Case-Power-BI-DRE-Logistica/README|Voltar ao Case DRE]] | [[05_PROJETOS/DRE/HUB_DRE|HUB DRE]]  

## O que foi removido

O case público não contém:

- arquivos PBIX ou PBIP;
- cache do modelo ou dados brutos;
- credenciais e arquivos de ambiente;
- URLs, caminhos locais ou identificadores de tenant;
- nomes de pessoas, fornecedores ou centros de custo reais;
- valores financeiros legíveis nas imagens.

## Como as imagens foram tratadas

As imagens publicadas devem seguir este fluxo:

```text
Captura autorizada -> seleção das áreas sensíveis -> blur/cobertura -> revisão visual -> publicação
```

O blur não é uma substituição para a remoção. Sempre que possível, o texto
sensível deve ser trocado por um rótulo genérico; o desfoque é usado quando a
estrutura visual precisa ser preservada.

## Limitações do case

O repositório mostra a arquitetura e o raciocínio do desenvolvimento, mas não
reproduz o ambiente de produção. Portanto:

- fontes são descritas genericamente;
- regras dependentes de políticas internas foram simplificadas;
- resultados numéricos não podem ser usados para validar o negócio real;
- a agenda de refresh deve ser definida pela operação que fornece os arquivos.

## Checklist antes de publicar

- [ ] nenhuma imagem original foi copiada;
- [ ] valores e nomes estão ilegíveis ou substituídos;
- [ ] não existem arquivos proibidos no Git;
- [ ] não existem segredos ou URLs internas;
- [ ] o README continua compreensível sem os dados reais;
- [ ] links e imagens renderizam corretamente no GitHub.

