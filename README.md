# PISI 3 - SAÚDE MENTAL
Desenvolvido em disciplina de Projeto Interdisciplinar para Sistemas de Informação 3(PISI3)

por: Arthur de Barros (<arthur.bbsantos@ufrpe.br>)

Trabalho científico feito no curso de Bacharelado em Sistemas de Informação (BSI) da Sede, da Universidade Federal Rural de Pernambuco (UFRPE).

## Resumo do projeto

Utiliza-se  Streamlit, linguagem Python para abordagem com Machine Learning voltado à análise de dados sobre saúde mental.<br>
O Dataset encontra-se em : (<https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset/data>) <br>
Com o objetivo de aprendizado, descobrir insights e gerar um conhecimento duradouro através do potencial do Machine Learning

## Instalação

* Instale o VSCode.
* Efetue o clone do projeto: `CTRL+SHIFT+P > Git:Clone > Clone from GitHub > https://github.com/arthurbo1/pisi3-saude-mental`
* Instale o python.
* Acesse a aba "Terminal" disponível na parte inferior do VSCode.
* Execute a linha abaixo para criar um ambiente virtual do python para o projeto. Observe que a pasta `.venv` está no `.gitignore`. <br>
    `python -m venv .venv`
* Atualize o pip:
    `python -m pip install --upgrade pip`  
* Instale as libs necessárias para o projeto:
    `pip install -r requirements.txt --upgrade`
* Rode o sistema:
    `streamlit run Home.py`
