import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """Function to generate a random password based on user preferences."""
    char_pool = ''  # Initializing an empty string to store selected character sets
    
    # Adding selected character sets to the character pool, asks if use uppercase/lowercase letters, how many numbers, and what symbols.
    if use_uppercase:
        char_pool += string.ascii_uppercase  
    if use_lowercase:
        char_pool += string.ascii_lowercase  
    if use_digits:
        char_pool += string.digits  
    if use_symbols:
        char_pool += string.punctuation 
    
    if not char_pool:  # If no character set is selected, display an error message
        print("Error: No character set selected. Please enable at least one option.")
        return None  # Return None if no characters are available for selection
    
    # Generating the password by randomly selecting characters from the pool
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    """Main function to interact with the user and generate a password based on input."""
    print("Customizable Password Generator")
    length = int(input("Enter password length: "))  # Taking input for password length
    
    # Taking user preferences for including different character types
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Generating the password based on user input
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    if password:  # Checking if a password was successfully generated
        print(f"\nGenerated Password: {password}")  # Displaying the generated password

if __name__ == "__main__":  # Ensuring the script runs only if executed directly
    main()  # Calling the main function to start the program
