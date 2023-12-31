import streamlit as st
import api_manager
from layout import render_header, render_sidebar

# Função para filtrar itens por categoria
def filtrar_itens_por_categoria(itens, categoria_selecionada):
    return [item for item in itens if item['categoria'] == categoria_selecionada]

# Página de categorias
def mostrar_pagina_categorias(itens):
    token = api_manager.get_token()
    
    # Inicializa a categoria default (que a gente colocar aqui) no estado da sessão se ela ainda não existir
    if 'categoria_selecionada' not in st.session_state:
        st.session_state['categoria_selecionada'] = 'Arduino'

    st.title("Categorias")
    
    # Layout de duas colunas
    col1, col2 = st.columns([1, 3])

    # Categorias e Filtros
    with col1:
        st.subheader("Filtrar por Categoria")
        categorias = ["Arduino", "Componentes", "Protoboards", "Kits Arduinos", "Jumpers", "Eletrôdos"]
        for categoria in categorias:
            if st.button(categoria, key=categoria):
                st.session_state['categoria_selecionada'] = categoria

        # Adicionar mais filtros conforme necessário

    # Itens
    with col2:
        # Filtrar itens pela categoria selecionada
        itens_filtrados = filtrar_itens_por_categoria(itens, st.session_state['categoria_selecionada'])

        st.write(f"{len(itens_filtrados)} resultados para {st.session_state['categoria_selecionada']}")

        # Organizar itens em uma grade
        num_columns = 3
        rows = [itens_filtrados[i:i+num_columns] for i in range(0, len(itens_filtrados), num_columns)]

        for row in rows:
            cols = st.columns(num_columns)
            for index, item in enumerate(row):
                with cols[index]:
                    st.subheader(item['nome'])
                    st.write(f"Disponibilidade: {item['disponibilidade']}")
                    st.write(item['descricao'])
                    # Adicione um evento no botão que atualiza o estado da sessão e faz um rerun
                    if st.button("Solicitar", key=f"btn_solicitar_{item['nome']}"):
                        # Atualiza a página atual no estado da sessão
                        st.session_state['current_page'] = 'item_request'
                        # Armazena os dados do item atual no estado da sessão
                        st.session_state['current_item'] = item
                        # Força o Streamlit a fazer um rerun para atualizar a página

# Chamada da função que mostra a página de categorias
if __name__ == "__main__":
    mostrar_pagina_categorias([])
