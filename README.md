# Escáner de Red y Puertos para Termux y Kali Linux

Este es un script en **Python 3** diseñado para **escáner redes y detectar dispositivos conectados**. Además, permite **escanear los puertos abiertos** de los dispositivos detectados.

## Características

- Escanea la red local y muestra los dispositivos conectados con su **IP y nombre**.
- Escanea los **puertos abiertos** de los dispositivos detectados.
- Compatible con **Termux** y **Kali Linux**.

## Instalación

### Requisitos previos

Asegúrate de tener **Python 3** y las siguientes dependencias instaladas:

```sh
pkg update && pkg upgrade -y  # Para usuarios de Termux
apt update && apt upgrade -y  # Para usuarios de Kali Linux
pkg install python -y         # Instalar Python en Termux
apt install python3 -y        # Instalar Python en Kali Linux
pip install scapy netifaces
```

## Uso

### Clonar y ejecutar
Para clonar el repositorio y ejecutar el script, use los siguientes comandos:

```sh
git clone https://github.com/MR-PATO/MR-PATO-Scan_Red.git
cd MR-PATO-Scan_Red
python3 Scan_Red
```



Ejecuta el script con:

```sh
python3 Scan_Red
```

### Menú de opciones

1. **Escanear dispositivos conectados:** muestra la IP y el nombre de cada dispositivo detectado.
2. **Escanear puertos abiertos:** revisa los puertos abiertos de los dispositivos encontrados en la red.
3. **Salir:** finaliza el programa.

## Ejemplo de salida

```
███   ███  ██████            ██████     ██     ██████    █████
 ███ ███   ██  ██            ██  ██   ████    █ ███ █   ██   ██
 ███████   ██  ██            ██  ██  ██  ██     ██     ██   ██
 ███████   █████             █████   ██  ██     ██     ██   ██

1. Escanear dispositivos conectados
2. Escanear puertos abiertos
3. Salir
Seleccione una opción: 1

[+] Dispositivos detectados:
    192.168.1.50 - GalaxyA20
    192.168.1.100 - Laptop-PC
```

## Notas

- Este script requiere permisos de **root** en Kali Linux (`sudo python3 scanner.py`).
- En **Termux**, asegúrate de tener activados los permisos adecuados.

## Autor

Desarrollado por Sr.Pato
