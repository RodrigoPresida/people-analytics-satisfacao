import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

IMAGENS = 'imagens'

# ── tema base ────────────────────────────────────────────────────────────────
LAYOUT = dict(
    font_family='Inter, sans-serif',
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(t=60, b=40, l=40, r=40),
)

def salvar(fig, nome):
    fig.update_layout(**LAYOUT)
    fig.write_image(f'{IMAGENS}/{nome}.png', width=900, height=500, scale=2)
    print(f'  ok: {nome}.png')

# ── carrega dados ─────────────────────────────────────────────────────────────
df = pd.read_csv('data/raw/hr_dashboard_data.csv')
df['Joining Date'] = pd.to_datetime(df['Joining Date'], format='%b-%y')
df['anos_empresa'] = ((pd.Timestamp('2024-01-01') - df['Joining Date']).dt.days / 365).round(1)
df['nivel_satisfacao'] = pd.cut(
    df['Satisfaction Rate (%)'],
    bins=[0, 33, 66, 100],
    labels=['Baixa (0-33%)', 'Média (34-66%)', 'Alta (67-100%)']
)
df['faixa_tempo'] = pd.cut(
    df['anos_empresa'],
    bins=[0, 2, 5, 10, 15, 100],
    labels=['< 2 anos', '2-5 anos', '5-10 anos', '10-15 anos', '> 15 anos']
)
df['risco'] = 'Normal'
df.loc[(df['Satisfaction Rate (%)'] < 33) & (df['Productivity (%)'] < 40), 'risco'] = 'Alto'
df.loc[(df['Satisfaction Rate (%)'] < 33) & (df['Productivity (%)'] >= 40), 'risco'] = 'Médio'
df.loc[(df['Satisfaction Rate (%)'] >= 33) & (df['Productivity (%)'] < 40), 'risco'] = 'Atenção'

print('=== Notebook 01 — Perfil dos Colaboradores ===')

# 01-A: headcount por departamento
por_depto = df['Department'].value_counts().reset_index()
por_depto.columns = ['departamento', 'total']
fig = px.bar(por_depto, x='total', y='departamento', orientation='h',
    title='Headcount por Departamento',
    labels={'total': 'Colaboradores', 'departamento': ''},
    color='total', color_continuous_scale='Blues', text='total')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False, yaxis={'categoryorder': 'total ascending'})
salvar(fig, '01a_headcount_departamento')

# 01-B: headcount por cargo
por_cargo = df['Position'].value_counts().reset_index()
por_cargo.columns = ['cargo', 'total']
fig = px.bar(por_cargo, x='total', y='cargo', orientation='h',
    title='Headcount por Cargo',
    labels={'total': 'Colaboradores', 'cargo': ''},
    color='total', color_continuous_scale='Teal', text='total')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False, yaxis={'categoryorder': 'total ascending'})
salvar(fig, '01b_headcount_cargo')

# 01-C: distribuição de idade
fig = px.histogram(df, x='Age', nbins=20,
    title='Distribuição de Idade',
    labels={'Age': 'Idade', 'count': 'Colaboradores'},
    color_discrete_sequence=['#2196F3'])
fig.update_layout(bargap=0.1)
salvar(fig, '01c_distribuicao_idade')

# 01-D: salário por cargo
ordem_cargos = ['Intern', 'Junior Developer', 'Analyst', 'Team Lead', 'Senior Developer', 'Manager']
fig = px.box(df, x='Position', y='Salary',
    title='Distribuição Salarial por Cargo',
    labels={'Position': 'Cargo', 'Salary': 'Salário (USD)'},
    category_orders={'Position': ordem_cargos},
    color='Position', color_discrete_sequence=px.colors.qualitative.Set2)
fig.update_layout(showlegend=False)
salvar(fig, '01d_salario_cargo')

# 01-E: tempo de casa
por_tempo = df['faixa_tempo'].value_counts().sort_index().reset_index()
por_tempo.columns = ['faixa', 'total']
fig = px.bar(por_tempo, x='faixa', y='total',
    title='Colaboradores por Tempo de Casa',
    labels={'faixa': 'Tempo de Casa', 'total': 'Colaboradores'},
    color='total', color_continuous_scale='Blues', text='total')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
salvar(fig, '01e_tempo_casa')

print('=== Notebook 02 — Satisfação e Engajamento ===')

