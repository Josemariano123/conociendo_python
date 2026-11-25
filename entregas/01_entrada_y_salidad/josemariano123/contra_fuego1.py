#fase 1 contra fuego bateria actual (85)
#oxigeno actual (empieza 15.5)
#¿cuantas horas de soporte vital quedan?
numero = [12,45,88,103,50,77,92,10] #Datos del sistema
suma = 0 #coloque la variable suma  = 0 para cargar el resultado
print("=" *50) #esto hara una simulacion de una linea
print("calculo de contraseña")
for num in numero :
    if num >40 and num % 2 == 0: # aqui compara remos resultado 
        print(f"Numero {num} valido")
        suma = suma + num # hacemos la suma
    else:
        print(f"numero {num} dscartado")
print("=" *50)
print(f"contraseña final: {suma}")
print("=" *50)
input("\npresiona enter para salir...")