# CarlitosDB ERP Interface

Esta interface foi desenvolvida para aprimorar a experiência do usuário com o [sistema CarlitosDB ERP](https://github.com/LucasGdBS/BD-Carlitos), facilitando a visualização e manipulação de dados.

## 💿 Instalação

Para proceder com a instalação, é necessário ter o Python 3.10 ou superior instalado em sua máquina. Caso não tenha, você pode baixá-lo [aqui](https://www.python.org/downloads/).

Após instalar o Python, você pode clonar este repositório em sua máquina com o seguinte comando:

```bash
git clone https://github.com/LucasGdBS/Carlitos_Interface.git
```

Em seguida, acesse a pasta do repositório clonado e execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

## 🖥️ Utilização

Para utilizar a interface, basta estar na raiz do projeto e executar o arquivo app.py com o seguinte comando:

```bash
streamlit run .\src\app.py
```

Após executar o comando, uma janela do navegador será aberta com a interface do CarlitosDB ERP.

> ⚠️ **Observação:**: A interface foi pensada para ser utilizada com a API do [sistema CarlitosDB ERP](https://github.com/LucasGdBS/BD-Carlitos) rodando localmente. Então é necessario que o sistema esteja rodando em sua máquina para que a interface funcione corretamente.
