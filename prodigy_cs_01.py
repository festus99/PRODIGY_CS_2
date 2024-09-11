#Function to encrypt the message
def encrypt(text, shift):
    result = ""  
    # Traverse through each character in the input text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # For characters that are not letters, we leave them unchanged
            result += char
    return result

#Function to decrypt the message
def decrypt(text, shift):
    result = "" 
    # Traverse through each character in the input text
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # For characters that are not letters, we leave them unchanged
            result += char
    return result

#User input for the message and the shift value is taken
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value (positive integer): "))

#Call the encrypt and decrypt functions
encrypted_message = encrypt(message, shift_value)
decrypted_message = decrypt(encrypted_message, shift_value)

#Output for the results
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
