# layout.py
import streamlit as st
from PIL import Image

# Renderiza o Header
def render_header(unique_key=""): # unique_key é usado para criar chaves únicas para cada página
    if 'current_page' in st.session_state:
        search_key = f"search_{st.session_state['current_page']}_{unique_key}"
    else:
        st.session_state['current_page'] = 'home'
        search_key = f"search_home_{unique_key}"

    header_col1, header_col2, header_col3, header_col4 = st.columns([1, 8, 1, 1]) 

    with header_col1:
        try:
            logo = Image.open('img/logo.png')
            st.image(logo, width=100)
        except Exception as e:
            st.error(f"Erro ao carregar logo: {e}")

    with header_col2:
        st.text_input("", placeholder="Procure por algo", key=search_key)

    with header_col3:
        if st.button("Conta"):
            st.session_state['current_page'] = 'conta'

    with header_col4:
        if st.button("Carrinho"):
            st.session_state['current_page'] = 'cart'
            st.experimental_rerun()

# Renderiza a Sidebar
def render_sidebar():
    nav_buttons = ['HOME', 'CATEGORIAS', 'DESTAQUES', 'SUPORTE', 'MINHA CONTA']
    for button in nav_buttons:
        if st.sidebar.button(button):
            st.session_state['current_page'] = button.lower()

# Redereiza o Footer
def render_footer():
    # Insere outra linha divisória
    st.markdown("---")  

    # Cria 3 colunas com subheader e botões
    spacer_left, col1, col2, col3, spacer_right = st.columns([1, 2, 2, 2, 1])
    with col1:
        st.subheader("Quem somos")
        st.button("Conheça a RentUp", key="conheca_rentup")
        st.button("Nossos produtos", key="nossos_produtos")
        st.button("Onde estamos", key="onde_estamos")

    with col2:
        st.subheader("Links")
        st.button("Novidades", key="novidades")
        st.button("Mais buscados", key="mais_buscados") 
        st.button("Fórum GARAgino", key="forum_garagino")

    with col3:
        st.subheader("Ajuda")
        st.button("Entre em contato", key="entre_em_contato")
        st.button("Reportar problema", key="reportar_problema")
        st.button("Suporte", key="suporte")

    # Insere uma linha divisória
    st.markdown("""---""") 
    footer_col1, footer_col2, footer_col3 = st.columns([6, 5, 5])
    with footer_col2:
        st.write("© 2023 by RentUp. All rights reserved.")