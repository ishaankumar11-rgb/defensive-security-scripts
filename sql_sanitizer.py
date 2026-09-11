import re
import sys

def analyze_input(user_input):
    """Scan input for common SQL Injection signatures and patterns."""
    # Common regex patterns used to detect SQLi attempts
    sqli_patterns = [
        r"('|\"|;|\-\-|#)",                 # Dangerous symbols
        r"(?i)(UNION\s+SELECT)",            # UNION based extraction
        r"(?i)(SELECT\s+.*\s+FROM)",        # Standard queries
        r"(?i)(OR\s+\d+\s*=\s*\d+)",        # Tautology attacks (e.g., OR 1=1)
        r"(?i)(DROP\s+TABLE|INSERT\s+INTO)" # Destructive commands
    ]
    
    violations = 0
    detected_patterns = []
    
    for pattern in sqli_patterns:
        if re.search(pattern, user_input):
            violations += 1
            detected_patterns.append(pattern)
            
    if violations > 0:
        return False, f"CRITICAL: SQL Injection signature detected! (Matches: {violations})"
    return True, "SAFE: Input successfully validated."

def main_entry():
    print("-" * 50)
    print("Defensive Tool: SQL Injection Input Sanitizer")
    print("-" * 50)
    
    try:
        if sys.version_info.major < 3:
            user_data = raw_input("Enter data payload to sanitize: ")
        else:
            user_data = input("Enter data payload to sanitize: ")
            
        if not user_data:
            print("[!] Error: Input payload cannot be empty.")
            return

        is_safe, message = analyze_input(user_data)
        
        print("\n[+] Audit Results:")
        print(f"Status  : {'[PASS]' if is_safe else '[BLOCK]'}")
        print(f"Report  : {message}")
        print("-" * 50)
        
    except KeyboardInterrupt:
        print("\n\nExiting tool.")
        sys.exit()

if __name__ == "__main__":
    main_entry()