# 02-A: satisfação por departamento
sat_depto = df.groupby('Department')['Satisfaction Rate (%)'].mean().reset_index()
sat_depto.columns = ['departamento', 'satisfacao_media']
sat_depto = sat_depto.sort_values('satisfacao_media')
fig = px.bar(sat_depto, x='satisfacao_media', y='departamento', orientation='h',
    title='Satisfação Média por Departamento',
    labels={'satisfacao_media': 'Satisfação Média (%)', 'departamento': ''},
    color='satisfacao_media',
    color_continuous_scale=['#ef5350', '#ffa726', '#66bb6a'],
    text=sat_depto['satisfacao_media'].round(1).astype(str) + '%')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
fig.add_vline(x=50, line_dash='dash', line_color='gray', annotation_text='Média geral')
salvar(fig, '02a_satisfacao_departamento')

# 02-B: satisfação por cargo
sat_cargo = df.groupby('Position')['Satisfaction Rate (%)'].mean().reset_index()
sat_cargo.columns = ['cargo', 'satisfacao_media']
fig = px.bar(sat_cargo, x='cargo', y='satisfacao_media',
    title='Satisfação Média por Cargo',
    labels={'satisfacao_media': 'Satisfação Média (%)', 'cargo': 'Cargo'},
    category_orders={'cargo': ordem_cargos},
    color='satisfacao_media',
    color_continuous_scale=['#ef5350', '#ffa726', '#66bb6a'],
    text=sat_cargo['satisfacao_media'].round(1).astype(str) + '%')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
fig.add_hline(y=df['Satisfaction Rate (%)'].mean(), line_dash='dash', line_color='gray', annotation_text='Média geral')
salvar(fig, '02b_satisfacao_cargo')

# 02-C: satisfação × produtividade
corr, _ = stats.pearsonr(df['Satisfaction Rate (%)'], df['Productivity (%)'])
fig = px.scatter(df, x='Satisfaction Rate (%)', y='Productivity (%)',
    color='Department',
    title=f'Satisfação × Produtividade (correlação: {corr:.2f})',
    labels={'Satisfaction Rate (%)': 'Satisfação (%)', 'Productivity (%)': 'Produtividade (%)'},
    trendline='ols')
salvar(fig, '02c_satisfacao_produtividade')

# 02-D: satisfação × feedback
df['faixa_feedback'] = pd.cut(df['Feedback Score'], bins=[0, 2, 3.5, 5],
    labels=['Baixo (1-2)', 'Médio (2-3.5)', 'Alto (3.5-5)'])
sat_fb = df.groupby('faixa_feedback', observed=True)['Satisfaction Rate (%)'].mean().reset_index()
sat_fb.columns = ['faixa_feedback', 'satisfacao_media']
fig = px.bar(sat_fb, x='faixa_feedback', y='satisfacao_media',
    title='Satisfação por Nível de Feedback Recebido',
    labels={'faixa_feedback': 'Feedback Score', 'satisfacao_media': 'Satisfação Média (%)'},
    color='satisfacao_media',
    color_continuous_scale=['#ef5350', '#ffa726', '#66bb6a'],
    text=sat_fb['satisfacao_media'].round(1).astype(str) + '%')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
salvar(fig, '02d_satisfacao_feedback')

# 02-E: satisfação × salário
df['quartil_salario'] = pd.qcut(df['Salary'], q=4, labels=['Q1 (menor)', 'Q2', 'Q3', 'Q4 (maior)'])
sat_sal = df.groupby('quartil_salario', observed=True)['Satisfaction Rate (%)'].mean().reset_index()
sat_sal.columns = ['quartil', 'satisfacao_media']
fig = px.bar(sat_sal, x='quartil', y='satisfacao_media',
    title='Satisfação por Faixa Salarial (Quartis)',
    labels={'quartil': 'Faixa Salarial', 'satisfacao_media': 'Satisfação Média (%)'},
    color='satisfacao_media',
    color_continuous_scale=['#ef5350', '#ffa726', '#66bb6a'],
    text=sat_sal['satisfacao_media'].round(1).astype(str) + '%')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
salvar(fig, '02e_satisfacao_salario')

# 02-F: satisfação × tempo de casa
sat_tempo = df.groupby('faixa_tempo', observed=True)['Satisfaction Rate (%)'].mean().reset_index()
sat_tempo.columns = ['faixa', 'satisfacao_media']
fig = px.line(sat_tempo, x='faixa', y='satisfacao_media',
    title='Satisfação por Tempo de Casa',
    labels={'faixa': 'Tempo de Casa', 'satisfacao_media': 'Satisfação Média (%)'},
    markers=True)
