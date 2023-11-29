# api_manager.py
import requests
from urllib.parse import quote
import json, os

# Configurações da API
BASE_URL = "https://rentup.up.railway.app"

def get_token():
    if os.path.exists('auth_user'):
        with open("auth_user", "r") as json_file:
            data = json.load(json_file)
            token = data["token"]
            return token

def check_status():
    if os.path.exists('auth_user'):
        return True
    else:
        return False
    

# Obtém uma lista de todos os itens disponíveis.
def get_all_items(token):
    endpoint = "/item/get-items"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    return response.json() if response.status_code == 200 else []

def get_item_by_name(token, nome_do_item):
    nome_do_item_codificado = quote(nome_do_item)  # Codifica o nome do item para a URL
    endpoint = f"/item/get-item-by-name?item={nome_do_item_codificado}"
    url = f"{BASE_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        print("URL da requisição:", response.json())
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Item com o nome {nome_do_item} não encontrado no estoque. Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Realiza um novo empréstimo de item.
def rent_item(token, user_email, item_name, rent_date, status="WAITING"):
    endpoint = "/rent/rent"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "user": user_email,
        "itens": item_name,
        "rentDate": rent_date,
        "status": status
    }
    response = requests.post(f"{BASE_URL}{endpoint}", json=data, headers=headers)
    return response.status_code == 201

# Realiza a devolução de um item emprestado.
def return_item(token, rent_id):
    endpoint = f"/rent/return?rent_id={rent_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}{endpoint}", headers=headers)
    return response.status_code == 200

# Recupera o histórico de empréstimos filtrado pelo nome do item.
def get_rent_history_by_item(token, item_name):
    endpoint = f"/rent/history-item?item={item_name}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    return response.json() if response.status_code == 200 else []

# Recupera o histórico de empréstimos filtrado pelo e-mail do usuário.
def get_rent_history_by_user(token, user_email):
    endpoint = f"/rent/history-user?user_email={user_email}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    return response.json() if response.status_code == 200 else []