while True:
    try:

        numero01 = float(input("Digite o primeiro numero : "))
        numero02 = float(input("Digite o segundo numero: "))
        operacao = input("Digite a operacao (+, -, *, /): ")

        if operacao == "+":
            resultado = numero01 + numero02
        elif operacao == "-":
            resultado = numero01 - numero02

        elif operacao == "*":
            resultado = numero01 * numero02
    
        elif operacao == "/":
            resultado = numero01 / numero02
        else:
            raise Exception()
        print(f"O resultado é {resultado}")
        break
    except ValueError:
        print("Você deve digitar apenas números")
    except ZeroDivisionError:
        print("Não é possivel dividir por zero")
    except Exception:
        print("Operação inválida")
        
