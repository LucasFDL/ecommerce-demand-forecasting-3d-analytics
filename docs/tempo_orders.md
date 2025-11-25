# Chaves de tempo – tabela orders (Olist)

## Coluna de referência (momento da decisão)

- `order_purchase_timestamp`
  - Momento em que o cliente conclui o pedido.
  - Vamos tratar como a **data de referência** do modelo (o "agora" na hora da previsão).
  - É com base nela que vamos:
    - Fazer splits temporais (treino = períodos mais antigos, teste = períodos mais recentes).
    - Decidir o que é passado/presente vs. futuro.

## Colunas que acontecem DEPOIS da compra (futuro → não usar como feature)

- `order_approved_at`
  - Papel: data/hora em que o pagamento é aprovado.
  - Acontece após a compra.
  - Informação de FUTURO em relação à `order_purchase_timestamp`.
  - Regra: **não usar como feature** em modelos que tomam decisão na hora da compra.

- `order_delivered_carrier_date`
  - Papel: data em que o pedido é entregue à transportadora.
  - Sempre depois da compra.
  - Informação de logística futura. Pode ser usada para análise de processo, mas:
    - **Não usar como feature** na previsão feita na compra.

- `order_delivered_customer_date`
  - Papel: data em que o pedido é entregue ao cliente.
  - Claramente bem depois da compra.
  - Natural candidata a **alvo** em problemas de prazo/atraso.
  - **Nunca** deve ser usada como feature em modelos que “decidem” na compra.

## Coluna de estimativa de entrega

- `order_estimated_delivery_date`
  - Papel: data estimada de entrega informada ao cliente.
  - Em princípio, conhecida pelo sistema na hora da compra.
  - Pode ser usada como feature se a regra de negócio permitir “usar o que o sistema já estimava”.
  - Se for usada como feature, documentar claramente:
    - O modelo está usando uma informação que também é derivada de dados históricos de logística.

## Resumo de regra anti–vazamento

- Tudo que acontece DEPOIS de `order_purchase_timestamp` é FUTURO para um modelo que decide na compra.
- Essas colunas de futuro (aprovado, enviado, entregue) **não podem entrar como features**.
- Elas podem:
  - ser alvo (ex.: prazo de entrega),
  - servir para análise de processo (EDA, dashboards),
  - mas não como entrada do modelo de previsão de demanda/prazo na data da compra.
