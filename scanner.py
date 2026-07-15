
import socket
import time
from datetime import datetime

# -------------------------------
# HEADER
# -------------------------------
def display_header():
    print("=" * 50)
    print("        PYTHON VULNERABILITY SCANNER")
    print("=" * 50)


display_header()
print("Educational Purpose Only")
print("-" * 50)

target = input("Enter Target IP or Hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("❌ Invalid hostname or IP address.")
    exit()

# -------------------------------
# COMMON PORTS
# -------------------------------
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

common_ports = list(services.keys())

open_ports = []
vulnerabilities = []

start_time = time.time()

print(f"\nScanning Target: {target}\n")

# -------------------------------
# PORT SCANNER
# -------------------------------
for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        service = services.get(port, "Unknown")

        print(f"✅ Port {port} OPEN ({service})")
        open_ports.append((port, service))

        # -------------------------------
        # Banner Grabbing
        # -------------------------------
        try:
          if port == 80:
             sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

          banner = sock.recv(1024).decode(errors="ignore").strip()

          if banner:
              print(f"   Version/Banner: {banner[:100]}")
        except:
             pass

        # -------------------------------
        # Basic Vulnerability Checks
        # -------------------------------
        if port == 21:
            vulnerabilities.append(
                "FTP detected - Consider using SFTP instead."
            )

        elif port == 23:
            vulnerabilities.append(
                "Telnet detected - Use SSH instead."
            )

        elif port == 445:
            vulnerabilities.append(
                "SMB is exposed - Ensure proper firewall protection."
            )

        elif port == 3389:
            vulnerabilities.append(
                "RDP is exposed - Restrict access and use strong passwords."
            )

    sock.close()

# -------------------------------
# HTTP CHECK
# -------------------------------
open_port_numbers = [p[0] for p in open_ports]

if 80 in open_port_numbers and 443 not in open_port_numbers:
    vulnerabilities.append(
        "HTTP detected without HTTPS."
    )

# -------------------------------
# REPORT
# -------------------------------
end_time = time.time()
time_taken = end_time - start_time

print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)

print(f"Open Ports Found: {len(open_ports)}")
print(f"Time Taken: {time_taken:.2f} seconds")

print("\nPotential Vulnerabilities:")

if vulnerabilities:
    for v in vulnerabilities:
        print("⚠", v)
else:
    print("No obvious vulnerabilities detected.")

# -------------------------------
# SAVE REPORT
# -------------------------------
filename = "vulnerability_report.txt"

with open(filename, "w") as report:

    report.write("=" * 60 + "\n")
    report.write("VULNERABILITY SCAN REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Target : {target}\n")
    report.write(f"Date   : {datetime.now()}\n")
    report.write(f"Time Taken : {time_taken:.2f} seconds\n\n")

    report.write("OPEN PORTS\n")
    report.write("-" * 30 + "\n")

    if open_ports:
        for port, service in open_ports:
            report.write(f"{port} - {service}\n")
    else:
        report.write("No open ports found.\n")

    report.write("\n")

    report.write("POTENTIAL VULNERABILITIES\n")
    report.write("\nVERSION DETECTION\n")
    report.write("-" * 30 + "\n")
    report.write("Banner grabbing attempted on detected services.\n")
    report.write("Software version depends on whether the service exposes its banner.\n\n")

    if vulnerabilities:
        for item in vulnerabilities:
            report.write(f"- {item}\n")
    else:
        report.write("No obvious vulnerabilities detected.\n")

    report.write("\n")

    report.write("RECOMMENDATIONS\n")
    report.write("-" * 30 + "\n")
    report.write("- Close unnecessary ports.\n")
    report.write("- Disable insecure services like FTP and Telnet.\n")
    report.write("- Use HTTPS instead of HTTP whenever possible.\n")
    report.write("- Keep software updated with the latest security patches.\n")
    report.write("- Restrict access to sensitive services.\n")
    report.write("- Regularly scan your systems.\n")
    report.write("- Remove unused services.\n")
    report.write("- Update outdated software versions.\n")
print("\nScan completed successfully.")
print(f"Report saved as '{filename}'")