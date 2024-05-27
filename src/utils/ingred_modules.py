import requests

def fetch_ingrediente():
    url = "http://localhost:8080/ingredientes/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_ingrediente_by_id(id):
    url = f"http://localhost:8080/ingredientes/buscar-por-id?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def fetch_ingrediente_by_nome(nome):
    url = f"http://localhost:8080/ingredientes/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_ingrediente(nome, dt_val, qntd, tipo):
    url = "http://localhost:8080/ingredientes/"
    data = {
        "nome": nome,
        "dtValidade": dt_val,
        "quantidade": qntd,
        "tipoAlimento": tipo
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return response.text
    except Exception:
        return False


def edit_ingrediente_by_id(id, nome, dt_val, qntd, cod, tipo):
    url = f"http://localhost:8080/ingredientes/editar-por-id/{id}"
    data = {
        "nome": nome,
        "dtValidade": dt_val,
        "quantidade": qntd,
        "codigo": cod,
        "tipoAlimento": tipo
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return response.text
    except Exception:
        return False


def delete_ingrediente(id):
    url = f"http://localhost:8080/ingredientes/{id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False