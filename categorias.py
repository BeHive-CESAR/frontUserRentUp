import streamlit as st
import requests
from PIL import Image
import pandas as pd
import numpy as np
import json
import base64
from layout import render_header, render_sidebar

# Dunção placeholder ate eu aprender a usar a API
def get_dummy_data():
   
    return [
        {'nome': 'Arduino Starter Kit TC-2', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
        {'nome': 'Arduino Starter Kit', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
        {'nome': 'Arduino Intermed Kit', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
        {'nome': 'Arduino Master Kit', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
        {'nome': 'Arduino Master Kit V2', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
        {'nome': 'Arduino Kit', 'descricao': 'Contém 10 itens', 'categoria': 'Kits Arduinos'},
    ]

# Página de categorias
def mostrar_pagina_categorias():
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

        st.subheader("Filtrar por Voltagem")
        if st.button('110V', key='110V'):
            # lógica de filtrar por voltagem aqui (se ainda for ter no produto final ne)
            pass
        if st.button('220V', key='220V'):
            # lógica de filtrar por voltagem aqui (se ainda for ter no produto final ne)
            pass

    # Itens
    with col2:
        # Dados simulados dos itens (a ser substituído pela chamada da API)
        itens = get_dummy_data()

        # Filtrar itens pela categoria selecionada
        itens_filtrados = [item for item in itens if item['categoria'] == st.session_state['categoria_selecionada']]

        st.write(f"{len(itens_filtrados)} resultados para {st.session_state['categoria_selecionada']}")
        # Organizar itens em uma grade
        # Aqui você pode definir quantas colunas por linha você quer, por exemplo, 3
        num_columns = 3
        rows = [itens_filtrados[i:i+num_columns] for i in range(0, len(itens_filtrados), num_columns)]

        for row in rows:
            cols = st.columns(num_columns)
            for index, item in enumerate(row):
                with cols[index]:
                    st.subheader(item['nome'])
                    st.write(item['descricao'])
                    st.button("Solicitar", key=f"btn_solicitar_{item['nome']}") # Ainda não faz nada

                

# Chamada da função que mostra a página de categorias
if __name__ == "__main__":
    mostrar_pagina_categorias()