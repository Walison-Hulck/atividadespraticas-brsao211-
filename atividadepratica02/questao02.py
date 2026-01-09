nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço unitario do produto: "))
desconto = 20 

valor_desconto = valor * (desconto / 100)
valor_final = valor - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço total: R$ {valor_final:.2f}")