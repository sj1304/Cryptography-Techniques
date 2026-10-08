import hashlib
import base64
import cryptocode


def hash_message(message):
    return hashlib.sha256(message.encode()).hexdigest()


def base64_encode(message):
    return base64.b64encode(message.encode()).decode()

def base64_decode(encoded):
    return base64.b64decode(encoded.encode()).decode()

def encrypt_with_cryptocode(message, secret):
    return cryptocode.encrypt(message, secret)

def decrypt_with_cryptocode(encrypted, secret):
    return cryptocode.decrypt(encrypted, secret)

def unit_v_demo():
    message = "SecureMessage123"
    secret = "mysecretkey"

    hashed = hash_message(message)

    encoded_b64 = base64_encode(message)
    decoded_b64 = base64_decode(encoded_b64)

    encrypted_crypto = encrypt_with_cryptocode(message, secret)
    decrypted_crypto = decrypt_with_cryptocode(encrypted_crypto, secret)

    print("Original Message:", message)
    print("\n--- Hashlib (SHA256) ---")
    print("Hashed:", hashed)

    print("\n--- Base64 ---")
    print("Encoded:", encoded_b64)
    print("Decoded:", decoded_b64)

    print("\n--- Cryptocode ---")
    print("Encrypted:", encrypted_crypto)
    print("Decrypted:", decrypted_crypto)


unit_v_demo()
