import streamlit as st
import requests
from PIL import Image
import pandas as pd
import numpy as np
import json
import base64

# Configuração da página
st.set_page_config(page_title='Rent Up', layout='wide')

# Injeção de CSS personalizado
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Header
header_col1, header_col2, header_col3, header_col4 = st.columns([1, 8, 1, 1])

with header_col1:
    logo = Image.open('img/logo.png')
    st.image(logo, width=100)

with header_col2:
    st.text_input("", placeholder="Procure por algo")

with header_col3:
    st.button("Conta")

with header_col4:
    st.button("Carrinho")

# SideBar
# Lista de botões para a navegação principal
nav_buttons = ['HOME', 'CATEGORIAS', 'DESTAQUES', 'SUPORTE', 'MINHA CONTA']

# Loop para adicionar cada botão na sidebar
for button in nav_buttons:
    st.sidebar.button(button)

# Navegação secundária
st.markdown("---")  
sec_nav_buttons = ['Mais buscados', 'Novidades', 'Kits Arduinos', 'Fórum GARAgino']

# Cria espaçamento à esquerda
st.write("")  # Isso cria um espaço vazio antes dos botões

# Define o número de colunas incluindo espaços vazios
cols = st.columns((1, *([2] * len(sec_nav_buttons)), 1))

# Coloca cada botão em sua própria coluna, ignorando a primeira e última coluna que são espaços vazios
for i, button in enumerate(sec_nav_buttons, start=1):
    cols[i].button(button)

# Cria espaçamento à direita
# Cria um espaço vazio após os botões
st.write("")  


#Footer
# Insere outra linha divisória
st.markdown("---")  

# Cria 3 colunas com cabeçalhos e botões
spacer_left, col1, col2, col3, spacer_right = st.columns([1, 2, 2, 2, 1])
with col1:
    st.subheader("Quem somos")
    st.button("Conheça a RentUp", key="1")
    st.button("Nossos produtos", key="2")
    st.button("Onde estamos", key="3")

with col2:
    st.subheader("Links")
    st.button("Novidades", key="4")
    st.button("Mais buscados", key="5") 
    st.button("Fórum GARAgino", key="6")

with col3:
    st.subheader("Ajuda")
    st.button("Entre em contato", key="7")
    st.button("Reportar problema", key="8")
    st.button("Suporte", key="9")

# Insere uma linha divisória
st.markdown("""---""") 
footer_col1, footer_col2, footer_col3 = st.columns([6, 5, 5])
with footer_col2:
    st.write("© 2023 by RentUp. All rights reserved.")