import streamlit as st
import api_manager
from datetime import date, timedelta

def show_cart_page():
    if 'cart' not in st.session_state:
        st.session_state.cart = []

    cart_items = st.session_state.cart
    if cart_items:
        st.subheader(f"Carrinho: {len(cart_items)} itens")
        for i, item in enumerate(cart_items):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.text(item['nome'])
            with col2:
                item['quantidade'] = st.number_input(f"Quantidade para {item['nome']}", min_value=1, value=item['quantidade'], key=f"qty_{i}")
            with col3:
                if st.button("Remover", key=f"remove_{i}"):
                    cart_items.pop(i)
                    st.experimental_rerun()

        # Seleção da data de devolução
        st.subheader("Finalizar Empréstimo")
        default_return_date = date.today() + timedelta(days=1)
        return_date = st.date_input("Insira a data de devolução", min_value=default_return_date, value=default_return_date)

        if st.button("Finalizar Empréstimo"):
            if 'auth_token' in st.session_state and st.session_state['auth_token']:
                for item in cart_items:
                    # Aqui você pode implementar a lógica para enviar cada item no carrinho para a API
                    rent_successful = api_manager.rent_item(
                        token=st.session_state['auth_token'],
                        user_email="email@example.com",  # Substitua pelo e-mail do usuário logado
                        item_name=item['nome'],
                        rent_date=return_date.isoformat(),
                        status="WAITING"
                    )
                    if not rent_successful:
                        st.error(f"Não foi possível realizar o empréstimo do item '{item['nome']}'.")
                        break
                else:
                    # Limpa o carrinho após o sucesso
                    st.session_state.cart = []
                    st.success("Empréstimo finalizado com sucesso!")
                    st.session_state['current_page'] = 'home'
                    st.experimental_rerun()
            else:
                st.error("Você precisa estar logado para finalizar o empréstimo.")
    else:
        st.write("Seu carrinho está vazio.")

if __name__ == "__main__":
    show_cart_page()
