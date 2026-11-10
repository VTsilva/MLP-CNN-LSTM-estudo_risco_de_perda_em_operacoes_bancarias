# Trabalho 1 — Enunciado e requisitos consolidados

> Documento auxiliar de consulta para agentes. O notebook original fornecido pelo professor permanece a fonte primária e deve ser preservado sem alterações.

## Texto de orientação recebido

Depois de filtrar e preparar esses dados, o estudante fará uma análise básica da série, plotando gráficos, determinando ciclos e tendências básicas.

Em seguida, dividirá os dados em 70% treinamento, 20% validação, e 10% teste, e determinará o tamanho da janela móvel.

Ao contrário do que foi feito em aula, o estudante irá treinar os modelos acompanhando as funções de custo e acurácia dos conjuntos de treinamento e de validação, e irá determinar manualmente, por inspeção do gráfico, o número de épocas ideal, isto é, o instante em que o modelo começa a fazer o overfitting dos dados de treinamento, conforme curso IAD-012.

Fará então o retreinamento do modelo até o número de épocas ideal, e irá fazer o cálculo da acurácia nos conjuntos de treinamento, validação e teste. Se o número de épocas estimado para treinamento for julgado insuficiente, o estudante deverá continuar o treinamento até atingir o overfitting ou um plateau no valor da função de custo quando aplicado ao conjunto de validação.

Este processo será feito inicialmente só com uma das variáveis do dataset (previsão univariada), a mesma sendo prevista. Deverão ser explorados todos os modelos indicados, concentrando a previsão somente no valor imediatamente a seguir da série de entrada (passo único).

Ao final, deverá preparar uma comparação entre os modelos e identificar qual o melhor modelo que foi encontrado. Nesta comparação deverão ser usados elementos visuais que facilitem o entendimento das capacidades e deficiências dos diversos modelos.

Em seguida, o processo será repetido, para uma lista de modelos ligeiramente diferentes, considerando também outras variáveis presentes no dataset (previsão multivariada), concentrando a previsão somente no valor imediatamente a seguir de uma das variáveis da série de entrada (passo único).

O formato que deve ser adotado é de um relatório profissional, bem claro a respeito dos métodos que foram usados, explicando as escolhas que foram realizadas, apresentando os resultados de forma clara e sucinta, e provendo uma análise objetiva da razão da escolha do melhor modelo. A entrega consistirá somente deste arquivo `.ipynb`, salvo como `<nome_do_estudante>_trabalho1.ipynb`.

O trabalho será avaliado pela corretude do código e de sua execução e também por sua clareza e facilidade de ler, e pelo seu profissionalismo.

## Conferência contra o notebook do professor

O notebook original detalha os modelos específicos para os Passos 3 e 4. Consulte `contexto_ia/enunciado_e_requisitos.md` e `contexto_ia/metodologia_provisoria.md` para o inventário estruturado. Em divergência, prevalece o notebook original.
