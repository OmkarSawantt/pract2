import string

# Function to encrypt using Vigenère cipher
def vigenere_encrypt(plain_text, key):
    alphabets = list(string.ascii_letters)
    cypher_text = []
    i = 0

    for x in plain_text:
        if x in alphabets:
            index = alphabets.index(x)
            key_index = alphabets.index(key[i % len(key)])
            ans = (index + key_index) % len(alphabets)
            cypher_text.append(alphabets[ans])
            i += 1
        else:
            cypher_text.append(x)

    return "".join(cypher_text)

# Function to decrypt using Vigenère cipher
def vigenere_decrypt(cypher_text, key):
    alphabets = list(string.ascii_letters)
    plain_text = []
    i = 0

    for x in cypher_text:
        if x in alphabets:
            index = alphabets.index(x)
            key_index = alphabets.index(key[i % len(key)])
            ans = (index - key_index) % len(alphabets)
            plain_text.append(alphabets[ans])
            i += 1
        else:
            plain_text.append(x)

    return "".join(plain_text)

# User inputs
plain_text = input("Enter Plain Text: ")
key = input("Enter Key: ")

# Encryption
encrypted_text = vigenere_encrypt(plain_text, key)
print("The Cypher text is:", encrypted_text)

# Decryption
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("The Decrypted text is:", decrypted_text)