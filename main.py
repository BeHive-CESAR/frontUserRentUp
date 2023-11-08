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
header_col1, header_col2, header_col3 = st.columns([1, 8, 2])

with header_col1:
    logo = Image.open('img/logo.png')
    st.image(logo, width=100)

with header_col2:
    st.text_input("", placeholder="Procure por algo")

with header_col3:
    st.button("Account")
    st.button("Shopping Cart")

# SideBar
# Lista de botões para a navegação principal
nav_buttons = ['HOME', 'CATEGORIAS', 'DESTAQUES', 'SUPORTE', 'MINHA CONTA']

# Loop para adicionar cada botão na sidebar
for button in nav_buttons:
    st.sidebar.button(button)

# Navegação secundária
# Insere linha divisória
st.markdown("""---""")  
sec_nav_buttons = ['Mais buscados', 'Novidades', 'Kits Arduinos', 'Fórum GARAgino']
sec_nav_cols = st.columns(len(sec_nav_buttons)) # Seleciona a quantidade de colunas a partir da quantidade de itens no array "sec_nav_buttons"
for i, button in enumerate(sec_nav_buttons):
    with sec_nav_cols[i]:
        st.button(button)

#Footer
# Insere outra linha divisória
st.markdown("---")  

# Cria 3 colunas com cabeçalhos e botões
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Quem somos")
    st.button("Conheça a RentUp")
    st.button("Nossos produtos")

with col2:
    st.subheader("Comunidade")
    st.button("Garagem")
    st.button("GARAgino")

with col3:
    st.subheader("Ajuda")
    st.button("Falar com suporte")

# Insere uma linha divisória
st.markdown("""---""") 
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.write("Rent Up © 2023")