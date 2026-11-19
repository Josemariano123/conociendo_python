#leer un numero desde el archivo 
with open("entrada-salida/ejemplo.txt", "r", encoding="utf-8") as archivo:#esta linea es para abrir el archivo y leer
    numero = (archivo.read().strip())#obtendriamos su contenido strip elimina espacio y saltos
    print("el numero es", numero)
    input("presiona enter para cerrar...")#es para cerrar el archivo