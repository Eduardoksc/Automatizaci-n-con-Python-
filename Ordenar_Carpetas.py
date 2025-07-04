import os
import shutil

# 1 - Crear una carpeta por cada tipo de archivos 

ruta = "C:/Users/kike/Downloads"

# 2 - Crear de destino si no existen 

tipos= ["Archivos Excel", "PDF", "Imagenes", "Programas", ]

for carpeta in tipos:
    ruta_carpeta= os.path.join(ruta,carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# 3 Incluir loas archivos en las carpetas creadas 

for archivo in os.listdir(ruta):
    if archivo.endswith(".jpeg") or archivo.endswith(".png")  or archivo.endswith(".gif")or archivo.endswith(".PNG"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"Imagenes",archivo))

    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"PDF",archivo))

    elif archivo.endswith(".exe"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"Programas",archivo))

    elif archivo.endswith(".xlsx"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"Archivos Excel",archivo))