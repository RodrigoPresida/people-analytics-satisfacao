# People Analytics — Satisfação e Engajamento de Colaboradores

Análise dos fatores que impactam a satisfação, produtividade e engajamento de colaboradores. O projeto traduz dados de RH em insights acionáveis: o que a empresa pode fazer antes de perder o colaborador.

Complementa o projeto de Turnover — se o primeiro responde "quem vai sair?", este responde "o que faz alguém querer ficar?".

## Estrutura do Projeto

```
people-analytics-satisfacao/
│
├── notebooks/
│   ├── 01_eda_perfil_colaboradores.ipynb   # Quem são os colaboradores?
│   ├── 02_satisfacao_engajamento.ipynb     # O que impacta a satisfação?
│   └── 03_insights_acoes.ipynb             # O que a empresa pode fazer?
│
├── data/
│   └── raw/                               # Dataset (baixar do Kaggle)
│
├── imagens/                               # Visualizações para LinkedIn/portfólio
├── outputs/
├── requirements.txt
└── README.md
```

## Notebooks

### 01 — Perfil dos Colaboradores
Análise exploratória do headcount: distribuição por departamento, faixa etária, tempo de casa, nível de cargo e distribuição salarial.

**Principais achados:**
- 200 colaboradores em 5 departamentos; cargo mais comum é Manager (40 pessoas)
- Idade média de 34,6 anos; tempo médio de casa de 10 anos
- Salário médio de USD 76.619 — com variação significativa por cargo

### 02 — Satisfação e Engajamento
Investigação dos fatores que mais se associam à satisfação: departamento, cargo, salário, feedback, produtividade e tempo de casa.

**Principais achados:**
- Satisfação média de 49,9% — quase metade dos colaboradores abaixo do ponto neutro
- 63 colaboradores (31,5%) com satisfação baixa (abaixo de 33%)
- Correlação satisfação × salário: -0,018 — praticamente zero
- Correlação satisfação × feedback: 0,008 — também insignificante
- Marketing é o departamento menos satisfeito (46%); IT é o mais satisfeito (54,3%)

### 03 — Insights e Ações
Segmentação de risco e tradução dos achados em recomendações concretas para o RH.

**Principais achados:**
- 29 colaboradores (14,5%) em risco alto: satisfação baixa e produtividade baixa simultaneamente
- Marketing e Sales concentram os maiores percentuais de risco alto (19%)
- 52 colaboradores (26%) recebem feedback abaixo de 2.0 — sinal de desmotivação silenciosa

## Conclusões

A análise revelou que **satisfação não é um problema de salário** — o fator financeiro tem correlação próxima de zero com o engajamento dos colaboradores.

| Fator | Sinal de Alerta | Recomendação |
|---|---|---|
| Satisfação < 33% | 63 colaboradores (32%) | Pesquisa de clima imediata + 1:1 com gestores |
| Feedback Score < 2.0 | 52 colaboradores (26%) | Capacitar gestores em feedback construtivo |
| Produtividade < 40% | 87 colaboradores (44%) | Identificar obstáculos: carga, ferramentas ou motivação |
| Diferença entre departamentos | 8pp entre Marketing e IT | Investigar práticas dos departamentos mais satisfeitos |
| Tempo de casa | Risco de estagnação após 5 anos | Trilha de carreira clara nos anos 3–5 |

**Risco imediato:** 29 colaboradores (14,5%) combinam satisfação baixa com produtividade baixa. Esse grupo provavelmente não será percebido até virar turnover — e o custo de substituição é muito maior que o custo de agir agora.

**Complemento ao projeto de Turnover:** se o projeto anterior respondia "quem vai sair?" (ROC-AUC 0,83), este responde "o que faz alguém querer ficar?" — as duas perguntas juntas formam uma visão completa de retenção.

## Como Reproduzir

```bash
# 1. Clone o repositório
git clone https://github.com/RodrigoPresida/people-analytics-satisfacao.git
cd people-analytics-satisfacao

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Baixe o dataset
# Acesse: https://www.kaggle.com/datasets/adityaab1407/employee-productivity-and-satisfaction-hr-data
# Salve o CSV em: data/raw/

# 4. Execute os notebooks na ordem
jupyter notebook
```

## Dataset

**Employee Productivity and Satisfaction HR Data**
- Fonte: [Kaggle](https://www.kaggle.com/datasets/adityaab1407/employee-productivity-and-satisfaction-hr-data)
- Variável central: satisfação do colaborador (escala 1–5)

## Stack

| Ferramenta | Uso |
|---|---|
| Python 3.12 | Linguagem principal |
| Pandas | Manipulação de dados |
| Plotly | Visualizações interativas |
| SciPy | Correlações e testes estatísticos |

## Autor

**Rodrigo Presida**
Estudante de Ciência de Dados — último semestre
[LinkedIn](https://www.linkedin.com/in/rodrigopresidati) · [GitHub](https://github.com/RodrigoPresida)
