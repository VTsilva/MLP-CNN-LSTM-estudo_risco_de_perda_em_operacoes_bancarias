# Plano — implementação dos experimentos neurais

**Status:** implementação concluída; diagnósticos recebidos e interpretados; seleção de épocas registrada; retreinamentos finais automatizados, ainda pendentes de execução.

## Objetivo
Completar o notebook com os oito modelos univariados e oito multivariados, seguindo previsão de um passo à frente e protocolo de treino/validação/teste.

## Etapas realizadas
1. Preservar o ZIP recebido e o histórico Git.
2. Conferir EDA, target, partições, janelas e benchmark.
3. Definir construtores para as 16 arquiteturas.
4. Implementar conversores de tensores, incluindo entradas por ramo multi-head e adaptação ConvLSTM temporal.
5. Implementar diagnóstico até 100 épocas com MSE/MAE em treino e validação.
6. Registrar época/justificativa por arquitetura em CSV e carregar automaticamente antes do retreinamento.
7. Implementar retreinamento por épocas escolhidas e avaliação em treino/validação/teste na escala original.
8. Implementar comparação contra persistência e exportação dos resultados.
9. Validar sintaxe, estrutura e execução sem TensorFlow.
10. Atualizar contexto, README, Skills, requisitos e CI estrutural.

## Critérios de conclusão
- 16 construtores de arquitetura presentes.
- Imports somente na célula central.
- Nenhum placeholder de modelo.
- Notebook com seleção de épocas registrada e retreinamento automático; execução neural final depende de TensorFlow no ambiente do estudante.
- Com TensorFlow, reutilizar diagnósticos compatíveis, carregar épocas registradas e executar retreinamentos.
- Não inventar resultados antes da execução do estudante.

## Limitações desta entrega
TensorFlow não está instalado no ambiente de construção. Portanto, os construtores foram implementados e os diagnósticos foram executados no ambiente do estudante. O retreinamento final precisa ser executado novamente após a seleção registrada, no Python 3.14 conforme `.python-version` e `requirements.txt`.
