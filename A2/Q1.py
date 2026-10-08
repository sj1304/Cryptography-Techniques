def caesar_encrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(base) + 3) % 26 + ord(base))
        else:
            result += ch
    return result

def caesar_decrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(base) + (-3)) % 26 + ord(base))
        else:
            result += ch
    return result


print("Encrypt: ",caesar_encrypt("abc"))
print("Decrypt: ",caesar_decrypt("def"))
