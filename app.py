import streamlit as st
import api_manager

# Configuração inicial da página
st.set_page_config(page_title='Rent Up', layout='wide')

# Importações dos módulos das páginas
from home import run_home_page
from categorias import mostrar_pagina_categorias
from item_request import show_item_request_page  
from cart import show_cart_page
from layout import render_header, render_sidebar, render_footer
from search_results import show_search_results

# Inicialização do estado da sessão
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'
    
st.session_state['auth_token'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDEwNjEzNDIsImlhdCI6MTcwMTA0MzM0Miwic3ViIjoidXNlcnRlc3RlQGNlc2FyLnNjaG9vbCJ9.PsQ_hWxrXVueKS0FunuUR0VOqduU-o5AOdTiaG_N3eE"


# Função para controle da navegação das páginas
def navigation_control():
    # As páginas são controladas pelo estado da sessão 'current_page'
    if st.session_state['current_page'] == 'home':
        run_home_page()
    elif st.session_state['current_page'] == 'categorias':
        if st.session_state['auth_token']:
            items = api_manager.get_all_items(st.session_state['auth_token'])
            mostrar_pagina_categorias(items)
        else:
            st.error("Por favor, faça login para visualizar as categorias.")
    elif st.session_state['current_page'] == 'item_request':
        item_data = st.session_state.get('current_item', None)
        if item_data:
            show_item_request_page(item_data)
        else:
            st.error("Erro: Dados do item não encontrados.")
    elif st.session_state['current_page'] == 'cart':
        show_cart_page()
    elif st.session_state['current_page'] == 'search_results':
        search_term = st.session_state.get('search_term', '')
        if st.session_state['auth_token']:
            show_search_results(search_term, st.session_state['auth_token'])
        else:
            st.error("Por favor, faça login para buscar itens.")
            

# Função principal para executar o aplicativo
def main():
    render_header("main")
    render_sidebar()
    navigation_control()
    render_footer()

# Ponto de entrada do script
if __name__ == "__main__":
    main()
