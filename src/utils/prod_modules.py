import requests

def fetch_produto():
    url = "http://localhost:8080/produtos/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_by_id(id):
    url = f"http://localhost:8080/produtos/buscar-por-id?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []

def fetch_by_nome(nome):
    url = f"http://localhost:8080/produtos/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def delete_produto(id):
    url = f"http://localhost:8080/produtos/{id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def fetch_ingredientes_produto(id):
    url = f"http://localhost:8080/produtos/buscar-ingredientes-produto?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []