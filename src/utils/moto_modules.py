import requests

def fetch_motoqueiro():
    url = "http://localhost:8080/motoqueiros/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def create_motoqueiro(cpf, cpf_gerente):
    url = "http://localhost:8080/motoqueiros/"
    data = {
        "cpf": cpf,
        "gerenteMotorqueiro_cpf": cpf_gerente,
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


def fetch_motoqueiro_by_nome(nome):
    url = f"http://localhost:8080/motoqueiros/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_motoqueiro_by_cpf(cpf):
    url = f"http://localhost:8080/motoqueiros/buscar-por-cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []

def delete_motoqueiro(cpf):
    url = f"http://localhost:8080/motoqueiros/{cpf}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def edit_motoqueiro_by_cpf(cpf, cpf_gerente):
    url = f"http://localhost:8080/motoqueiros/editar-por-cpf/{cpf}"
    data = {
        "gerenteMotorqueiro_cpf": cpf_gerente,
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False