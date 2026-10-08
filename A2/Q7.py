import rsa

(public_key, private_key) = rsa.newkeys(512)

message = "HelloSecureWorld"
encrypted_rsa = rsa.encrypt(message.encode(), public_key)


decrypted_rsa = rsa.decrypt(encrypted_rsa, private_key).decode()


def rsa_demo():
    print("Original Message:", message)
    print("Encrypted RSA:", encrypted_rsa)
    print("Decrypted RSA:", decrypted_rsa)


rsa_demo()
