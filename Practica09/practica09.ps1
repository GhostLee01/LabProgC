$regRipperPath = "Ruta al .exe de RegRipper3.0"

$registryFilePath = "ruta al registro de ntuser.dat"

$outputDirectory = "ruta donde se va a guardar"

# Comando para ejecutar RegRipper y analizar el registro de usuario
$regRipperCommand = "& '$regRipperPath' -r '$registryFilePath' -p all > '$outputDirectory\regripper_results.txt'"

# Ejecutar el comando de RegRipper
Invoke-Expression -Command $regRipperCommand