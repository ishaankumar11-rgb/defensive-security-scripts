import hashlib
import os
import sys
import time

def calculate_sha256(filepath):
    """Calculate the SHA-256 hash of a file to check its integrity."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read file in chunks to handle large files smoothly
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def monitor_file(filepath, interval=5):
    """Monitor the specified file for any integrity changes."""
    print("-" * 60)
    print(f"Starting Integrity Monitor for: {filepath}")
    print(f"Checking every {interval} seconds. Press Ctrl+C to stop.")
    print("-" * 60)
    
    # Generate the initial baseline hash
    baseline_hash = calculate_sha256(filepath)
    if not baseline_hash:
        sys.exit()
        
    print(f"Initial Baseline Hash: {baseline_hash}\n")
    
    try:
        while True:
            time.sleep(interval)
            current_hash = calculate_sha256(filepath)
            
            if current_hash is None:
                print("[!] WARNING: File has been deleted or is inaccessible!")
                break
                
            # Compare current hash with baseline
            if current_hash != baseline_hash:
                print(f"[ALERT] {time.strftime('%Y-%m-%d %H:%M:%S')} - FILE INTEGRITY COMPROMISED!")
                print(f" New Hash: {current_hash}")
                print("-" * 60)
                # Update baseline to the new modified state to avoid constant alerts
                baseline_hash = current_hash
                
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit()

if __name__ == "__main__":
    # Create a temporary dummy file for safe and isolated local testing
    test_file = "test_integrity.txt"
    if not os.path.exists(test_file):
        with open(test_file, "w") as f:
            f.write("This is a secure baseline configuration statement.")
            
    monitor_file(test_file, interval=5)
