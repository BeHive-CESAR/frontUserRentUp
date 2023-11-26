import streamlit as st
import api_manager
from layout import render_header, render_sidebar

def run_home_page():
    # Verifica se o usuário está autenticado
    if 'auth_token' in st.session_state and st.session_state['auth_token']:
        # Obter itens usando a API
        items = api_manager.get_all_items(st.session_state['auth_token'])
        
        if items:
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

            # Apresentar itens
            for item in items:
                st.write(item['nome'])  # Substitua 'nome' pelo nome da chave correspondente no seu JSON
                st.write(f"Disponibilidade: {item['disponibilidade']}")
                st.write(item['descricao'])
        else:
            st.write("Nenhum item disponível no momento.")

    else:
        st.error("Por favor, faça login para acessar os itens.")

# Chamada da função que mostra a página home
if __name__ == "__main__":
    run_home_page()
