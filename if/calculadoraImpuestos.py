ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso < 85528 :
    impuesto = (ingreso * 0.18) - 556.2
else :
    impuesto = 14839.2 + (85528 * 0.32)
    
if impuesto < 0 :
    impuesto = 0
    
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

'''
Érase una vez una tierra - una tierra de leche y miel, habitada por gente feliz y próspera. 
La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El impuesto más importante, 
denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó 
utilizando la siguiente regla:
Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos 
y 2 centavos (esta fue la llamada exención fiscal ).
Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del 
excedente sobre 85,528 pesos.
'''