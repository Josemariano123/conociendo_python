#fase 2 de nexus se tomaran algunos datos de la fase  uno
nombre_estacion = "Nexus" #empezamos colocando los datos a ocupar
nivel_bateria = 85
compuertas_selladas = True # para comprobar si la compuerta esta sellada 
print("=" *50) #mandare a imprimir en pantalla
print("protocolo de seguridad")
print("=" *50)
print(f"Nivel de bateria:{nivel_bateria}")
print(f"compuertas selladas:{'si'  if compuertas_selladas else 'no'} ") #hacemos un if y else para de volver un resultado booleano
print("=" *50)
if nivel_bateria >= 20 and compuertas_selladas: #aqui coloco un if para comprobar si se cumple las dos condicciones
 print("protocolo de seguridad superado iniciandose secuencia")
else:
    print("Alerta roja: condiciones inestable abortando mision")
    print("=" *50)
input("\npresiona enter para salir")