function num_Par {
    param (
        [int]$num
    )

    if ($num % 2 -eq 0) {
        Write-Host "El número $num es par"
    }
    else {
        Write-Host "El número $num es impar"
    }
}

$des = "s"

while ($des -eq "s") {
    $num = Read-Host "Ingresa un número"
    num_Par $num

    $des = Read-Host "¿Deseas ingresar otro número? (s/n)"
}
