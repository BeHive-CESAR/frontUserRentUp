import streamlit as st
import requests
from PIL import Image
import pandas as pd
import numpy as np
import json
import base64
from layout import render_header, render_sidebar

def run_home_page():
    # Nav bar secundária
    st.markdown("---")  
    sec_nav_buttons = ['Mais buscados', 'Novidades', 'Kits Arduinos', 'Fórum GARAgino']

    # Cria espaçamento à esquerda
    st.write("")  # Cria um espaço vazio antes dos botões

    # Define o número de colunas incluindo espaços vazios (pra ficar bonitinho e centralizado)
    cols = st.columns((1, *([2] * len(sec_nav_buttons)), 1))

    # Coloca cada botão em sua própria coluna, ignorando a primeira e última coluna que são espaços vazios
    for i, button in enumerate(sec_nav_buttons, start=1):
        cols[i].button(button)

    # Cria espaçamento à direita
    st.write("")  # Cria um espaço vazio após os botões


# Injeção de CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


