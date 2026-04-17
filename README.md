# People Analytics — Satisfação e Engajamento de Colaboradores

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-interativo-blueviolet?logo=plotly)
![Dados](https://img.shields.io/badge/dados-Kaggle%20HR%20Dataset-lightgrey)

Análise dos fatores que impactam a satisfação, produtividade e engajamento de colaboradores. O projeto traduz dados de RH em insights acionáveis: o que a empresa pode fazer antes de perder o colaborador.

> *"Satisfação não é um problema de salário — o fator financeiro tem correlação próxima de zero com o engajamento real."*

---

## Motivação

Esse projeto é o segundo de uma série de People Analytics desenvolvida como portfólio. Se o projeto de Turnover respondia **"quem vai sair?"**, este responde **"o que faz alguém querer ficar?"**

As duas perguntas parecem opostas, mas formam a mesma visão: retenção não começa quando o colaborador pede demissão — começa muito antes, nos sinais que os dados já capturam.

---

## Notebooks

| # | Notebook | Descrição | Status |
|---|---|---|---|
| 01 | `01_eda_perfil_colaboradores.ipynb` | Composição do headcount: departamento, cargo, faixa etária, salário e tempo de casa | ✅ |
| 02 | `02_satisfacao_engajamento.ipynb` | Fatores associados à satisfação: salário, feedback, produtividade, cargo, departamento e tempo de casa | ✅ |
| 03 | `03_insights_acoes.ipynb` | Segmentação de risco e recomendações concretas para o RH | ✅ |

---

## Principais Achados

| Achado | Valor |
|---|---|
| Satisfação média geral | **49,9%** — quase metade abaixo do ponto neutro |
| Colaboradores com satisfação baixa (< 33%) | **63 pessoas — 31,5%** do headcount |
| Correlação satisfação × salário | **-0,018** — praticamente zero |
| Correlação satisfação × feedback | **0,008** — também insignificante |
| Departamento menos satisfeito | **Marketing — 46%** |
| Departamento mais satisfeito | **IT — 54,3%** |
| Colaboradores em risco alto | **29 pessoas — 14,5%** (satisfação baixa + produtividade baixa) |

> O problema não está no que a empresa paga. Está em algo que o salário não compra — e que os dados ainda não conseguem nomear sozinhos.

---

## Conclusões

| Fator | Sinal de Alerta | Recomendação |
|---|---|---|
| Satisfação < 33% | 63 colaboradores (32%) | Pesquisa de clima imediata + 1:1 com gestores |
| Feedback Score < 2.0 | 52 colaboradores (26%) | Capacitar gestores em feedback construtivo |
| Produtividade < 40% | 87 colaboradores (44%) | Identificar obstáculos: carga, ferramentas ou motivação |
| Diferença entre departamentos | 8pp entre Marketing e IT | Investigar práticas dos departamentos mais satisfeitos |
| Tempo de casa | Risco de estagnação após 5 anos | Trilha de carreira clara nos anos 3–5 |

**Risco imediato:** 29 colaboradores combinam satisfação baixa com produtividade baixa. Esse grupo provavelmente não será percebido até virar turnover — e o custo de substituição é muito maior que o custo de agir agora.

---

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

---

## Dataset

| Base | Fonte | Variáveis |
|---|---|---|
| Employee Productivity and Satisfaction HR Data | [Kaggle](https://www.kaggle.com/datasets/adityaab1407/employee-productivity-and-satisfaction-hr-data) | 200 colaboradores, 5 departamentos — variável central: `Satisfaction Rate (%)` |

---

## Stack

| Ferramenta | Uso |
|---|---|
| Python 3.12 | Linguagem principal |
| Pandas | Manipulação de dados |
| Plotly | Visualizações interativas |
| SciPy | Correlações e testes estatísticos |

---

## Autor

**Rodrigo Cruz dos Santos**
[LinkedIn](https://www.linkedin.com/in/rodrigopresidati) · [GitHub](https://github.com/RodrigoPresida)
