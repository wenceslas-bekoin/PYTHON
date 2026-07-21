import socket

def scanner_port(ip, port):
    """Teste si un port est ouvert sur une machine"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultat = sock.connect_ex((ip, port))
    sock.close()
    if resultat == 0:
        return True
    return False

# Scanner plusieurs ports
ip_cible = "192.168.1.6"
print(f"Scan de {ip_cible} en cours...")

for numero_port in range(1, 1025):
    if scanner_port(ip_cible, numero_port):
        print(f"Port {numero_port} — OUVERT ")

print("Scan terminé !")