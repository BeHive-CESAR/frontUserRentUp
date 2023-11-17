import streamlit as st

# Usuário: [user@user.com] e [User100%]

st.set_page_config(page_title='Rent Up', layout='wide')

from home import run_home_page
from categorias import mostrar_pagina_categorias
from item_request import show_item_request_page  
from cart import show_cart_page
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
    elif st.session_state['current_page'] == 'item_request':
        # Aqui você passa os dados do item para a função
        item_data = st.session_state.get('current_item', None)
        if item_data is not None:
            show_item_request_page(item_data)
        else:
            st.error("Erro: Dados do item não encontrados.")
    elif st.session_state['current_page'] == 'cart':
        show_cart_page()  # Adiciona a página do carrinho na navegação
    # Se tiver mais paginas, adicionar aqui

# Main - executa as funções que renderizam o layout da página
def main():
    render_header("main")
    render_sidebar()
    navigation_control()
    render_footer()

if __name__ == "__main__":
    main()
