import base64
import os

#  Se crea una carpeta para guardar los archivos resultantes
carpeta_resultados = "resultados"
os.mkdir(carpeta_resultados)

# Decodifica y guarda la primera imagen
with open("imagen_codificada.txt", "r") as archivo1:
    imagen1_codificada = archivo1.read()

datos_imagen1 = base64.b64decode(imagen1_codificada)
ruta_imagen1 = os.path.join(carpeta_resultados, "imagen_decodificada.jpg")
with open(ruta_imagen1, "wb") as archivo_imagen1:
    archivo_imagen1.write(datos_imagen1)

# Decodifica y guarda la segunda imagen
with open("imagen_codificada2.txt", "r") as archivo2:
    imagen2_codificada = archivo2.read()

datos_imagen2 = base64.b64decode(imagen2_codificada)
ruta_imagen2 = os.path.join(carpeta_resultados, "imagen_decodificada2.jpg")
with open(ruta_imagen2, "wb") as archivo_imagen2:
    archivo_imagen2.write(datos_imagen2)


# Aquí hace el proceso para el archivo .cpp

with open("Hola_Mundo.cpp", "r") as archivo:
    contenido_cpp = archivo.read()

# Codifica el contenido del archivo en Base64
contenido_codificado = base64.b64encode(contenido_cpp.encode("utf-8")).decode("utf-8")

ruta_cpp_codificado = os.path.join(carpeta_resultados, "archivo_codificado.txt")
# Guarda la codificación en un archivo de texto
with open(ruta_cpp_codificado, "w") as archivo_codificado:
    archivo_codificado.write(contenido_codificado)
