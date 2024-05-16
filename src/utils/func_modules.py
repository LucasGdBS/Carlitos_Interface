import requests


def fetch_funcionario():
    url = "http://localhost:8080/funcionarios/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []
        

def fetch_funcionario_by_nome(nome):
    url = f"http://localhost:8080/funcionarios/buscar-por-nome?nome={nome}" 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []

    except Exception:
        return []

def fetch_funcionario_by_cpf(cpf):
    url = f"http://localhost:8080/funcionarios/buscar-por-cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_funcionario(cpf, nome, salario):
    url = "http://localhost:8080/funcionarios/"
    data = {
        "cpf": cpf,
        "nome": nome,
        "salario": salario
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


def edit_funcionario_by_cpf(cpf, nome, salario):
    url = f"http://localhost:8080/funcionarios/editar-por-cpf/{cpf}"
    data = {
        "nome": nome,
        "salario": salario
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False

def delete_funcionario(cpf):
    url = f"http://localhost:8080/funcionarios/{cpf}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False