# app.py
import streamlit as st

st.set_page_config(page_title='Rent Up', layout='wide')

from home import run_home_page
from categorias import mostrar_pagina_categorias
from layout import render_header, render_sidebar, render_footer

# Inicializa a chave 'current_page' no estado da sessão se ela ainda não existir
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

# Função para controlar a navegação da página
def navigation_control():
    # As páginas são controladas pelo estado da sessão 'current_page'
    if st.session_state['current_page'] == 'home':
        run_home_page()
    elif st.session_state['current_page'] == 'categorias':
        mostrar_pagina_categorias()
    # Se tiver mais paginas, adicionar aqui

# Main - executa as funções que renderizam o layout da página
def main():
    render_header("main")
    render_sidebar()
    navigation_control()
    render_footer()

if __name__ == "__main__":
    main()
