
# Diagnóstico Probabilístico de Doenças com Redes Bayesianas

<p align="justify">
Projeto de inferência probabilística utilizando Redes Bayesianas para estimar a probabilidade de doenças a partir de sintomas observados por meio de Modelos Gráficos Probabilísticos (PGMs).
</p>

---

# 1. Visão Geral

<p align="justify">
Este projeto demonstra a utilização de uma Rede Bayesiana para realizar diagnósticos probabilísticos a partir dos sintomas apresentados por um paciente. Em vez de utilizar regras fixas, o modelo representa explicitamente as relações de dependência entre doenças e sintomas por meio de um grafo direcionado.

</p>

<p align="justify">
À medida que novas evidências são informadas, como febre, tosse ou cansaço, o algoritmo atualiza automaticamente as probabilidades de cada doença utilizando inferência bayesiana.

</p>

<p align="justify">
Essa abordagem permite tratar naturalmente a incerteza presente em problemas reais, tornando o processo de decisão mais interpretável e flexível.

</p>

---

# 2. Modelos Gráficos Probabilísticos

<p align="justify">
Modelos Gráficos Probabilísticos (PGMs) representam relações estatísticas entre variáveis utilizando grafos.

</p>

<p align="justify">
Cada nó representa uma variável aleatória, enquanto as arestas representam dependências condicionais entre essas variáveis.

</p>

<p align="justify">
Essa representação permite decompor distribuições de probabilidade complexas em componentes menores, simplificando os cálculos de inferência.

</p>

<p align="justify">
Neste projeto foi utilizada uma Rede Bayesiana, composta por um grafo direcionado acíclico e distribuições de probabilidade condicionais.

</p>

---

# 3. Estrutura da Rede

<p align="justify">
As doenças são consideradas as causas dos sintomas. Dessa forma, cada doença influencia probabilisticamente a ocorrência de um ou mais sintomas.

</p>

<p align="center">
  <img src="https://github.com/rodfloripa/Projeto81/blob/main/fig.png">
</p>

<p align="justify">
Quando os sintomas são observados, o algoritmo percorre essa estrutura para calcular a probabilidade posterior de cada doença.

</p>

---

# 4. Probabilidades Condicionais

<p align="justify">
Cada ligação do grafo possui uma distribuição de probabilidade condicional (CPD), responsável por modelar a influência de uma variável sobre outra.

</p>

<p align="justify">
Essas probabilidades podem ser definidas por especialistas, aprendidas automaticamente a partir de bases de dados ou obtidas pela combinação dessas duas abordagens.

</p>

<p align="justify">
Em aplicações reais, normalmente essas distribuições são estimadas automaticamente utilizando grandes bases de dados clínicos.

</p>

---

# 5. Construção da Rede

<p align="justify">
Inicialmente são definidas as variáveis do problema e a estrutura do grafo que representa suas dependências.

</p>

<p align="justify">
Em seguida são adicionadas as distribuições de probabilidade condicional e realizada uma verificação automática da consistência matemática do modelo.

</p>

```python
modelo = BayesianModel([
    ("Gripe","Febre"),
    ("Covid","Febre"),
    ("Gripe","Tosse"),
    ("Covid","Tosse")
])
```

---

# 6. Inferência Bayesiana

<p align="justify">
Após a construção da rede, o algoritmo recebe os sintomas observados e calcula automaticamente a probabilidade de cada doença.

</p>

<p align="justify">
Esse processo utiliza inferência probabilística baseada no Teorema de Bayes, eliminando variáveis intermediárias para reduzir o custo computacional.

</p>

```python
resultado = inferencia.query(
    variables=["Gripe","Covid"],
    evidence={
        "Febre":1,
        "Tosse":1
    }
)
```

<p align="justify">
Sempre que um novo sintoma é informado, as probabilidades são recalculadas automaticamente, refletindo o novo conjunto de evidências disponível.

</p>

---

# 7. Aprendizado das Probabilidades

