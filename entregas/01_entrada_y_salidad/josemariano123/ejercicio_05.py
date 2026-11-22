nombre_archivo = "gasto.txt"#definimos el nombre de la variable
texto_a_guardar = "hola soy mariano"#colocamos el texto donde queremos guardar

with open(nombre_archivo, "w", encoding="utf-8") as archivo:#modo escritura
    archivo.write(texto_a_guardar)#escribimos el texto
    print("el archivo se guardó correctamente")#imprimimos confirmacion del archivo
