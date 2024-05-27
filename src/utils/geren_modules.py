import requests



def fetch_gerente():
    url = "http://localhost:8080/gerentes"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []



def fetch_gerente_by_nome(nome):
    url = f"http://localhost:8080/gerentes/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_gerente_by_cpf(cpf):
    url = f"http://localhost:8080/gerentes/buscar-por-cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []
    

def create_gerente(cpf):
    url = "http://localhost:8080/gerentes"
    data = {
        "cpf": cpf,
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return response.text
    except Exception:
        return False

def delete_gerente(cpf):
    url = f"http://localhost:8080/gerentes/{cpf}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False