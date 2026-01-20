import json

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding = 'utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado")

def escrever_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding = 'utf-8' ) as arquivo_json:
            json.dump(dados, arquivo_json, indent = 4, ensure_ascii = False)
        return f"Dados escritos com sucesso no arquivo {nome_arquivo}"
    except Exception as e:
        return f"Erro ao escrever no arquivo: {e}"
    
dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"

}
nome = input("Digite o nome do arquivo JSON: ")
print(escrever_arquivo(nome, dados))
print(ler_arquivo(nome))