import streamlit as st
import requests
from PIL import Image
import pandas as pd
import numpy as np
import json
import base64

# Configuração da página
st.set_page_config(page_title='Rent Up', layout='wide')


def get_image_as_base64(filepath):
    with open(filepath, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def local_css(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def icon(icon_name):
    return f'<i class="material-icons">{icon_name}</i>'

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

encoded_image = get_image_as_base64('img/logo.png')

# Custom header com a imagem codificada em base64
st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{encoded_image}" class="logo">
        <div class="search-box">
            <span class="material-icons">search</span>
            <input type="text" class="search-input" placeholder="Procure por algo">
        </div>
        <span class="material-icons icon">account_circle</span>
        <span class="material-icons icon">shopping_cart</span>
    </div>
    <div class="navigation">
        <button class="nav-btn active">HOME</button>
        <button class="nav-btn">CATEGORIAS</button>
        <button class="nav-btn">DESTAQUES</button>
        <button class="nav-btn">SUPORTE</button>
        <button class="nav-btn">MINHA CONTA</button>
    </div>
""", unsafe_allow_html=True)

# Barra de navegação secundária
st.markdown("""
<div class="secondary-nav">
        <button class="sec-nav-btn active">Mais buscados</button>
        <button class="sec-nav-btn">Novidades</button>
        <button class="sec-nav-btn">Kits Arduinos</button>
        <button class="sec-nav-btn">Fórum GARAgino</button>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div class="footer-section">
            <h5>Quem somos</h5>
            <a href="#">Conheça a RentUp</a>
            <a href="#">Nossos produtos</a>
            <a href="#">Lorem ipsum</a>
        </div>
        <div class="footer-section">
            <h5>Comunidade</h5>
            <a href="#">Garagem</a>
            <a href="#">GaRAgino</a>
            <a href="#">Lorem ipsum</a>
        </div>
        <div class="footer-section">
            <h5>Ajuda</h5>
            <a href="#">Falar com suporte</a>
            <a href="#">Lorem ipsum</a>
            <a href="#">Lorem ipsum</a>
        </div>
    </div>
""", unsafe_allow_html=True)