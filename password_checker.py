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

if __name__ == "__main__":
    main_entry()
