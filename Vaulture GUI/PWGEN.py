import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """Function to generate a random password based on user preferences."""
    char_pool = ''  
    
    #Choosing the User's Preferences for whats in the password
    if use_uppercase:
        char_pool += string.ascii_uppercase  
    if use_lowercase:
        char_pool += string.ascii_lowercase  
    if use_digits:
        char_pool += string.digits  
    if use_symbols:
        char_pool += string.punctuation 
    
    if not char_pool: 
        print("Error: No character set selected. Please enable at least one option.")
        return None
    
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    """Main function to interact with the user and generate a password based on input."""
    print("Customizable Password Generator")
    length = int(input("Enter password length: "))  
    
    #Part where it calls the user's choices
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    if password: 
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":  
    main() 
