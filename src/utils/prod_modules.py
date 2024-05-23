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


def fetch_produto_ingredientes(id):
    url = "http://localhost:8080/produtos/buscar-ingredientes-produto?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_produto(nome, preco):
    url = "http://localhost:8080/produtos/"
    data = {
        "nome": nome,
        "preco": preco,
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


def edit_produto(id, nome, preco):
    url = f"http://localhost:8080/produtos/editar-por-id/{id}"
    data = {
        "nome": nome,
        "preco": preco,
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


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


