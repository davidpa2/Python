def isYearLeap(year):
    if year % 4 != 0 :
        return False;
    elif year % 100 != 0 :
        return True;
    elif year % 400 != 0 :
        return False;
    else :
        return True;

def daysInMonth(year, month):
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31;
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30;
        
    if month == 2 and isYearLeap(year):
        return 29
    else:
        return 28

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

'''
Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de d
ías del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen 
sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.1.3.6). Puede ser muy 
útil. Te recomendamos que utilices una lista con los meses. Puedea crearla dentro de la función; este truco 
acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
'''