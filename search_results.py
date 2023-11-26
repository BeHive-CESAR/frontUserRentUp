# search_results.py
import streamlit as st
import api_manager

def show_search_results(search_term, token):
    st.title(f"Resultados para '{search_term}'")  # O que o usuario pesquisou é o título da página

    if search_term:
        results = api_manager.get_item_by_name(token, search_term)

        if results:
            # Cria uma grade com cartões para cada item encontrado
            for item in results:
                # Estrutura de colunas para os itens
                col1, col2, col3 = st.columns([1, 2, 1], gap="small")
                with col2:  # Centraliza o cartão na coluna do meio
                    st.card(
                        image=item.get('imagem_url', ''),  # Depois ver para fornecer uma imagem padrão caso não exista
                        title=item.get('nome', 'Nome não disponível'),
                        description=item.get('descricao', 'Descrição não disponível'),
                        # Botões para solicitar e adicionar ao carrinho colocar aqui
                    )
            if not results:
                st.write("Nenhum item encontrado com esse nome.")
    else:
        st.write("Digite algo para buscar.")
