idade = int(input("Digite a idade: "))
if idade < 0:
    print("Idade invalida")

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolecente")
elif idade <= 59:
    print("Adulto")
 
else:
    print("Idoso")
 