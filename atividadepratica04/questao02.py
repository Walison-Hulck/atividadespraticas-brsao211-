notas = []

while True:
    try:
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para sair: ")

        if entrada.lower() == 'fim':
            break

        nota = float(entrada)

        if nota < 0 or nota > 10:
            raise Exception()
        
        notas.append(nota)




    except ValueError:
        print("Voce deve digitar apenas números ")
    except Exception:
        print("Nota invalida")

    soma = 0 

    for nota in notas:1
        soma += nota

    media = soma / len(notas)

    print(f"Media final: {media:.2f} ")
