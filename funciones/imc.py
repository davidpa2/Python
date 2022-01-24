def imc(peso, altura):
    if type(peso) != str and type(altura) != str:
        return peso / altura ** 2

    return "No se han introducido bien los datos"
    
print(imc(52.5, 1.65))
