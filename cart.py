# cart.py

import streamlit as st
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
        # Defina a data de devolução padrão para ser pelo menos um dia após a data atual
        default_return_date = date.today() + timedelta(days=1)
        return_date = st.date_input("Insira a data de devolução", 
                                    min_value=default_return_date, 
                                    value=default_return_date)  # Defina o valor padrão dentro do intervalo
        if st.button("Finalizar Empréstimo"):
            # Lógica para finalizar o empréstimo
            st.session_state.cart = []
            st.success("Empréstimo finalizado com sucesso!")
            # Redireciona para a página de confirmação ou outra página
            st.session_state['current_page'] = 'home'
            st.experimental_rerun()
    else:
        st.write("Seu carrinho está vazio.")

if __name__ == "__main__":
    show_cart_page()
