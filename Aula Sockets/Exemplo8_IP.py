import socket #pip install socket

hostname = socket.gethostname()
ip_local = socket.gethostbyaddr(hostname)

print(f"Nome do host: {hostname}")
print(F"Endereço: {ip_local}")