<p align="justify">
Quando existe uma base de dados contendo diagnósticos e sintomas, as distribuições condicionais podem ser aprendidas automaticamente utilizando algoritmos estatísticos.

</p>

<p align="justify">
Em aplicações reais, as distribuições de probabilidade condicional (CPDs) normalmente não são preenchidas manualmente. Em vez disso, elas são estimadas automaticamente a partir de uma base de dados contendo registros históricos.
</p>

<p align="justify">
Cada registro representa uma observação do problema, contendo os valores das variáveis da rede. No exemplo deste projeto, cada linha informa se um paciente possui determinada doença e quais sintomas foram observados.
</p>

| Gripe | Resfriado | Covid | Febre | Tosse | Cansaço |
|------:|----------:|------:|-------:|-------:|---------:|
| 1 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |

<p align="justify">
Após carregar a base de dados, o algoritmo utiliza um estimador estatístico para calcular automaticamente todas as distribuições de probabilidade condicional da Rede Bayesiana.
</p>

```python
from pgmpy.estimators import MaximumLikelihoodEstimator

modelo.fit(
    dados,
    estimator=MaximumLikelihoodEstimator
)
```

<p align="justify">
Durante esse processo, o algoritmo contabiliza a frequência de ocorrência de cada combinação entre doenças e sintomas e estima as probabilidades condicionais que serão utilizadas durante a inferência probabilística.
</p>

<p align="justify">
Quanto maior e mais representativa for a base de dados utilizada no treinamento, mais precisas tendem a ser as probabilidades aprendidas, tornando o modelo mais confiável para realizar diagnósticos probabilísticos.
</p>

<p align="justify">
Esse procedimento elimina a necessidade de preencher manualmente todas as tabelas de probabilidades e permite adaptar o modelo aos dados reais.
</p>

---

# 8. Fluxo do Projeto

```text
Base de Dados
      │
      ▼
Construção da Rede
      │
      ▼
Aprendizado das Probabilidades
      │
      ▼
Recebimento dos Sintomas
      │
      ▼
Inferência Bayesiana
      │
      ▼
Probabilidade de Cada Doença
```

<p align="justify">
O fluxo demonstra como as informações percorrem todas as etapas até a obtenção das probabilidades finais das doenças.

</p>

---

# 9. Aplicações

<p align="justify">
Redes Bayesianas são amplamente utilizadas em sistemas especialistas, diagnóstico médico, análise de risco, manutenção preditiva, bioinformática, detecção de fraudes, confiabilidade de equipamentos, previsão de falhas industriais, segurança cibernética e diversos problemas de apoio à decisão.

</p>

<p align="justify">
Sua principal característica é combinar conhecimento especializado com dados históricos, produzindo modelos interpretáveis e capazes de atualizar automaticamente suas estimativas sempre que novas evidências são observadas.

</p>

---

# 10. Tecnologias Utilizadas

<p align="justify">

- Python

- pgmpy

- NumPy

- Redes Bayesianas

- Modelos Gráficos Probabilísticos (PGMs)

- Inferência Bayesiana

</p>

---

# 11. Resultado

<p align="center">

<p align="center">
  <img src="https://github.com/rodfloripa/Projeto81/blob/main/fig2.jpg">
</p>

</p>

---

# 12. Conclusão

<p align="justify">
Este projeto demonstra como Redes Bayesianas podem representar relações probabilísticas entre doenças e sintomas de forma intuitiva e interpretável. A utilização de Modelos Gráficos Probabilísticos permite incorporar conhecimento especializado, aprender distribuições condicionais a partir de dados históricos e atualizar automaticamente as probabilidades conforme novas evidências são observadas.

</p>

<p align="justify">
Essa capacidade de lidar naturalmente com incertezas torna essa abordagem extremamente útil para sistemas de apoio à decisão, oferecendo modelos transparentes, eficientes e aplicáveis em diversos domínios onde a interpretação das relações entre variáveis é tão importante quanto a própria previsão realizada.

</p>
`
