


ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 ==0:
            print("Bissexto")
        else:
            print("Não é bissexto")
    else:
        print("Bissexto")            

else:
    print("Não é bissexto")


