# mi fase uno: diagnostico del sistema
nombre_estacion = "Nexus" #primero registrare todos los datos cada uno con su variable
nivel_bateria = 85
nivel_oxigeno = 15.5
compuertas_selladas = True # ayudara a saber si es verdadero o falso
consumo_por_hora = 12 #hasta aqui fuero datos empezare hacer la operacion en la siguiente linea
horas_restantes = nivel_bateria / consumo_por_hora #para calcular la hora restante
print("=" *50) # de la siguiente linea hacia abajo mandare a imprimir en pantalla
print("diagnostico- estacion espacial nexus")
print("=" *50)
print(f"nombre de la estacion:{nombre_estacion}") # mandamos a llamar a la variable con los datos pertinentes
print(f"nivel de bateria:{nivel_bateria} unidades")
print(f"nivel de oxigeno:{nivel_oxigeno} unidades")
print(f"compuertas de zona segura selladas{'si' if compuertas_selladas else 'no'}") # aqui coloque un if y else para regresas si y no
print("=" *50)
print(f"consumo:{consumo_por_hora} unidades por hora")
print(f"hora de soporte vital restante:{horas_restantes:.2f} horas")
print("=" *50)
input("\npresiona enter para salir") #recordando con mis otros codigos es es para que la ventana de windos se mantenga  y podamamos visualizar lo que imprimira

