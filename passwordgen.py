import random
import string

def password_generator(strength=None):
    # letters, numbers, and symbols used to generate password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = ['!','@','#','$','^','&','*','(',')','-','+','=','<','>','?']
    password_chars = []
    password = None
    # prompts for input and displays options if no strength level is chosen
    if strength is None:
        strength = input("How strong does your password need to be?\nWeak (8 characters & no symbols) | Strong (16 characters w/ symbols): ")

    if strength.lower() == "weak":
        length = 8
        # generates 6 random letters & 2 random numbers
        for i in range(3):
            password_chars.append(random.choice(lowercase))
        for i in range(3):
            password_chars.append(random.choice(uppercase))
        for i in range(2):
            password_chars.append(random.choice(digits))
        # converts list of password characters to string
        random.shuffle(password_chars)
        password = "".join(password_chars)
    
    elif strength.lower() == "strong":
        length = 16
        # generates 10 random letters, 4 random numbers, & 2 random digits
        for i in range(5):
            password_chars.append(random.choice(lowercase))
        for i in range(5):
            password_chars.append(random.choice(uppercase))
        for i in range(4):
            password_chars.append(random.choice(digits))
        for i in range(2):
            password_chars.append(random.choice(symbols))
        # converts list of password characters to string
        random.shuffle(password_chars)
        password = "".join(password_chars)

    else:
        raise TypeError("Unexpected input. Please try again entering either 'weak' or 'strong'.")
    return password

print(password_generator())