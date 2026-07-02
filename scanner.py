
import socket
import time
def display_header():
    print("=" * 40)
    print("      PYTHON PORT SCANNER")
    print("=" * 40)
display_header()
target = input("Target Host: ")
def display_target(target):
    print(f"Target Host: {target}")
display_target(target)
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
start_time=time.time()
count = 0
def scan_ports(target):
      global count
      for port in common_ports:
              sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              sock.settimeout(1)
              result = sock.connect_ex((target, port))
              if result == 0:
                service_name = services.get(port, "Unknown Service")
                print(f"✅Port {port} is open ({service_name})")
                count+=1
              else:
                print(f"❌Port {port} is closed")
      sock.close()
scan_ports(target)
print("=" * 40)
print("      SCAN COMPLETE")
print(f"Total Open Ports: {count}")
end_time=time.time()
time_taken=end_time-start_time
print(f"Time taken for scanning: {time_taken:.2f} seconds")
print("=" * 40)