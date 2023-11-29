import streamlit as st
import api_manager
import json, os
from PIL import Image
import requests
import pandas as pd

def run_home_page():
    token = api_manager.get_token()
    # Verifica se o usuário está autenticado
    if api_manager.check_status():
        # Obter itens usando a API
        items = api_manager.get_all_items(token)

        if items:
            # Mostrar itens
            st.markdown("---")  # Linha divisória

            # cols = st.columns(3)  # Criar 3 colunas
            # for i in range(min(3, len(items['itens']))):  # Iterar apenas pelos 3 primeiros itens
            #     item = items['itens'][i]
            #     with cols[i]:
            #         st.write(f"Nome: {item['nome_item']}")
            #         st.write(f"Disponibilidade: {item['qnt_emprestar']}")
            #         st.write(f"Descrição: {item['descricao']}")
            
            # Mostrar itens usando a biblioteca Pandas
            df = pd.DataFrame(items['itens'])
            df.columns = ['Item', 'Total', 'Em estoque', 'Disponíveis', 'Emprestados', 'Quebrados', 'Descrição', 'Imagem']
           
            df = df.drop(columns=['Total','Em estoque', 'Emprestados', 'Quebrados','Imagem'])
            st.dataframe(df, hide_index=True)
            
        else:
            st.write("Nenhum item disponível no momento.")
    else:
        st.warning("Você precisa estar logado para ver os itens disponíveis.")
    
# Chamada da função que mostra a página home
if __name__ == "__main__":
    run_home_page()
