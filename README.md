# 🛡️ PRODIGY_CS_02 - Pixel Manipulation for Image Encryption

## 📌 Overview
This project is a simple image encryption tool that performs **pixel manipulation** to encrypt and decrypt images. It uses basic operations like **XOR transformations** to modify pixel values and protect image data.

## ✨ Features
- 🔒 Encrypt images using pixel-level transformations
- 🔓 Decrypt images with the same key to restore the original
- 🖼️ Supports both RGB and grayscale images
- 🐍 Built with Python, using Pillow and NumPy

## 🛠️ Technologies Used
- Python
- Pillow (PIL)
- NumPy

## 🚀 Usage
```python
from encryption import encrypt_image
from decryption import decrypt_image

# Encrypt an image
encrypt_image("original.png", "encrypted.png", key=123)

# Decrypt the image
decrypt_image("encrypted.png", "decrypted.png", key=123)

