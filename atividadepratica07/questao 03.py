import csv 

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline = '', encoding = 'utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado")

nome_arquivo = input("Digite o nome do arquivo CSV: ")
ler_arquivo(nome_arquivo)