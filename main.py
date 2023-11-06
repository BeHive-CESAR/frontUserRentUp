import streamlit as st
import json, os
from PIL import Image
import webbrowser

# FUNÇÃO DE LOGIN
# OBS¹: FUNÇÃO DE LOGIN SERÁ MODIFICADA PARA SER COMPATÍVEL COM A API, ESSA É SÓ PRA TESTAR !!! 
# OBS²: Pra logar como adm ou usuário

def login():
    st.warning('Adminstrador ou usuário: email = "email",  senha = "senha"')
    tipo = st.selectbox('Tipo de usuário', ('Administrador', 'Aluno/Professor'), index=1)

    #Se for administrador, redireciona para a outra aplicação
    if tipo == 'Administrador':
        st.write(f"Redirecionando para login de {tipo}...")
        webbrowser.open('https://rentup-adm.streamlit.app')

    #Se for administrador, pede pra preencher o forms de login
    else:
        with st.form("loginForms", True):
            email = st.text_input('Email')
            senha = st.text_input('Senha',  type="password")
            submitted = st.form_submit_button("Enviar")
            if submitted: #substituir pelo metodo de auth da API
                if email == 'email' and senha == 'senha':
                    data = {
                        "usuario": {
                            "email": email,
                            "senha": senha
                        }
                    }

                    # Cria um arquivo json para salvar os dados do usuário logado e salvar o status de "logado"
                    with open('auth_user.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                        st.rerun()

                    
                    return True
                else:
                    st.error('Credenciais inválidas')
                    return False

# Se o usuário já estiver logado, o forms de login não aparecerá
if os.path.exists('auth_user.json'):

    #Definindo a sidebar global da interface do adm
    with st.sidebar:
        #page = st.selectbox('Selecione uma página:', ('Inventário', 'Dashboard')) -> Substituir as páginas pelas as de usuário

        #Se o usuário deslogar, o arquivo json é removido e pede para fazer login novamente
        if st.button("Logout"):
            os.remove('auth_user.json')
            st.rerun()

    # Editar de acordo com as páginas disponíveis
    # if page == 'Dashboard':
    #     dashboard.dashboard()
    # elif page == 'Inventário':
    #     inventario.inventario()

# Enquanto o usuário não estiver logado, irá pedir para preencher o forms de  login
else:
    # HEADER DO SITE #
    logo_container = st.container()
    col1, col2, col3 = st.columns(3)

    with logo_container:
        with col2:
            image = Image.open('img/logo.png')
            st.image(image, width=150)
            
    login()