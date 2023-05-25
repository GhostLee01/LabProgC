import socket
import subprocess
import requests
import nmap
import base64

# Obtener la dirección IP local
def get_local_ip():
    try:
        # Crear un socket y conectarlo a un host externo
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "No se pudo obtener la IP local"

# Obtener la dirección IP pública utilizando ifconfig.me
def get_public_ip():
    try:
        response = requests.get("https://ifconfig.me/ip")
        public_ip = response.text.strip()
        return public_ip
    except requests.RequestException:
        return "No se pudo obtener la IP pública"

# Realizar un escaneo Nmap en una dirección IP o rango de IP
def nmap_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments="-sV")
    return scanner.scaninfo()

# Guardar los resultados en un archivo de texto y codificarlos con Base64
def save_results(filename, content, append=False):
    with open(filename, "a" if append else "w") as file:
        file.write(content)
    with open(filename, "r") as file:
        encoded_content = base64.b64encode(file.read().encode()).decode()
    with open(filename, "w") as file:
        file.write(encoded_content)

# Obtener la dirección IP local y pública
local_ip = get_local_ip()
public_ip = get_public_ip()

# Guardar los resultados en un archivo de texto
save_results("results.txt", f"Dirección IP local: {local_ip}\nDirección IP pública: {public_ip}\n")

# Escanear el segmento de red privado
private_network = local_ip.split(".")[:-1]  # Eliminar el último octeto
private_network.append("0/24")  # Agregar la notación CIDR
private_network = ".".join(private_network)

# Realizar el escaneo Nmap en el segmento de red privado
scan_result_private = nmap_scan(private_network)

# Guardar los resultados en un archivo de texto
save_results("results.txt", f"{scan_result_private}\n", append=True)

# Escanear una IP específica o scanme.nmap.org
target_ip = "192.168.1.1"  # Puedes cambiarlo por otra IP

# Realizar el escaneo Nmap en la IP específica
scan_result_specific = nmap_scan(target_ip)

# Guardar los resultados en un archivo de texto
save_results("results.txt", f"{scan_result_specific}\n", append=True)

# Escanear la dirección IP pública
scan_result_public = nmap_scan(public_ip)

# Guardar los resultados en un archivo de texto
save_results("results.txt", f"{scan_result_public}\n", append=True)
