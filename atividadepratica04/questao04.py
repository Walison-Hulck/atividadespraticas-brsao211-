pares = 0
impares = 0

while True:
    try:
        entrada = input("Digite um numero ou 'fim para sair: ")
        
        if entrada.lower() == 'fim':
            break
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par")
            pares += 1

        else:
             print(f"{numero} é impar")
             impares += 1
             
    except ValueError:
        print("Voce deve digitar apenas numeros")

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")



