#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Es necesario la ruta relativa con TXT"
    exit 1
fi

# Ruta relativa del archivo de texto que contiene las direcciones de correo electrónico
archivo="$1"

# Comprobar si el archivo existe y contiene direcciones de correo válidas
if [ -f "$archivo" ]; then
    while IFS= read -r linea; do
        # Verificar si la línea contiene una dirección de correo válida
        if [[ "$linea" =~ ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$ ]]; then
            # Configuración del correo electrónico
            rem="tucorreo@example.com"
            asunto="Asunto del correo"
            mensaje="Cuerpo del correo"

            # Enviar correo electrónico
            dest="$linea"
            echo "Enviando correo a: $dest"
            echo "$mensaje" | mail -s "$asunto" -r "$rem" "$dest"
        fi
    done < "$archivo"
else
    echo "El archivo ($archivo) no existe."
    exit 1
fi
