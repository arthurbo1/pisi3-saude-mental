<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np


def build_header():
    text = '''<h1> Alento - Aprendizado de máquina para observar a saúde mental</h1>
        <p>
        <code>Grupo 12 : Arthur de Barros Botelho dos Santos</code>
        <p> Contato: arthur.bbsanto@ufrpe.br</p>
        <p>
        <p> Projeto desenvolvido na disicplina de Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3)'''
    st.write(text, unsafe_allow_html=True)


build_header()
st.subheader('Visão geral do Dataset')

data = pd.read_csv('data\Mental_Health_Dataset.csv')

if st.checkbox('Mostrar dados brutos'):
    st.subheader('Saúde mental Dataset')
    st.write(data)
=======
import streamlit as st
import pandas as pd
import numpy as np


def build_header():
    text = '''<h1> Alento - Aprendizado de máquina para observar a saúde mental</h1>
        <p>
        <code>Grupo 12 : Arthur de Barros Botelho dos Santos</code>
        <p> Contato: arthur.bbsanto@ufrpe.br</p>
        <p>
        <p> Projeto desenvolvido na disicplina de Projeto Interdisciplinar para Sistemas de Informação 3 (PISI3)'''
    st.write(text, unsafe_allow_html=True)


build_header()
st.subheader('Visão geral do Dataset')

data = pd.read_csv('data\Mental_Health_Dataset.csv')

if st.checkbox('Mostrar dados brutos'):
    st.subheader('Saúde mental Dataset')
    st.write(data)
>>>>>>> 712c3c5 (commit inicial - Data Profiling e gráficos iniciais)
