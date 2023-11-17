import streamlit as st
from layout import render_header, render_sidebar, render_footer

# Esta função pode ser movida para um arquivo separado se necessário
def show_item_request_page(item_data):
    # Cabeçalho do item
    st.header(item_data["nome"])


    st.write(f'Disponibilidade: {item_data["disponibilidade"]}')
    max_quantidade = int(item_data["disponibilidade"])
    # Seleção de quantidade
    quantidade = st.number_input("Quantidade", min_value=1, max_value=max_quantidade, value=1, step=1)
    
    if quantidade > max_quantidade:
        st.error("Quantidade solicitada maior que a quantidade disponível.")
    else:
        # Botões de ação
        col3, col4 = st.columns([1, 1])
        with col3:
            add_cart = st.button("Adicionar ao carrinho")
        with col4:
            rent = st.button("Solicitar")
        # Lógica para adicionar ao carrinho ou alugar
        if add_cart:
        # Adicionar informações do item ao carrinho
            cart_item = {
                'nome': item_data['nome'],
                'quantidade': quantidade,
                # ... adicione outras informações relevantes do item aqui
            }
            # Adiciona o item ao carrinho no estado da sessão
            st.session_state.cart.append(cart_item)
            st.success(f"{item_data['nome']} adicionado ao carrinho com sucesso!")
            # Redireciona para a página do carrinho
            st.session_state['current_page'] = 'cart'
            st.experimental_rerun()

        if rent:
            st.success("Solicitação de aluguel enviada!")
            # Implemente a lógica de aluguel aqui
    # Descrição do item
    st.subheader("Sobre o Equipamento")
    st.write(item_data["descricao"])