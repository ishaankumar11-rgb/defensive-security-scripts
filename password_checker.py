import re
import sys

def check_password_strength(password):
    """Analyze password strength based on standard security baseline rules."""
    strength = 0
    remarks = ""
    
    # Check length criteria
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1
        
    # Check for character diversity
    if re.search(r"[A-Z]", password): # Uppercase
        strength += 1
    if re.search(r"[a-z]", password): # Lowercase
        strength += 1
    if re.search(r"[0-9]", password): # Digits
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): # Special characters
        strength += 1

    # Determine final remarks
    if strength <= 2:
        remarks = "WEAK - Highly vulnerable to brute-force attacks!"
    elif strength <= 4:
        remarks = "MEDIUM - Consider adding more character variety."
    else:
        remarks = "STRONG - Excellent cryptographic entropy!"
        
    return strength, remarks

def main_entry():
    print("-" * 50)
    print("Defensive Tool: Password Strength Analyzer")
    print("-" * 50)
    
    # Safe fallback input simulation for automation testing
    sample_pass = "Secure@123_Pass"
    score, msg = check_password_strength(sample_pass)
    
    print(f"Testing Password: {sample_pass}")
    print(f"Entropy Score   : {score}/6")
    print(f"Security Alert  : {msg}")
    print("-" * 50)

def main_entry():
    print("-" * 50)
    print("Defensive Tool: Dynamic Password Strength Analyzer")
    print("-" * 50)
    
    try:
        # टर्मिनल से लाइव यूजर इनपुट लेने के लिए input() का उपयोग
        if sys.version_info < 3:
            user_pass = raw_input("Enter password to analyze: ")
        else:
            user_pass = input("Enter password to analyze: ")
            
        if not user_pass:
            print("[!] Error: Password cannot be empty.")
            return

        score, msg = check_password_strength(user_pass)
        
        print("\n[+] Audit Results:")
        print(f"Entropy Score   : {score}/6")
        print(f"Security Alert  : {msg}")
        print("-" * 50)
        
    except KeyboardInterrupt:
        print("\n\nExiting tool.")
        sys.exit()