fig.update_traces(line_color='#2196F3', marker_size=10)
fig.add_hline(y=df['Satisfaction Rate (%)'].mean(), line_dash='dash', line_color='gray', annotation_text='Média geral')
salvar(fig, '02f_satisfacao_tempo_casa')

# 02-G: mapa de calor de correlações
colunas_num = ['Satisfaction Rate (%)', 'Productivity (%)', 'Feedback Score', 'Salary', 'Age', 'anos_empresa', 'Projects Completed']
nomes_pt = ['Satisfação', 'Produtividade', 'Feedback', 'Salário', 'Idade', 'Tempo de Casa', 'Projetos']
corr_matrix = df[colunas_num].corr()
corr_matrix.index = nomes_pt
corr_matrix.columns = nomes_pt
fig = px.imshow(corr_matrix, title='Correlação entre Variáveis',
    color_continuous_scale='RdBu', zmin=-1, zmax=1, text_auto='.2f')
salvar(fig, '02g_mapa_correlacoes')

print('=== Notebook 03 — Insights e Ações ===')

# 03-A: mapa de risco
fig = px.scatter(df, x='Satisfaction Rate (%)', y='Productivity (%)',
    color='risco',
    color_discrete_map={'Alto': '#ef5350', 'Médio': '#ffa726', 'Atenção': '#ffee58', 'Normal': '#66bb6a'},
    title='Mapa de Risco: Satisfação × Produtividade',
    labels={'Satisfaction Rate (%)': 'Satisfação (%)', 'Productivity (%)': 'Produtividade (%)'},
    hover_data=['Name', 'Department', 'Position'])
fig.add_vline(x=33, line_dash='dash', line_color='gray')
fig.add_hline(y=40, line_dash='dash', line_color='gray')
salvar(fig, '03a_mapa_risco')

# 03-B: diagnóstico por departamento
depto_risco = df.groupby('Department').agg(
    satisfacao_media=('Satisfaction Rate (%)', 'mean'),
    total=('Name', 'count'),
    risco_alto=('risco', lambda x: (x == 'Alto').sum())
).reset_index()
depto_risco['pct_risco_alto'] = (depto_risco['risco_alto'] / depto_risco['total'] * 100).round(1)
depto_risco = depto_risco.sort_values('satisfacao_media')

fig = make_subplots(rows=1, cols=2,
    subplot_titles=['Satisfação Média por Departamento', '% em Risco Alto por Departamento'])
fig.add_trace(go.Bar(
    y=depto_risco['Department'], x=depto_risco['satisfacao_media'],
    orientation='h', marker_color='#2196F3',
    text=depto_risco['satisfacao_media'].round(1).astype(str) + '%',
    textposition='outside', name='Satisfação'), row=1, col=1)
fig.add_trace(go.Bar(
    y=depto_risco['Department'], x=depto_risco['pct_risco_alto'],
    orientation='h', marker_color='#ef5350',
    text=depto_risco['pct_risco_alto'].astype(str) + '%',
    textposition='outside', name='Risco Alto'), row=1, col=2)
fig.update_layout(title='Diagnóstico por Departamento', showlegend=False, height=400)
salvar(fig, '03b_diagnostico_departamentos')

# 03-C: % com feedback baixo por departamento
df['feedback_baixo'] = df['Feedback Score'] < 2
fb_depto = df.groupby('Department').agg(
    total=('Name', 'count'),
    feedback_baixo=('feedback_baixo', 'sum')
).reset_index()
fb_depto['pct_fb_baixo'] = (fb_depto['feedback_baixo'] / fb_depto['total'] * 100).round(1)
fig = px.bar(
    fb_depto.sort_values('pct_fb_baixo', ascending=False),
    x='Department', y='pct_fb_baixo',
    title='% de Colaboradores com Feedback Baixo (< 2.0) por Departamento',
    labels={'Department': 'Departamento', 'pct_fb_baixo': '% com Feedback Baixo'},
    color='pct_fb_baixo',
    color_continuous_scale=['#66bb6a', '#ffa726', '#ef5350'],
    text=fb_depto.sort_values('pct_fb_baixo', ascending=False)['pct_fb_baixo'].astype(str) + '%')
fig.update_traces(textposition='outside')
fig.update_layout(coloraxis_showscale=False)
salvar(fig, '03c_feedback_baixo_departamento')

print('\nConcluído.')
