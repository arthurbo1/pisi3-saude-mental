import pandas as pd
import streamlit as st
import plotly.express as px
from utils import read_df

def build_nota_saude_mental():
    with st.expander('Notas sobre o dataset de Saúde mental'):
        st.write(
        '''
        <table>
            <tr><th>COLUNA ORIGINAL</th><th>COLUNA</th><th>DESCRIÇÃO</th></tr>
            <tr><td>Timestamp</td><td>Data_hora</td><td>Data e hora que a pesquisa foi feita.</td></tr>
            <tr><td>Gender</td><td>Sexo</td><td>Sexo do entrevistado.</td></tr>
            <tr><td>Country</td><td>País</td><td>País no qual foi feita a pesquisa.</td></tr>
            <tr><td>Ocupation</td><td>Ocupação</td><td>Inclui atividades dos intrevistados ou qual tipo de profissão.</td></tr>
            <tr><td>self_employed</td><td>Autonomo</td><td>É trabalhador autônomo?</td></tr>
            <tr><td>family_history</td><td>Historico_Familiar</td><td>Você tem histórico familiar de doenças mentais?</td></tr>
            <tr><td>treatment</td><td>Tratamento</td><td>Você procurou tratamento para alguma condição de saúde mental?</td></tr>
            <tr><td>Days_indoors</td><td>Dias_em_casa</td><td>Quanto tempo costuma passar sequencialmente sem sair de casa?</td></tr>
            <tr><td>Growing_Stress</td><td>Crescimento_de_Estresse</td><td>Você percebeu algum aumento no estresse?</td></tr>
            <tr><td>Changes_Habits</td><td>Mudancas_de_habitos</td><td>Você mudaria de hábitos em caso de falta de saúde mental?</td></tr>
            <tr><td>Mental_Health_History</td><td>Historico_Saude_Mental</td><td>Você apresenta histórico de saúde mental?</td></tr>
            <tr><td>Mood_Swings</td><td>Mudancas_de_humor</td><td>Em que níveis você apresenta mudanças de humor?</td></tr>
            <tr><td>Coping_Struggles</td><td>Falta_de_Foco</td><td>Você apresenta dificuldade em focar em algo?</td></tr>
            <tr><td>Work_Interest</td><td>Interesse_Profissional</td><td>Você sente interesse em trabalhar?</td></tr>
            <tr><td>Social_Weakness</td><td>Debilidade_Social</td><td>Você sente debilidade em sua capacidades sociais?</td></tr>
            <tr><td>mental_health_interview</td><td>Entrevista_Saude_Mental</td><td>Você falaria sobre algum problema na sua saúde mental para um possível empregador em uma entrevista?</td></tr>
            <tr><td>care_options</td><td>Opções_de_Cuidado</td><td>Você tem conhecimento das formas de cuidados com a saúde mental?</td></tr>
        </table>
        <br>
        Notas:<br>
        Mood_Swings: níveis das Mudanças de humor:<br>
        High =  Alta<br>
        Medium = Média<br>
        Low =  Baixa<br>
        ''', unsafe_allow_html=True)
        
def build_dataframe_section(df:pd.DataFrame):
    st.write('<h2>Dados de Saúde Mental</h2>', unsafe_allow_html=True)
    st.dataframe(df)
    
def __ingest_saude_mental_data() -> pd.DataFrame:
    df = read_df('Mental_Health_Dataset')
    df.rename(columns={
        'Timestamp':'Data_hora','Gender':'Sexo',
        'Country':'País','Ocupation':'Ocupação',
        'self_employed':'Autonomo','family_history':'Historico_Familiar','treatment':'Tratamento',
        'Days_Indoors':'Dias_em_casa','Growing_Stress':'Crescimento_de_Estresse',
        'Changes_Habits':'Mudancas_de_habitos','Mental_Health_History':'Historico_Saude_Mental','Mood_Swings':'Mudancas_de_humor',
        'Coping_Struggles':'Falta_de_Foco','Work_Interest':'Interesse_Profissional','Social_Weakness':'Debilidade_Social',
        'mental_health_interview':'Entrevista_Saude_Mental','care_options':'Opções_de_Cuidado'
    }, inplace=True)
    return df

def __get_color_sequence_map() -> dict[str,list[str]]:
    def filter(colors) -> list[str]:
        #código usado para alternar as cores, para aumentar a diferença da tonalidade
        return [x for idx, x in enumerate(colors) if idx%2!=0]
    result = {
        'Azul (reverso)': filter(px.colors.sequential.Blues_r),
        'Azul': filter(px.colors.sequential.Blues),
        'Plasma (reverso)': filter(px.colors.sequential.Plasma_r),
        'Plasma': filter(px.colors.sequential.Plasma),
        'Vermelho (reverso)': filter(px.colors.sequential.Reds_r),
        'Vermelho': filter(px.colors.sequential.Reds),
    }
    return result

def get_color_sequence_names() -> list[str]:
    return __get_color_sequence_map().keys()

def get_color_sequence(name) -> list[str]:
    return __get_color_sequence_map()[name]

def read_saude_mental_df() -> pd.DataFrame:
    return __ingest_saude_mental_data()