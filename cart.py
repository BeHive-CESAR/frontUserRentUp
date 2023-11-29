import time
import streamlit as st
import api_manager
from datetime import date, datetime, timedelta

def show_cart_page():
    token = api_manager.get_token()
    
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
        st.subheader("Finalizar Solicitação")
        default_return_date = date.today() + timedelta(days=1)
        return_date = st.date_input("Insira a data de devolução", min_value=default_return_date, value=default_return_date)

        if st.button("Fazer Solicitação"):
            if api_manager.check_status:
                all_rent_successful = True
                return_datetime = datetime.combine(return_date, datetime.min.time())  # Combina a data com o horário mínimo (00:00:00)
                rent_date = return_datetime.isoformat() + "Z"  # Adiciona 'Z' para indicar UTC

                for item in cart_items:
                    for _ in range(item['quantidade']):
                        rent_successful = api_manager.rent_item(
                            token= token,
                            user_email="userteste@cesar.school",  # Substituir pelo e-mail do usuário logado
                            item_name=item['nome'],
                            rent_date=rent_date,
                            status="WAITING"
                        )
                        if not rent_successful:
                            st.error(f"Não foi possível realizar o empréstimo do item '{item['nome']}'.")
                            all_rent_successful = False
                            break
                    if not all_rent_successful:
                        break

                if all_rent_successful:
                    # Limpa o carrinho após o sucesso
                    st.session_state.cart = []
                    st.success("Empréstimo finalizado com sucesso!")
                    st.session_state['current_page'] = 'home'
                    time.sleep(3)
                    st.rerun()
            else:
                st.error("Você precisa estar logado para finalizar o empréstimo.")
    else:
        st.write("Seu carrinho está vazio.")

if __name__ == "__main__":
    show_cart_page()
