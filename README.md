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

### 02 — Satisfação e Engajamento
Investigação dos fatores que mais se associam à satisfação: equilíbrio trabalho-vida, relacionamento com gestores, reconhecimento, ambiente e crescimento.

**Perguntas que o notebook responde:**
- Qual departamento tem os colaboradores menos satisfeitos?
- Satisfação cai com o tempo de casa?
- Quem recebe menos reconhecimento tem menor engajamento?
- Equilíbrio trabalho-vida impacta mais que salário?

### 03 — Insights e Ações
Tradução dos achados em recomendações concretas para o RH. Cada insight vira uma ação: o que monitorar, quando agir, qual o custo de não agir.

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
