import streamlit as st
import api_manager

# Esta função pode ser movida para um arquivo separado se necessário
def show_item_request_page(item_data):
    token = api_manager.get_token()
    # Cabeçalho do item
    st.header(item_data["nome_item"])

    st.write(f'Disponibilidade: {item_data["qnt_emprestar"]}')
    max_quantidade = int(item_data["qnt_emprestar"])
    # Seleção de quantidade
    quantidade = st.number_input("Quantidade", min_value=1, max_value=max_quantidade, value=1, step=1)
    
    if quantidade > max_quantidade:
        st.error("Quantidade solicitada maior que a quantidade disponível.")
    else:
        # Botões de ação
        col3, col4 = st.columns([10, 1])
        with col3:
            add_cart = st.button("Adicionar a sacola")
        with col4:
            rent = st.button("Solicitar")
        
        # Lógica para adicionar ao carrinho
        if add_cart:
            # Adicionar informações do item ao carrinho
            cart_item = {
                'nome': item_data['nome_item'],
                'quantidade': quantidade,
            }
            # Adiciona o item ao carrinho no estado da sessão
            if 'cart' not in st.session_state:
                st.session_state.cart = []
            st.session_state.cart.append(cart_item)
            st.success(f"{item_data['nome_item']} adicionado ao carrinho com sucesso!")

        # Lógica para solicitar o aluguel do item
        if rent:
            if api_manager.check_status():
                rent_successful = api_manager.rent_item(
                    token=token,
                    user_email="email@example.com",  # por enquanto fica assim
                    item_name=item_data['nome_item'],
                    rent_date="2023-01-01T00:00:00Z",  # por enquanto fica assim
                    status="WAITING"
                )
                if rent_successful:
                    st.success("Solicitação de aluguel enviada!")
                else:
                    st.error("Falha ao solicitar o aluguel. Verifique suas permissões ou tente novamente mais tarde.")
            else:
                st.error("Você precisa estar logado para solicitar um aluguel.")

    # Descrição do item
    st.subheader("Sobre o Equipamento")
    st.write(item_data["descricao"])

if __name__ == "__main__":
    show_item_request_page({'nome': 'Item Exemplo', 'disponibilidade': 10, 'descricao': 'Descrição do Item Exemplo'})
