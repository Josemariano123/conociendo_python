#fase 1 contra fuego bateria actual (85)
#oxigeno actual (empieza 15.5)
#¿cuantas horas de soporte vital quedan?
numero = [12,45,88,103,50,77,92,10] #Datos del sistema
bateria = 85 #dato de bateria actual variable
oxigeno = 15.5 #horas
consumo_total = 0
for num in numero:  # usre un for para calcular  cuantas horas se consumen
 if num > 40 and num % 2 == 0: # uso un residuo para verificar si es par 
    consumo_total += num 
    print(f"numero de consunmidor:{num}horas") #use esta funcion para imprimir las horas y bueno encerre la varible num
    horas_restantes = oxigeno - consumo_total   #para calcular el resultadod de horas hice una resta entre oxigeno y consumo
    print ("_" *40) #desde esta parte todo va ser para imprimir en pantalla resultado
    print (F"bateria actual:{bateria}%")
    print (f"oxigeno inicial:{oxigeno}horas")
    print(f"total de horas consumidas:{consumo_total}")
    print(f"horas de soporte vital que quedan:{horas_restantes}")
    if horas_restantes <= 0: #aqui le coloque un condicional para que mande una alerta si se que da sin oxigeno
        print("alerta el oxigeno esta agotado")
        input("\npresiona enter para salir") # este lo coloque para que se mantenga imprimido en mi pantalla de windows 