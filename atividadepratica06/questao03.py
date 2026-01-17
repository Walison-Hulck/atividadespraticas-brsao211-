import requests


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if 'erro' in dados:
            return "Cep inválido."
        
        logradouro = dados['logradouro']
        