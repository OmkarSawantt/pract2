def poly_cipher(text, key, encrypt=True):
    key = key.upper()
    text = text.upper()
    key_length = len(key)
    result = []

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if not encrypt:
                shift = -shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

# User inputs
plain_text = input("Enter Text: ")
key = input("Key: ")

# Encryption and Decryption
encrypted = poly_cipher(plain_text, key, encrypt=True)
decrypted = poly_cipher(encrypted, key, encrypt=False)

# Output results
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)