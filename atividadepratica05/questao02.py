def eh_palindromo(texto):
    texto_limpo = ''
    for letra in texto:
        if letra.isalnum():
            texto_limpo += letra.lower()

    #invertido = texto_limpo[::-1]

    texto_invertido = ''
    for letra in texto_limpo:
        texto_invertido = letra + texto_invertido

    if texto_limpo == texto_invertido:
        return "Sim"
    else:
        return "Não"
    
texto = input("Digite um texto: ")
resultado = eh_palindromo(texto)
print(f"{texto} é um palindromo? {resultado}")
