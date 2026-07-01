import socket
print("=" * 40)
print("      PYTHON PORT SCANNER")
print("=" * 40)
target = input("Enter the IP address:")
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((target,port))
    if result == 0:
      print(f"✅ Port {port} ({services.get(port,'Unknown')}) is OPEN")
    else:
        print(f"❌ Port {port} ({services.get(port,'Unknown')}) is CLOSED")
    sock.close()