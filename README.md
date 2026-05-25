# 🔐 Secure File Sharing Using RC6 Encryption & Image Steganography

A secure file sharing system developed using **Python, Flask, RC6 Encryption, and Image Steganography** to protect sensitive data during transmission. This project encrypts files using the **RC6 cryptographic algorithm** and securely hides the encrypted data inside PNG images using **Least Significant Bit (LSB) Steganography**.

The system ensures **confidentiality, security, and hidden transmission of files** by combining encryption with steganography techniques.

---

## 📌 Project Overview

Traditional file sharing methods can expose sensitive information to unauthorized users. To solve this problem, this project implements a secure mechanism where:

1. Files are encrypted using the **RC6 encryption algorithm**
2. Encrypted data is hidden inside an image
3. The receiver extracts the hidden encrypted data
4. The file is decrypted back to its original format

This provides an additional security layer and makes data transmission more secure.

---

## ✨ Features

✅ File Encryption using RC6 Algorithm  
✅ Secure File Decryption  
✅ Image Steganography using PNG Images  
✅ Hide Files Inside Images  
✅ Extract Hidden Data from Images  
✅ Flask-Based Web Interface  
✅ Secure File Recovery  
✅ User-Friendly Interface  
✅ Fast Processing and Secure Communication

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| Flask | Web Framework |
| OpenCV | Image Processing |
| RC6 Algorithm | File Encryption |
| Steganography | Hidden Data Transmission |
| HTML/CSS | Frontend Interface |

---

## 🧠 System Workflow

### Encryption Process
1. User uploads a file
2. User selects a PNG cover image
3. File is encrypted using **RC6 Encryption**
4. Encrypted data is embedded into the image
5. Stego image is generated successfully

### Decryption Process
1. User uploads the stego image
2. Hidden encrypted data is extracted
3. RC6 decryption is applied
4. Original file is recovered successfully

---

## 📂 Project Structure

```txt
Secure-File-Sharing-Steganography/
│── app.py
│── templates/
│── uploads/
│── stego/
│── encrypted/
│── decrypted/
│── extracted/
│── requirements.txt
│── README.md
│── .gitignore
