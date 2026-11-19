# para leer un archivo primero definiremos la ruta del archivo
ruta_archivo = "../../../entrada-salida/ejemplo.txt" # le colocamos la variable ruta = y el archivo a leer este es para definir
with open(ruta_archivo,"r",encoding= "utf-8")as archivo: 
            contenido = archivo.read()   #como cambiamos el nobre leera archivo  
            print(contenido)  #imprimimos contenido                                    