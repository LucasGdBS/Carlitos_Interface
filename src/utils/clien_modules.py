import requests


def fetch_cliente():
    url = "http://localhost:8080/cliente/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []
    

def fetch_cliente_by_nome(nome):
    url = f"http://localhost:8080/cliente/buscar-por-nome?nome={nome}" 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []

    except Exception:
        return []


def fetch_cliente_by_telefone(tel):
    url = f"http://localhost:8080/cliente/buscar-por-telefone?phone={tel}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_cliente(nome, telefone_1, telefone_2, complemento, rua, bairro, numero, cep):
    url = "http://localhost:8080/cliente/"
    data = {
        "nome": nome,
        "telefone_1": telefone_1,
        "telefone_2": telefone_2,
        "complemento": complemento,
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "cep": cep
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


def edit_cliente(tel, nome, telefone_1, telefone_2, complemento, rua, bairro, numero, cep):
    url = f"http://localhost:8080/cliente/editar-por-telefone/{tel}"
    data = {
        "nome": nome,
        "telefone_1": telefone_1,
        "telefone_2": telefone_2,
        "complemento": complemento,
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "cep": cep
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def delete_cliente(id):
    url = f"http://localhost:8080/cliente/{id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False