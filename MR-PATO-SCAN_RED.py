import scapy.all as scapy
import socket
import os
import netifaces

AZUL = "\033[34m"
ROJO = "\033[31m"
VERDE = "\033[32m"
NARANJA = "\033[33m"
RESET = "\033[0m"

def obtener_ip_local():
    interfaces = netifaces.interfaces()
    for interfaz in interfaces:
        if netifaces.AF_INET in netifaces.ifaddresses(interfaz):
            ip_info = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]
            ip = ip_info["addr"]
            if ip.startswith(("192.168.", "10.", "172.")):
                return ip
    return None

def obtener_nombre(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Desconocido"

def escanear_red(ip):
    print(f"\n[+] Escaneando dispositivos en la red {ip}/24...\n")
    request = scapy.ARP(pdst=f"{ip}/24")
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    respuesta = scapy.srp(broadcast / request, timeout=2, verbose=False)[0]

    dispositivos = []
    for _, recibido in respuesta:
        ip_dispositivo = recibido.psrc
        nombre = obtener_nombre(ip_dispositivo)
        dispositivos.append({"ip": ip_dispositivo, "nombre": nombre})

    return dispositivos

def escanear_puertos(ip, nombre):
    for puerto in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex((ip, puerto)) == 0:
            print(f"{VERDE}{puerto} abierto ({ip}, {nombre}){RESET}")
        else:
            print(f"{ROJO}{puerto} cerrado ({ip}, {nombre}){RESET}")
        sock.close()

def menu():
    os.system("clear")
    print(f"""{NARANJA}
███   ███  ██████            ██████     ██     ██████    █████             █████     ████     ██     ██   ██           ██████   ███████  █████
 ███ ███   ██  ██            ██  ██   ████    █ ███ █   ██   ██           ██   ██   ██  ██   ████    ███  ██            ██  ██   ██   █   ██ ██
 ███████   ██  ██            ██  ██  ██  ██     ██     ██   ██           █        ██       ██  ██   ████ ██            ██  ██   ██ █     ██  ██
 ███████   █████             █████   ██  ██     ██     ██   ██  ██████    █████   ██       ██  ██   ██ ████  ██████    █████    ████     ██  ██
 ██ █ ██   ██ ██             ██      ██████     ██     ██   ██                ██  ██       ██████   ██  ███            ██ ██    ██ █     ██  ██
 ██   ██   ██  ██    ██      ██      ██  ██     ██     ██   ██           ██   ██   ██  ██  ██  ██   ██   ██            ██  ██   ██   █   ██ ██
 ██   ██  ████ ██    ██     ████     ██  ██    ████     █████             █████     ████   ██  ██   ██   ██           ████ ██  ███████  █████
                                                  
Versión: 1.4.0
Autor: MR.Pato
{RESET}
{AZUL}[1] Escanear dispositivos en la red (Scapy)
[2] Escanear puertos abiertos en dispositivos detectados
[3] Escanear puertos en una IP específica
[4] Salir{RESET}
""")

def main():
    ip_local = obtener_ip_local()
    if not ip_local:
        print("No se pudo determinar la IP local. Asegúrate de estar conectado a una red.")
        return

    dispositivos = []

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dispositivos = escanear_red(ip_local)
            if dispositivos:
                print("\n[+] Dispositivos detectados:")
                for d in dispositivos:
                    print(f"    {d['ip']} - {d['nombre']}")
            else:
                print("\n[-] No se encontraron dispositivos.")
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            if not dispositivos:
                print("\n[-] Primero debe escanear los dispositivos con la opción 1.")
            else:
                print("\n[+] Escaneando puertos abiertos y cerrados...\n")
                for d in dispositivos:
                    escanear_puertos(d["ip"], d["nombre"])
            input("\nPresione Enter para continuar...")

        elif opcion == "3":
            ip_objetivo = input("\nIngrese la IP que desea escanear: ")
            nombre_objetivo = obtener_nombre(ip_objetivo)
            print(f"\n[+] Escaneando puertos en {ip_objetivo} ({nombre_objetivo})...\n")
            escanear_puertos(ip_objetivo, nombre_objetivo)
            input("\nPresione Enter para continuar...")

        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\n[!] Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
