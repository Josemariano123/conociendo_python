# fase 3 empezaremos a la reactivacion del soporte vital
nivel_oxigeno = 15.5 # coloque el dato inicial para comenzar
print("Reactivacion del soporte vital")
print("=" *50)
while nivel_oxigeno < 100:  #coloque un ciclo while un mientras se ha menor a 100 l e inyectara oxigeno
    nivel_oxigeno = nivel_oxigeno + (nivel_oxigeno * 0.20) #esto va hacer para inyectar es una formula primero sera nivel oxigeno y despues inyectara *0.20
    print(f"nivel de oxigeno:{nivel_oxigeno:.1f}%...")
    print("=" *50)
print("oxigeno al 100% mision cumplida, excelente ingeniero Mariano")
print("=" *50)
input("\npresiona enter para salir ")
    