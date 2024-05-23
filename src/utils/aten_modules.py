import requests

def fetch_atendente():
    url = "http://localhost:8080/atendentes/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_atendente_by_nome(nome):
    url = f"http://localhost:8080/atendentes/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_atendente_by_cpf(cpf):
    url = f"http://localhost:8080/atendentes/buscar-por-cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_atendente_by_geren_cpf(cpf):
    url = f"http://localhost:8080/atendentes/buscar-por-gerente?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def create_atendente(cpf, turno, cpf_gerente):
    url = "http://localhost:8080/atendentes/"
    data = {
        "cpf": cpf,
        "turno": turno,
        "cpf_gerente": cpf_gerente
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False



def edit_atendente_by_cpf(cpf, turno):
    url = f"http://localhost:8080/atendentes/editar-por-cpf/{cpf}"
    data = {
        "turno": turno
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def delete_atendente(cpf):
    url = f"http://localhost:8080/atendentes/{cpf}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False