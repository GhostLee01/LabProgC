#!/bin/bash

num_Par() {
    num=$1
    if [ $((num % 2)) -eq 0 ]; then
        echo "El numero $num es par"
    else
        echo "El numero $num es impar"
    fi
}

des="s"

while [ "$des" = "s" ]; do
    read -p "Ingresa un numero: " num
    num_Par $num

    read -p "¿Deseas ingresar otro numero? (s/n): " des
done
