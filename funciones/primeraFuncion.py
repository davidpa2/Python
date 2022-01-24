def ingresarValor() :
    return int(input("Ingresa un valor: "))

print(ingresarValor())


def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Se pueden pasar los parámetros desordenados pero con el nombre
suma(c=3, a = 1, b = 2)


#Parámetros por defecto
def presentar(primerNombre, segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Jorge")


def strangeFunction(n):
    if(n % 2 == 0):
        return True
        
if strangeFunction(2):
    print("El número es par")
else:
    print("El número es impar")


# Pasarle un array como argumento
def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
    
print(sumaDeLista([5, 4, 3])) 


# Devolver un array
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))
