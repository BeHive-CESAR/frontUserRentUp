# search_results.py
import streamlit as st

import api_manager

def show_search_results(search_term, token):
    st.title(f"Resultados para '{search_term}'")

    if search_term:
        response = api_manager.get_item_by_name(token, search_term)
        if response and 'item' in response:
            item = response['item']
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.subheader(item.get('nome_item'))
                st.caption(item.get('descricao'))
                st.write(f"Disponivel: {item.get('qnt_emprestar')}")

                # Botão 'Adicionar a sacola'
                if st.button("Adicionar a sacola", key=f"rent_{item['nome_item']}"):
                    # Inicializa o carrinho se ele não existir
                    if 'cart' not in st.session_state:
                        st.session_state.cart = []
                    # Adiciona o item ao carrinho
                    st.session_state.cart.append({
                        'nome': item['nome_item'],
                        'quantidade': 1  # Define a quantidade inicial como 1
                    })
                    st.success(f"{item['nome_item']} adicionado a sacola.")
                
                # Botão 'Mostrar detalhes'
                if st.button("Mostrar detalhes", key=f"details_{item['nome_item']}"):
                    st.session_state['current_item'] = item
                    st.session_state['current_page'] = 'item_request'
        else:
            st.write(f"Nenhum item encontrado com o nome '{search_term}'.")
    else:
        st.write("Digite algo para buscar.")

if __name__ == "__main__":
    show_search_results([], [])
