import string

def create_playfair_matrix(key):
    # Filter and prepare the key
    key = ''.join(filter(str.isalpha, key)).upper().replace('J', 'I')
    key = ''.join(sorted(set(key), key=key.index))
    
    matrix = list(key)
    for char in range(ord('A'), ord('Z') + 1):
        char = chr(char)
        if char not in key and char != 'J':
            matrix.append(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = ''.join(filter(str.isalpha, text.upper().replace('J', 'I')))
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            pairs.append(text[i] + text[i + 1])
            i += 2
        else:
            pairs.append(text[i] + 'X')
            i += 1
    return pairs

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def playfair_encrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])
    
    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    if c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_decrypt_pair(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])
    
    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    if c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def playfair_cipher(text, key, encrypt=True):
    matrix = create_playfair_matrix(key)
    pairs = preprocess_text(text)
    process_pair = playfair_encrypt_pair if encrypt else playfair_decrypt_pair
    return ''.join(process_pair(pair, matrix) for pair in pairs)

def main():
    key = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")
    
    encrypted = playfair_cipher(plaintext, key, encrypt=True)
    decrypted = playfair_cipher(encrypted, key, encrypt=False)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()