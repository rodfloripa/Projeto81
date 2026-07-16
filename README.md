
# Diagnóstico Probabilístico de Doenças com Redes Bayesianas

<p align="center">
Projeto de inferência probabilística utilizando Redes Bayesianas para estimar a probabilidade de doenças a partir de sintomas observados, empregando Modelos Gráficos Probabilísticos (PGMs).
</p>

---

# 1. Visão Geral

<p align="justify">

Este projeto demonstra a aplicação de um **Modelo Gráfico Probabilístico (PGM)** para realizar diagnóstico probabilístico de doenças utilizando uma **Rede Bayesiana**. Diferentemente de sistemas baseados em regras fixas, o modelo representa explicitamente as relações de dependência entre doenças e sintomas por meio de um grafo direcionado.

A partir das evidências observadas, como presença de febre, tosse e cansaço, o algoritmo estima automaticamente a probabilidade de cada doença utilizando inferência bayesiana. Dessa forma, novas informações podem ser incorporadas ao diagnóstico, atualizando continuamente as probabilidades calculadas.

O objetivo do projeto é ilustrar como técnicas probabilísticas podem auxiliar processos de apoio à decisão, tratamento de incertezas e interpretação de relações causais entre variáveis.

</p>

---

# 2. Modelos Gráficos Probabilísticos

<p align="justify">

Modelos Gráficos Probabilísticos representam variáveis aleatórias e suas dependências condicionais através de grafos.

Cada nó representa uma variável, enquanto as arestas representam relações probabilísticas entre elas.

Essa estrutura permite decompor distribuições de probabilidade complexas em componentes menores, tornando os cálculos de inferência mais eficientes e interpretáveis.

Neste projeto foi utilizada uma Rede Bayesiana, um tipo de PGM baseado em grafos direcionados acíclicos.

</p>

---

# 3. Estrutura da Rede Bayesiana

<p align="justify">

O grafo representa a hipótese de que as doenças são responsáveis pela ocorrência dos sintomas.

Cada doença influencia probabilisticamente um ou mais sintomas, permitindo calcular a probabilidade das doenças após a observação dos sintomas apresentados pelo paciente.

A estrutura simplificada do modelo pode ser representada da seguinte forma:

</p>

```text
          Gripe
            │
            ├────────┐
            │        │
            ▼        ▼
         Febre     Tosse
            ▲        ▲
            │        │
       Resfriado   Covid
            │        │
            └──► Cansaço
```

---

# 4. Probabilidades Condicionais

<p align="justify">

Cada ligação do grafo possui uma distribuição de probabilidade condicional (CPD), responsável por representar a influência de uma variável sobre outra.

Essas tabelas podem ser obtidas de diferentes maneiras:

- conhecimento de especialistas;
- aprendizado automático a partir de bases de dados;
- combinação entre conhecimento especialista e dados históricos.

Em aplicações reais, normalmente essas probabilidades são aprendidas automaticamente utilizando grandes conjuntos de dados rotulados.

</p>

---

# 5. Construção do Modelo

<p align="justify">

Inicialmente são definidas as variáveis que compõem o problema e a estrutura do grafo direcionado.

Em seguida são adicionadas as distribuições de probabilidade condicional de cada variável e realizada uma verificação automática da consistência matemática da rede.

Trecho simplificado da construção:

</p>

```python
modelo = BayesianModel([
    ("Gripe", "Febre"),
    ("Covid", "Febre"),
    ("Gripe", "Tosse"),
    ("Covid", "Tosse")
])
```

---

# 6. Processo de Inferência

<p align="justify">

Após a construção da rede, o algoritmo recebe as evidências observadas e calcula automaticamente as probabilidades posteriores das doenças.

Esse processo utiliza inferência probabilística baseada no Teorema de Bayes, eliminando variáveis intermediárias durante os cálculos para tornar o processamento mais eficiente.

Trecho simplificado da inferência:

</p>

```python
resultado = inferencia.query(
    variables=["Gripe", "Covid"],
    evidence={"Febre":1, "Tosse":1}
)
```

<p align="justify">

Sempre que uma nova evidência é adicionada, as probabilidades são atualizadas automaticamente.

Por exemplo, ao informar que o paciente também apresenta cansaço, a distribuição de probabilidades pode mudar significativamente, refletindo o novo conjunto de informações disponível.

</p>

---

# 7. Aprendizado das Probabilidades

<p align="justify">

Quando existe uma base de dados contendo diagnósticos e sintomas, as distribuições condicionais podem ser estimadas automaticamente por algoritmos de aprendizado estatístico.

Isso elimina a necessidade de preencher manualmente todas as tabelas de probabilidade.

Trecho simplificado:

</p>

```python
modelo.fit(
    dados,
    estimator=MaximumLikelihoodEstimator
)
```

<p align="justify">

Quanto maior e mais representativa for a base de dados utilizada no treinamento, maior tende a ser a qualidade das probabilidades aprendidas pelo modelo.

</p>

---

# 8. Fluxo do Projeto

<p align="justify">

O funcionamento geral do sistema segue as seguintes etapas:

</p>

```text
Base de Dados
       │
       ▼
Construção da Rede Bayesiana
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

---

# 9. Aplicações

<p align="justify">

A utilização de Redes Bayesianas é amplamente empregada em problemas que envolvem incerteza e raciocínio probabilístico.

Além do diagnóstico médico, essa abordagem pode ser aplicada em sistemas especialistas, manutenção preditiva, análise de risco, detecção de fraudes, confiabilidade de equipamentos, segurança cibernética, previsão de falhas industriais, bioinformática, suporte à decisão clínica e modelagem de processos complexos.

Sua principal vantagem é combinar conhecimento especialista com dados históricos, produzindo modelos interpretáveis e capazes de atualizar automaticamente suas estimativas conforme novas evidências são observadas.

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

# 11. Espaço para Resultado

<p align="center">

**Imagem do grafo e dos resultados do diagnóstico**

*(Inserir imagem posteriormente.)*

</p>

---

# 12. Conclusão

<p align="justify">

Este projeto demonstra como Modelos Gráficos Probabilísticos podem representar relações de causa e efeito entre variáveis e realizar inferências mesmo na presença de informações incompletas ou incertas. A utilização de Redes Bayesianas permite incorporar conhecimento especializado, aprender probabilidades a partir de dados históricos e atualizar automaticamente as estimativas conforme novas evidências são disponibilizadas. Essa combinação entre representação gráfica, modelagem estatística e inferência probabilística torna essa abordagem uma ferramenta poderosa para sistemas de apoio à decisão em diversas áreas, especialmente em problemas onde a interpretação das relações entre as variáveis é tão importante quanto a própria previsão realizada pelo modelo.

</p>

