import requests
from utils.ingred_modules import fetch_ingrediente_by_nome

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


def fetch_produto_by_id(id):
    url = f"http://localhost:8080/produtos/buscar-por-id?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def fetch_produto_by_nome(nome):
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
    url = f"http://localhost:8080/produtos/buscar-ingredientes-produto?id={id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_produto(nome, preco, nome_ingredientes):
    id_ingredientes = []
    for i in nome_ingredientes:
        ingrediente = fetch_ingrediente_by_nome(i)[0]["codigo"]
        id_ingredientes.append(ingrediente)


    url = "http://localhost:8080/produtos/"
    data = {
        "nome": nome,
        "preco": preco,
        "ingredientes": id_ingredientes
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return response.text
    except Exception:
        return False


def edit_produto(id, nome, preco):
    url = f"http://localhost:8080/produtos/editar-por-id/{id}"
    data = {
        "nome": nome,
        "preco": preco
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return response.text
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


def get_ingredientes(ingredientes):
    ingredientes_list = []
    for ingrediente in ingredientes:
        ingredientes_list.append(ingrediente["nome"])
    return ingredientes_list
   