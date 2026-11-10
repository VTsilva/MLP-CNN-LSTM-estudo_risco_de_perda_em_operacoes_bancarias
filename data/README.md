# Dados — arquitetura Medallion

## Princípios

A arquitetura organiza a origem e as transformações de forma rastreável. O Raw é imutável. Cada camada derivada deve ser reproduzível e ter schema/regras documentados.

- `raw/`: cópia original recebida da fonte, sem transformação.
- `bronze/`: ingestão e padronização técnica (encoding, tipos, datas e schema), preservando valores originais.
- `silver/`: dados validados e tratados para análise, com regras explícitas.
- `gold/`: dataset(s) finais com target/features e estrutura usada nos experimentos.

## Regras de modelagem temporal

- Não embaralhar a série bruta antes da divisão cronológica.
- Criar janelas sem permitir que a entrada contenha informação posterior ao target.
- Ajustar transformadores somente no treino.
- Guardar definições das partições, da janela e do schema por experimento.
- Não misturar target futuro com features observáveis no mesmo instante de previsão.

## Estado

Somente `raw/` contém o CSV original neste momento. Bronze, Silver e Gold ainda não possuem datasets derivados. Consulte `contexto_ia/estado_atual.md`.
