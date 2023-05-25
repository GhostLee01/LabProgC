from ftplib import FTP
import os

def descargar_archivo(ftp, archivo, directorio_destino):
    ruta_local = os.path.join(directorio_destino, archivo)
    with open(ruta_local, 'wb') as archivo_local:
        ftp.retrbinary('RETR ' + archivo, archivo_local.write)

def buscar_archivos_texto(ftp, directorio_actual, directorio_destino):
    archivos = ftp.nlst(directorio_actual)
    for archivo in archivos:
        if ftp.nlst(archivo) == []:  # Verificar si es un archivo
            if archivo.lower().endswith('.txt'):  # Verificar si es un archivo de texto
                print("Descargando", archivo)
                descargar_archivo(ftp, archivo, directorio_destino)
        else:
            
            nuevo_directorio = os.path.join(directorio_actual, archivo)
            buscar_archivos_texto(ftp, nuevo_directorio, directorio_destino)

def conectar_ftp(servidor, usuario, contraseña, directorio_destino):
    ftp = FTP(servidor)
    ftp.login(usuario, contraseña)
    ftp.cwd('/')  # Directorio raíz del servidor FTP
    buscar_archivos_texto(ftp, '/', directorio_destino)
    ftp.quit()

servidor_ftp = 'nombre_del_servidor'
usuario_ftp = 'nombre_de_usuario_ftp'
contraseña_ftp = 'contraseña_ftp'

directorio_destino_local = 'ruta_a_la_carpeta_TXT'

conectar_ftp(servidor_ftp, usuario_ftp, contraseña_ftp, directorio_destino_local)
