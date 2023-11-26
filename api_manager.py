# api_manager.py
import requests

# Configurações da API
BASE_URL = "https://rentup.up.railway.app"

# Autentica um usuário e retorna um token de acesso.
def login(email, password):
    endpoint = "/user/login"
    data = {"email": email, "password": password}
    try:
        # Modifique esta linha se a API esperar JSON
        response = requests.post(f"{BASE_URL}{endpoint}", json=data)  # Use json=data se a API esperar um JSON

        if response.status_code == 200:
            return response.json().get("token")
        else:
            # Imprime a resposta para ajudar na depuração
            print("Falha no login:", response.text)
            return None
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Obtém uma lista de todos os itens disponíveis.
def get_all_items(token):
    endpoint = "/itens/all"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    return response.json() if response.status_code == 200 else []

# Busca um item específico pelo nome.
# Busca itens pelo nome
def get_item_by_name(token, search_term):
    endpoint = f"/itens/search?name={search_term}"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        if response.status_code == 200:
            return response.json()  # Supondo que a API retorna uma lista de itens
        else:
            # Imprime a resposta para ajudar na depuração
            print("Erro ao buscar itens:", response.text)
            return []
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return []

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