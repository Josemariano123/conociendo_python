#Escribe una función llamada calibrar_energia(temperatura, carga_actual). Las reglas del manual de crisis cuántica dictan:

#Si la temperatura es mayor a 80 grados, el pulso de energía debe ser exactamente la mitad de la carga_actual.
#Si la temperatura está entre 50 y 80 grados (inclusive), el pulso debe ser igual a la carga_actual multiplicada por 1.5.
#Si la temperatura es menor a 50, el pulso es 0 (no se requiere acción).
#¿Cuál es la energía exacta que tu función decide inyectar? Define la función y pruébala simulando que el núcleo está a 75 grados con una carga actual de 120 voltios
def calibrar_energia(temperatura,carga_actual): #definimos la funcion y el nobre seria calibrar energia
    """
    calibra ka energia segun la temperatura del nucleo:
    > 80ºc mitad de la carga
    50-80ºc carga * 1.5
    <50ºc 0"""
    if temperatura > 80: #use un if si la temperatura es mayo 80 grados devuelve el resultado
        return carga_actual / 2 #divide mi carga a a la mitad
    elif 50 <= temperatura <= 80: # este lo agregue si la temperatura esta entre 50 y 80 incluye ambos numeros
        return carga_actual * 1.5 # multiplica mi carga por 1.5
    else: # si no cumple ninguna de las codiciones
        return 0 
temperatura_nucleo = 75 # llame a la funcion y le entrgue los datos los que me pide el problema
carga = 120
energia_resultante = calibrar_energia( temperatura_nucleo,carga)
print("=" *50) # todo de esta linea hacia abajo la coloque para imprimir en pantalla esta mutiplica el signo = *50 para definir una linea
print("diagnostico del nucleo c.e.r.e.s")
print("=" *50)
print(f"temperatura del nucleo:{temperatura_nucleo}ºc")
print(f"carga actual:{carga} voltios")
print(f"energia a inyectar:{energia_resultante}voltios")
print("=" *50 )
print(F"\nRespuesta: la energia exacta es {energia_resultante} voltios")
input("\npresiona enter para salir...")