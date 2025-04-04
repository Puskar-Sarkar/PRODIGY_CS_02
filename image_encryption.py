import os
from PIL import Image

def encrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_r = (r + 50) % 256
            new_g = (g + 100) % 256
            new_b = (b + 150) % 256
            pixels[x, y] = (new_r, new_g, new_b)
    img.save(output_image)
    print(f"Image encrypted and saved to {output_image}")

def decrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_r = (r - 50) % 256
            new_g = (g - 100) % 256
            new_b = (b - 150) % 256
            pixels[x, y] = (new_r, new_g, new_b)
    img.save(output_image)
    print(f"Image decrypted and saved to {output_image}")
    
if __name__ == "__main__":
    input_image_path = "input_image/input_image.png"
    encrypted_image_path = "encrypted_images/encrypted_image.png"
    decrypted_image_path = "decrypted_images/decrypted_image.png"
    os.makedirs("encrypted_images", exist_ok=True)
    os.makedirs("decrypted_images", exist_ok=True)
    encrypt_image(input_image_path, encrypted_image_path)
    decrypt_image(encrypted_image_path, decrypted_image_path)