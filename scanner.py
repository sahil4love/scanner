#!/usr/bin/env python
import socket
import sys
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# --- COLORS ---
G = '\033[92m'  # Green
B = '\033[94m'  # Blue
R = '\033[91m'  # Red
W = '\033[0m'   # Reset
C = '\033[96m'  # Cyan

def print_sahiko_banner():
    banner = f"""{B}
    ███████╗ █████╗ ██╗  ██╗██╗██╗  ██╗ ██████╗ 
    ██╔════╝██╔══██╗██║  ██║██║██║ ██╔╝██╔═══██╗
    ███████╗███████║███████║██║█████╔╝ ██║   ██║
    ╚════██║██╔══██║██╔══██║██║██╔═██╗ ██║   ██║
    ███████║██║  ██║██║  ██║██║██║  ██╗╚██████╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ 
        >> {W}Port Scanner & Manner Grabber{B} <<{W}
    """
    print(banner)

def grab_manner(s):
    """Safely grabs the service banner/manner."""
    try:
        # A standard HTTP header request
        s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        data = s.recv(1024).decode(errors='ignore').strip()
        if data:
            # Return only the first line of the response
            return data.splitlines()[0]
        return "Connected (No Manner)"
    except:
        return "No Manner"

def scan_port(target_ip, port):
    """The task each worker thread will perform."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        
        # connect_ex returns 0 if successful
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            
            manner = grab_manner(s)
            print(f"{G}[+]{W} Port {C}{port:<5}{W} | {G}{service:<8}{W} | {B}{manner}{W}")
        
        s.close()
    except Exception:
        pass

def main():
    print_sahiko_banner()

    if len(sys.argv) < 2:
        print(f"{R}Usage:{W} python scanner.py <host> <start_port> <end_port>")
        return

    host = sys.argv[1]
    start_p = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end_p = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"{R}[!] Error: Could not resolve {host}{W}")
        return

    print(f"{C}Target IP:{W} {target_ip}")
    print(f"{C}Range    :{W} {start_p} - {end_p}")
    print("-" * 65)

    # THREAD POOL: This limits the number of threads to 100.
    # It reuses threads instead of creating new ones for every port.
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_p, end_p + 1):
            executor.submit(scan_port, target_ip, port)

    print("-" * 65)
    print(f"{G}Scan Completed.{W}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user.{W}")
        sys.exit()
