import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from pages.util.notas_dataset import read_saude_mental_df, build_nota_saude_mental, build_dataframe_section, get_color_sequence_names, get_color_sequence

def build_page():
    build_header()
    build_body()

def build_header():
    text ='<h1>Plots com a base de Saúde Mental</h1>'+\
    '<p>Esta página apresenta alguns gráficos a partir da base de dados do '+\
    'Saúde Mental (https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset/data).</p>'
    st.write(text, unsafe_allow_html=True)
    build_nota_saude_mental()
    
def build_body():
    df = read_saude_mental_df()
    build_dataframe_section(df)
    
    st.markdown('<h2>Gráficos Relativos à Instabilidade emocionais</h2>', unsafe_allow_html=True)
    build_histograma_section(df)
    build_boxplot_section(df)
    build_bar_section(df)

#Sessão das funções dos gráficos:
def build_histograma_section(df:pd.DataFrame):
    st.markdown('<h3>Histograma</h3>', unsafe_allow_html=True)
    c1, c2 = st.columns([.3,.7])
    cols = ['Crescimento_de_Estresse', 'Mudancas_de_humor', 'Falta_de_Foco', 'Debilidade_Social']
    series_col = c1.selectbox('Instabilidades*', options=cols, key='serie_1')
    stacked = c1.checkbox('Empilhado', value=True)
    color_sequence_name = c1.selectbox('Escala de Cor', options=get_color_sequence_names())
    color_sequence = get_color_sequence(color_sequence_name)
    if stacked:
        fig = create_histograma_stacked(df, series_col, color_sequence)
    else:
        fig = create_histograma_unstacked(df, series_col, color_sequence)
    c2.plotly_chart(fig, use_container_width=True)
    fig.update_layout(title=f'Histograma de "{series_col}" por dias em casa.', 
                      legend_title_text=series_col, xaxis_title_text='Dias em casa', yaxis_title_text='Quantidade')

def create_histograma_stacked(df:pd.DataFrame, series_col:str, color_sequence) -> go.Figure:
    df = df.query(f'{series_col}.notna()').copy()
    df.sort_values(by=series_col, inplace=True)
    return px.histogram(df, x='Dias_em_casa', nbins=20, color=series_col, 
                        opacity=.75, color_discrete_sequence=color_sequence)

def create_histograma_unstacked(df:pd.DataFrame, series_col:str, color_sequence) -> go.Figure:
    # em alguns casos, pode ser interessante ou mesmo necessário usar a api graph objects do plotly: https://plotly.com/python/graph-objects/
    # esta api se baseia na inclusão de 'traces' sobre uma figura. ademais, propriedades e eixos da figura e dos traces podem ser customizados
    # apesar de mais complexo, o uso destes elementos diretamente permite que cada elemetno do gráfico seja ajustado individualmente.
    series_vals = ordered_vals(df, series_col)
    fig = go.Figure()
    color_idx = 0
    for val in series_vals:
        query = f'{series_col}==@val'
        df_aux = df.query(query).copy()
        opacity = .5 * (1+color_idx/10)
        str_series = str(val)
        #showlegend e o legendgroup são usados para mostrar apenas a legenda da primeira linha
        #e permitir que a interação com a legenda altere o estado de todos os subplots
        color = f'{color_sequence[color_idx]}'
        hist = go.Histogram(name=str_series, x=df_aux['Dias_em_casa'], 
                            xbins=dict(start=0,end=80,size=5), legendgroup=val, showlegend=True,
                            marker={'color': color, 'opacity':opacity})
        fig.add_trace(hist)
        color_idx += 1
    fig.update_layout(barmode='overlay', legend_title_text=series_col)
    return fig

def ordered_vals(df:pd.DataFrame, col:str) -> list:
    result = df[[col]].groupby(by=col).count().\
        reset_index().copy()
    return result[col].to_list()

def build_boxplot_section(df:pd.DataFrame):
    st.markdown('<h3>Diagrama de Caixa (<i>Boxplot</i>)</h3>', unsafe_allow_html=True)
    c1, c2 = st.columns([.3,.7])
    cols = ['Crescimento_de_Estresse', 'Mudancas_de_humor', 'Falta_de_Foco', 'Debilidade_Social']
    serie_col = c1.selectbox('Instabilidade*', options=cols, key='serie_2')
    inverter = c1.checkbox('Inverter Eixos', True)
    cols = [serie_col, 'Dias_em_casa']
    cols.reverse()
    if inverter:
        cols.reverse()
    df_plot = df[cols]
    fig = px.box(df_plot,x=cols[0],y=cols[1])
    c2.plotly_chart(fig, use_container_width=True)
    
def build_bar_section(df:pd.DataFrame):
    st.markdown('<h3>Diagrama de Barras (<i>Bar</i>)</h3>', unsafe_allow_html=True)
    c1, c2 = st.columns([.3,.7])
    cols = ['Crescimento_de_Estresse', 'Mudancas_de_humor', 'Falta_de_Foco', 'Debilidade_Social']
    serie_col = c1.selectbox('Instabilidade*', options=cols, key='serie_3')
    df_plot = df[serie_col]
    fig = px.bar(df_plot, title='Distribuição da quantidade de Instabilidades')
    fig.update_yaxes(title='count')
    c2.plotly_chart(fig, use_container_width=True)
#Fim da Sessão    

build_page()