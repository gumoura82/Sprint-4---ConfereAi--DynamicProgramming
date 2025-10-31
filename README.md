# Projeto de Programação Dinâmica: Otimização de Estoque (Wagner-Whitin)

Este projeto aplica a Programação Dinâmica para resolver um problema de controle de estoque e previsão de reposição. O objetivo é modelar o consumo de insumos (reagentes, descartáveis) para minimizar os custos totais, que são compostos pelo **custo fixo de pedido** e pelo **custo de manutenção de estoque**.

A solução implementada é o algoritmo de **Wagner-Whitin**, a abordagem clássica de PD para o problema de **Dimensionamento de Lote (Lot-Sizing)**.



## 1. Contexto e Formulação do Problema

O problema central é decidir **quando** fazer um pedido de reposição e **quanto** pedir, diante de uma demanda conhecida, para minimizar os custos ao longo do tempo.

* Fazer pedidos pequenos com frequência gera muitos **custos fixos** (frete, processamento).
* Fazer um pedido muito grande "zera" o custo fixo, mas gera um alto **custo de manutenção** (armazenagem, refrigeração, risco de validade).

O algoritmo de Wagner-Whitin encontra o balanço perfeito.

### 1.1. Definições da Programação Dinâmica

A formulação de Programação Dinâmica (PD) quebra o problema em subproblemas menores.

* **Estado ($t$):**
    Representa o período atual (ex: dia, semana) para o qual precisamos tomar uma decisão. Estamos no período $t$ e precisamos atender a demanda de $t$ até o final do horizonte $n$.

* **Função Objetivo ($F(t)$):**
    Define o **custo mínimo para atender a demanda de todos os períodos de $t$ até $n$**. Nosso objetivo final é encontrar $F(1)$, que é o custo ótimo total para o problema inteiro.

* **Decisão ($j$):**
    Estando no período $t$ (e decidindo fazer um pedido), a decisão é *até qual período $j$* (com $t \le j \le n$) este pedido irá cobrir. Ou seja, "Vou pedir agora o suficiente para suprir a demanda de $t$ até $j$."

* **Função de Transição (Recorrência):**
    Para calcular o custo $F(t)$, testamos todas as decisões $j$ possíveis e escolhemos a que gerar o menor custo. O custo de uma decisão $j$ é a soma de três partes:
    1.  **Custo Fixo ($K$):** O custo de fazer o pedido no período $t$.
    2.  **Custo de Estoque ($CustoEstoque(t, j)$):** O custo de manter o estoque necessário para os períodos $t+1, t+2, ..., j$.
    3.  **Custo do Futuro ($F(j+1)$):** O custo ótimo para resolver o resto do problema a partir do período $j+1$.

    A fórmula matemática é:

    $$ F(t) = \min_{t \le j \le n} \left\{ K + CustoEstoque(t, j) + F(j+1) \right\} $$

    Onde o custo de estoque é calculado como:

    $$ CustoEstoque(t, j) = h \cdot \sum_{r=t+1}^{j} (r-t) \cdot \text{demanda}[r-1] $$

    * $K$ é o custo fixo por pedido.
    * $h$ é o custo de manter 1 unidade por 1 período.

### 1.2. Implementação das Versões

Para resolver esta recorrência, o projeto implementa as duas abordagens clássicas de PD:

1.  **`recursive.py` (Top-Down com Memoization):**
    * Uma função `F(t)` é definida de forma recursiva, exatamente como a fórmula acima.
    * Usamos o decorador `@lru_cache` (Memoization) para armazenar os resultados de `F(t)` que já foram calculados, evitando recálculo e garantindo eficiência.

2.  **`bottomup.py` (Iterativa/Tabular):**
    * Um array (lista) `F` é criado para armazenar os custos.
    * O algoritmo preenche esse array "de trás para frente", começando com $F(n)$ e indo até $F(1)$.
    * Esta abordagem não usa recursão e é geralmente considerada mais eficiente em Python por evitar o limite de chamadas recursivas.

### 1.3. Validação dos Resultados

O arquivo `example.py` serve como o script de validação. Ele importa as duas funções (`wagner_whitin_topdown` e `wagner_whitin_bottomup`) e as executa com **exatamente os mesmos dados de entrada**.

Ao rodar o `example.py`, o console exibe o custo total e a política de pedidos (quando e quanto comprar) calculados por ambas as versões, provando que elas chegam ao mesmo resultado ótimo.



## 2. Relatório do Projeto

### 2.1. Código no GitHub

Este repositório contém os seguintes arquivos:
* `recursive.py`: Implementação Top-Down (Recursiva).
* `bottomup.py`: Implementação Bottom-Up (Iterativa).
* `example.py`: Script para executar e comparar as duas versões.
* `README.md`: Este relatório.

### 2.2. Explicação da Estrutura no Contexto

A estrutura do algoritmo foi usada para resolver o problema de "controle de estoque e previsão de reposição" da seguinte forma:

1.  **Modelagem:** O problema foi modelado como um problema de Dimensionamento de Lote.
    * A "demanda diária de insumos" (reagentes, etc.) é a lista `demanda`.
    * O "custo de reposição" (processar um pedido, frete) é a constante `K`.
    * O "custo de manter insumos" (armazenagem, refrigeração, desperdício) é a constante `h`.

2.  **Solução:** Ao executar o algoritmo (seja o `bottomup` ou `recursive`), a saída `F[1]` nos dá o **custo total mínimo** para gerenciar o estoque.

3.  **Ação Prática:** A variável `politica` (calculada por ambos os scripts) nos dá o plano de ação. Uma saída como `[(1, 2, 30), (3, 5, 40)]` significa:
    * No **Período 1**, fazer um pedido de **30 unidades** (suficiente para os períodos 1 e 2).
    * No **Período 3**, fazer um pedido de **40 unidades** (suficiente para os períodos 3, 4 e 5).
    * Nos períodos 2, 4 e 5, não fazer nenhum pedido.

Isso melhora a visibilidade do consumo e reduz desperdícios ao criar um cronograma de pedidos matematicamente ótimo.



## 3. Como Executar o Projeto

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório.
3.  (Opcional) Crie e ative um ambiente virtual.
4.  Abra o terminal na pasta do projeto e execute o script de exemplo:

```bash
python example.py
```

Você verá a saída das duas versões, confirmando que produzem o mesmo custo e a mesma política de pedidos.

## Nomes e RMs

Giovanne Charelli Zaniboni Silva | 556223 
Juan Francisco Alves Muradas | 555541 
Leonardo Pasquini Baldaia | 557416 
Gustavo Oliveira de Moura | 555827 
Lynn Bueno Rosa | 551102
