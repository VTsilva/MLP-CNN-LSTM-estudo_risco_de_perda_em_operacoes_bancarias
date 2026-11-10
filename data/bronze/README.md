# Bronze — ingestão técnica

Propósito: criar uma representação tipada e padronizada do arquivo Raw, sem alterar o significado dos valores.

Transformações previstas (a confirmar na execução):
- leitura do CSV com encoding e delimitador explícitos;
- parsing de `Friday_of_Week` com formato `%m/%d/%Y`;
- tipagem numérica das seis colunas de indicadores;
- ordenação por data e validações estruturais;
- preservação de todas as colunas de origem.

O CSV Raw permanece intocado. Ainda não existe dataset Bronze gerado.
