import streamlit as st
import api_manager
import json, os
from PIL import Image
import requests

# Configuração inicial da página
st.set_page_config(page_title='Rent Up', layout='wide')

# Importações dos módulos das páginas
from home import run_home_page
from categorias import mostrar_pagina_categorias
from item_request import show_item_request_page  
from cart import show_cart_page
from layout import render_header, render_sidebar, render_footer
from search_results import show_search_results

# Inicialização do estado da sessão
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'

def login(): # FUNÇÃO DE LOGIN
    
    with open('style.css') as file: #Importando arquivo css
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

    logo_container = st.container() # LOGO #
    with logo_container: 
        logo_cols = st.columns([1,1,1])
        with logo_cols[1]:
            image = Image.open('img/logo.png')
            st.image(image, width=150)
    
    st.header('Login', divider='orange')
    
    tipo = st.selectbox('Tipo de usuário', ('Aluno ou Professor', 'Administrador'))
    if tipo == 'Administrador':
        st.link_button("Fazer login como Administrador", "https://rentup-adm.streamlit.app")
    
    else:
        with st.form("loginForms", True):  #Forms de login#
            email = st.text_input('Email')    
            senha = st.text_input('Senha',  type="password")

            login_cols = st.columns([5,2.5,1])    
            with login_cols[2]:
                submitted = st.form_submit_button("Enviar")

            if submitted: 
                
                data = {
                    "email": email,
                    "password": senha
                }

                response = requests.post("https://rentup.up.railway.app/user/login", json=data)
                error_mesage = response.json().get('detail')
                
                #Tratamento de erros
                if response.status_code == 200: #Se o usuário for logado com sucesso 
                    output = response.json()
                    with open("auth_user", "w") as json_file: #Escrevendo os dados do usuário em um json
                        json.dump(output, json_file)

                    
                    with open("auth_user", "r") as json_file: #Verificando se o tipo inserido condiz com o banco de dados 
                        output = json.load(json_file)  

                    user_tipe = output['access']

                    if user_tipe != "USER":
                        os.remove('auth_user')
                        st.error("Tipo de usuário informado não condiz com o nosso sistema")
                    else:
                        st.rerun()
                        
                else:
                    st.error(error_mesage)

        cancel_cols = st.columns([6, 1])                
        with cancel_cols[1]:
            if st.button("Cadastro", type='secondary'):
                st.session_state.cadastro = True
                st.rerun()


def cadastro(): #Função de cadastro
    with open('style.css') as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)
        
    
    logo_container = st.container() # LOGO #
    with logo_container: 
        logo_cols = st.columns([1,1,1])
        with logo_cols[1]:
            image = Image.open('img/logo.png')
            st.image(image, width=150)

    st.header('Cadastro', divider='orange')
    
    with st.form("RegisterForms", False): #Se for administrador, pede pra preencher o forms de login
        email = st.text_input('Email')    
        contato = st.text_input('Número') 
        nome = st.text_input('Nome')  
        password = st.text_input('Senha',  type="password")
        st.caption('A senha deve conter uma letra maiúscula e um caractere especial') 
       
        cols = st.columns([5.5,1,0.8])        
        
        with cols[1]:    
            if st.form_submit_button("Cancelar"):
                st.session_state.cadastro = False
                st.rerun()
    
        with cols[2]:
            submitted = st.form_submit_button("Enviar")   

        if submitted: #Lançar os dados pra api autenticar
            url = 'https://rentup.up.railway.app/user/register'

            data = {
                "email": email,
                "password": password,
                "nome": nome,
                "contato": contato,
                "cargo": "USER",
            }
               
            response = requests.post(url, json=data) #Tratamnento de erros#
            error_mesage = response.json().get('detail')
            
            if response.status_code == 201: #Se o usuário for logado com sucesso 
                st.session_state.cadastro = False
                #st.error(error_mesage)
            elif response.status_code == 400:
                st.error(error_mesage)
            elif response.status_code == 409:
                st.error(error_mesage)
            else:
                st.error(error_mesage)
                    

if 'cadastro' not in st.session_state:
    st.session_state.cadastro = False

# Função para controle da navegação das páginas
def navigation_control():
    token = api_manager.get_token()
    # As páginas são controladas pelo estado da sessão 'current_page'
    if st.session_state['current_page'] == 'home':
        run_home_page()
    elif st.session_state['current_page'] == 'item_request':
        item_data = st.session_state.get('current_item', None)
        if item_data:
            show_item_request_page(item_data)
        else:
            st.error("Erro: Dados do item não encontrados.")
    elif st.session_state['current_page'] == 'cart':
        show_cart_page()
    elif st.session_state['current_page'] == 'search_results':
        search_term = st.session_state.get('search_term', '')
        if api_manager.check_status():
            show_search_results(search_term, token)
        else:
            st.error("Por favor, faça login para buscar itens.")
    elif st.session_state['current_page'] == 'logout':
            st.session_state['current_page'] = 'home'
            os.remove('auth_user')
            st.rerun()
            
            
# Função principal para executar o aplicativo
def main():
    render_header("main")
    render_sidebar()
    navigation_control()
    #render_footer()

# Ponto de entrada do script
if __name__ == "__main__":
    if api_manager.check_status():
        main()
    else:
        if st.session_state.cadastro == False:
            login()  
        else:
            cadastro()
        
