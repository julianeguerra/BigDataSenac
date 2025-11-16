def contar_caractere(texto, caractere_procurado):
    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()
    
    contador = 0
    for caractere in texto:        
        if caractere == caractere_procurado:
            contador += 1
    return contador
            
frase = input('Insira o texto a ser analisado: ')
letra = input('Insira o caractere a ser contado: ')

contagem = contar_caractere(frase, letra)

print(f"A letra '{letra}' aparece {contagem} vez(es) em '{frase}'.")    
