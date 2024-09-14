from PIL import Image
import random

# Load the image
def load_image(image_path):
    img = Image.open(image_path)
    return img

# Encrypt the image by shifting pixel values
def encrypt_image(image, key):
    encrypted_img = image.copy()
    pixels = encrypted_img.load()
    width, height = encrypted_img.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Apply simple mathematical operation (e.g., add key to each pixel value)
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    return encrypted_img

# Decrypt the image by reversing the operation
def decrypt_image(encrypted_image, key):
    decrypted_img = encrypted_image.copy()
    pixels = decrypted_img.load()
    width, height = decrypted_img.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Reverse the operation by subtracting the key
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    return decrypted_img

# Example usage
key = 50  # Encryption key
image_path = 'download.png'
img = load_image(image_path)
encrypted = encrypt_image(img, key)
encrypted.save('encrypted_image.png')

# To decrypt
decrypted = decrypt_image(encrypted, key)
decrypted.save('decrypted_image.png')
