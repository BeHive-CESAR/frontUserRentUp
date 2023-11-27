import streamlit as st
import api_manager

def run_home_page():
    # Verifica se o usuário está autenticado
    if 'auth_token' in st.session_state and st.session_state['auth_token']:
        # Obter itens usando a API
        items = api_manager.get_all_items(st.session_state['auth_token'])

        if items:
            # Mostrar itens
            st.markdown("---")  # Linha divisória

            cols = st.columns(3)  # Criar 3 colunas
            for i in range(min(3, len(items['itens']))):  # Iterar apenas pelos 3 primeiros itens
                item = items['itens'][i]
                with cols[i]:
                    st.write(f"Nome: {item['nome_item']}")
                    st.write(f"Disponibilidade: {item['qnt_emprestar']}")
                    st.write(f"Descrição: {item['descricao']}")

        else:
            st.write("Nenhum item disponível no momento.")
    else:
        st.error("Por favor, faça login para acessar os itens.")

# Chamada da função que mostra a página home
if __name__ == "__main__":
    run_home_page()
