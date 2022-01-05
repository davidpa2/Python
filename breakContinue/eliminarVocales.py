palabraSinVocal = ""

palabra = input("Escribe una palabra\n")
palabra = palabra.upper();


for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    
    palabraSinVocal = palabraSinVocal + letra


print(palabraSinVocal)

'''
Tu programa debe:

Pedir al usuario que ingrese una palabra.
Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de 
la palabra ingresada.
Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.
'''