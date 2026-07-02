
import socket
import time
def display_header():
    print("=" * 40)
    print("      PYTHON PORT SCANNER")
    print("=" * 40)
display_header()
target = input("Target host:")
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
start_time=time.time()
count = 0
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result=sock.connect_ex((target,port))
    if result == 0:
      count+=1
      print(f"✅ Port {port} ({services.get(port,'Unknown')}) is OPEN")
    else:
        print(f"❌ Port {port} ({services.get(port,'Unknown')}) is CLOSED")
    sock.close()
print("=" * 40)
print("      SCAN COMPLETE")
print(f"Total Open Ports: {count}")
end_time=time.time()
time_taken=end_time-start_time
print(f"Time taken for scanning: {time_taken:.2f} seconds")
print("=" * 40)