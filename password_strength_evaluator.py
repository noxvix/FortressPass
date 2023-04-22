import re
import string
import enchant
import argparse

def password_strength(password):
    strength = 0
    length = len(password)
    d = enchant.Dict("en_US")

    if length >= 8:
        strength += 1

    if length >= 12:
        strength += 1

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength += 1

    if re.search(r"\d", password):
        strength += 1

    if re.search(r"[^\w\s]", password):
        strength += 1

    if not any(d.check(word) for word in re.findall(r"\w+", password)):
        strength += 1

    return strength

def display_strength(strength):
    print("Password strength:")
    if strength <= 2:
        print(r"""
  __        __
 /  \.-"""-./  \
 \    -   -    /
  |   o   o   |
  \  .-'"'-.  /
   '-\__Y__/-'
      `---`""")
        print("Weak password")
    elif strength == 3:
        print(r"""
     .-"      "-.
   /            \
  |              ;
  |              |           
  ;              :           
  \   -.        /           
   `-.   '-. .-'      _._  
      `:_     .-:/  /  _._\
        ||    /:|_|  /   o o\
        ||   / /|_|| /_/_|_/_/
       _|;._./ /  |;._.::._./
     /   .::./   ;   .::::./""")
        print("Moderate password")
    elif strength == 4:
        print(r"""
  .-=-.          .--.
 /  .  \        /_   |
| |\_|  |       |  \  \
 \  .  /        \  `"`
  `=-=´jgs       `""""")
        print("Good password")
    else:
        print(r"""
      /\_/\  
     / o o \ 
    (   "   ) 
     \~---~/ 
      \~_~_/""")
        print("Strong password")

def is_common_password(password):

def is_common_password(password):
    common_passwords = ['password', '123456', '123456789', 'qwerty', 'abc123']
    return password.lower() in common_passwords

def has_keyboard_pattern(password):
    keyboard_patterns = [
        r'(?i)(qwerty|asdfgh|zxcvbn)',
        r'(?i)(0987654321|1234567890)'
    ]
    for pattern in keyboard_patterns:
        if re.search(pattern, password):
            return True
    return False

def has_consecutive_sequence(password):
    patterns = [
        r'(?i)(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
        r'(?i)(123|234|345|456|567|678|789|890)',
    ]
    for pattern in patterns:
        if re.search(pattern, password):
            return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Strength Evaluator")
        parser.add_argument("password", help="Password to analyze")
    args = parser.parse_args()

    strength = password_strength(args.password)
    display_strength(strength)

    if is_common_password(args.password):
        print("Warning: This is a common password.")
    
    if has_keyboard_pattern(args.password):
        print("Warning: This password contains a keyboard pattern.")

    if has_consecutive_sequence(args.password):
        print("Warning: This password contains a consecutive character sequence.")
