# Medidas e regras de negócio

## Organização das medidas

As medidas foram agrupadas por finalidade para que o leitor encontre o cálculo
sem precisar procurar em cada tabela de origem:

| Grupo | Exemplos de finalidade |
| --- | --- |
| Realizado | Totalizar os lançamentos no contexto selecionado |
| Orçamento | Recuperar o valor planejado para a mesma combinação |
| Variação | Comparar realizado contra orçamento ou período anterior |
| Tempo | Calcular acumulado no ano, restante do ano e ano completo |
| Indicadores | Retornar valor, cor e rótulo para cartões e destaques |
| Navegação | Entregar o contexto usado no drillthrough |

## Regra de contexto

Uma medida não representa um número fixo. Ela responde ao filtro aplicado pelo
usuário. Por exemplo, o total realizado muda quando o leitor escolhe um mês,
uma categoria ou um centro de custo.

O raciocínio pode ser resumido assim:

```text
Medida = regra DAX + filtros ativos + relacionamentos do modelo
```

## Comparações

As comparações mais importantes são:

- realizado versus orçamento DRE;
- realizado versus orçamento base zero;
- realizado versus período anterior;
- acumulado no ano versus saldo restante.

O case evita publicar fórmulas com valores reais. A documentação explica a
intenção do cálculo e o contexto em que ele deve ser usado.

## Indicadores visuais

Além do valor, o modelo possui medidas auxiliares para controlar cores, textos,
cards HTML e indicadores de status. Essa separação deixa a regra visual
reutilizável e reduz fórmulas longas nos objetos do relatório.

## Cuidados

- validar o sinal dos valores antes de comparar;
- comparar períodos com a mesma granularidade;
- evitar misturar orçamento mensal e anual na mesma medida;
- tratar ausência de dados de forma explícita;
- testar a medida com filtros de mês, categoria e centro de custo.

