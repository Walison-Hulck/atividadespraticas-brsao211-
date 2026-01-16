import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        dados = resposta.json() ['results'] [0]

        nome = f"{dados['name']['first']}{dados['name']['last']}"
        
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail: {email}\nPais: {pais}"
    except requests.RequestException as e:
        return f"Erro ao obter usuario aleatorio: {e}"
    
usuario = obter_usuario_aleatorio()
print(usuario)