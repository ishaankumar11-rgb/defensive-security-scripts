import socket
import sys
from datetime import datetime

# Educational and Defensive tool to check local network ports
def scan_ports(target_host, ports_to_scan):
    print("-" * 50)
    print(f"Scanning Target: {target_host}")
    print(f"Time Started: {str(datetime.now())}")
    print("-" * 50)
    
    try:
        for port in ports_to_scan:
            # Setting up a standard socket for connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout so it doesn't hang
            
            # Attempting to connect to the port
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()
            
    except KeyboardInterrupt:
        print("\nExiting script.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()

if __name__ == "__main__":
    # Standard local loopback for safe and legal testing
    target = "127.0.0.1" 
    ports = [21, 22, 80, 443, 8080]
    scan_ports(target, ports)
