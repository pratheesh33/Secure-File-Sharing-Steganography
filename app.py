import os
import cv2
from flask import Flask, render_template, request, send_from_directory, flash

# ================= SETUP =================
app = Flask(__name__)
app.secret_key = "final-stego-rc6"

BASE = os.path.dirname(__file__)
UPLOAD = os.path.join(BASE, "uploads")
STEGO = os.path.join(BASE, "stego")
DECRYPTED = os.path.join(BASE, "decrypted")

for d in [UPLOAD, STEGO, DECRYPTED]:
    os.makedirs(d, exist_ok=True)

KEY = b"1234567890ABCDEF"  # 16-byte RC6 key

# ================= RC6 =================
def rol(x, y): return ((x << (y & 31)) | (x >> (32 - (y & 31)))) & 0xFFFFFFFF
def ror(x, y): return ((x >> (y & 31)) | (x << (32 - (y & 31)))) & 0xFFFFFFFF

def key_schedule(key):
    r = 20
    P, Q = 0xB7E15163, 0x9E3779B9
    L = [int.from_bytes(key[i:i+4], 'big') for i in range(0, len(key), 4)]
    S = [(P + i * Q) & 0xFFFFFFFF for i in range(2*r + 4)]
    A = B = i = j = 0
    for _ in range(3 * max(len(S), len(L))):
        A = S[i] = rol((S[i] + A + B) & 0xFFFFFFFF, 3)
        B = L[j] = rol((L[j] + A + B) & 0xFFFFFFFF, (A + B))
        i = (i + 1) % len(S)
        j = (j + 1) % len(L)
    return S

def rc6_encrypt(data, key):
    S = key_schedule(key)
    pad = 8 - len(data) % 8
    data += bytes([pad]) * pad
    out = b''
    for i in range(0, len(data), 8):
        A = int.from_bytes(data[i:i+4], 'big') + S[0]
        B = int.from_bytes(data[i+4:i+8], 'big') + S[1]
        for r in range(1, 21):
            A = (rol(A ^ B, B) + S[2*r]) & 0xFFFFFFFF
            B = (rol(B ^ A, A) + S[2*r+1]) & 0xFFFFFFFF
        A = (A + S[42]) & 0xFFFFFFFF
        B = (B + S[43]) & 0xFFFFFFFF
        out += A.to_bytes(4,'big') + B.to_bytes(4,'big')
    return out

def rc6_decrypt(data, key):
    S = key_schedule(key)
    out = b''
    for i in range(0, len(data), 8):
        A = int.from_bytes(data[i:i+4], 'big') - S[42]
        B = int.from_bytes(data[i+4:i+8], 'big') - S[43]
        for r in range(20, 0, -1):
            B = ror((B - S[2*r+1]) & 0xFFFFFFFF, A) ^ A
            A = ror((A - S[2*r]) & 0xFFFFFFFF, B) ^ B
        A = (A - S[0]) & 0xFFFFFFFF
        B = (B - S[1]) & 0xFFFFFFFF
        out += A.to_bytes(4,'big') + B.to_bytes(4,'big')
    return out[:-out[-1]]
if __name__ == "__main__":
    app.run(debug=True,port="8081")
