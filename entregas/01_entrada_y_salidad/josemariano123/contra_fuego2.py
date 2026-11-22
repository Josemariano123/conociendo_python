# Has extraído el siguiente registro de sensores:registro = ["ok", "error_404", "ok", "corrupto", "ok", "ok", "falla_critica", "ok"]
# Crea un algoritmo que recorra este registro. Si encuentra un dato válido (“ok”), debe contarlo. Si encuentra una falla o corrupción
#¿qué posición exacta ocurrió?
#¿Cuántos paquetes “ok” hay y en qué índices exactos están los errores?
registro =["ok", "error_404", "ok", "corrupto", "ok", "ok", "falla_critica", "ok"] # primero coloque los registro parapoder empezar
contador_ok = 0 # use una variable contador  y empezamos en cero para guardar resultados
error = [] # por si hay fallas lo deje vacio el corchete ya que es posible que no falle
for indice, estado in enumerate(registro): # enumerate meda la posicion y el valor de cada elemento
 if estado == "ok": #este es para comparar el estado con un ok
    contador_ok += 1
 else: #si no es ok guardo en que tipo esta el dato de error
        error.append(f"posicion{indice}:{estado}") #guarde el tipo de error y su posiccion exacta
       
print("=" *50 ) #de esta line hacia abajo mandare imprimir resultados
print("informe de estado del sistema ")
print("=" *50 ) # en este caso = dibuja 50 veces que semega a una linea
print(f"informe del estado de sistema")
print("=" *50 )
print(f"paquetes validos('ok'):{contador_ok}")
print(f"total de errores detectados:{len(error)}")
print("\nubicacion exacta de errores:")
for falla in error:
            print("=" *50 )
            input("\npresiona enter para salir")