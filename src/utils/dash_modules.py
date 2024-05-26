import requests




# * FATURAMENTO
def faturamento_diario():
    url = 'http://localhost:8080/dashboard/faturamento-diario'
    response = requests.get(url)
    return response.json()


def faturamento_mensal():
    url = 'http://localhost:8080/dashboard/faturamento-mensal'
    response = requests.get(url)
    return response.json()


def faturamento_anual():
    url = 'http://localhost:8080/dashboard/faturamento-anual'
    response = requests.get(url)
    return response.json()



# * CLIENTES
def clientes_bairro():
    url = 'http://localhost:8080/dashboard/clientes-por-bairro'
    response = requests.get(url)
    return response.json()


def forma_pagamento():
    url = 'http://localhost:8080/dashboard/forma-pagamento-mais-utilizadas'
    response = requests.get(url)
    return response.json()



# * PEDIDOS E VENDAS
def produtos_vendidos():
    url = 'http://localhost:8080/dashboard/produtos-mais-vendidos'
    response = requests.get(url)
    return response.json()


def pedidos_por_turno():
    url = 'http://localhost:8080/dashboard/pedidos-por-turno'
    response = requests.get(url)
    return response.json()



# * INGREDIENTES E PRODUTOS
def produtos_3ingredientes():
    url = 'http://localhost:8080/dashboard/produtos-com-mais-de-tres-ingredientes'
    response = requests.get(url)
    return response.json()


def ingredientes_vencimento():
    url = 'http://localhost:8080/dashboard/ingredientes-proximos-vencimento'
    response = requests.get(url)
    return response.json()


def ingredientes_mais_utilizados():
    url = 'http://localhost:8080/dashboard/ingredientes-mais-utilizados'
    response = requests.get(url)
    return response.json()



# * FUNCIONARIOS
def atendentes_mais_vendas():
    url = 'http://localhost:8080/dashboard/atendentes-com-mais-vendas'
    response = requests.get(url)
    return response.json()


def funcionarios_salario_media():
    url = 'http://localhost:8080/dashboard/funcionarios-salarios-acima-media'
    response = requests.get(url)
    return response.json()






