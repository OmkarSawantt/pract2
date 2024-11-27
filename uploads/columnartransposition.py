def columnar_transposition_encrypt(text, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = -(-len(text) // num_cols)  # Ceiling division
    padded_text = text.ljust(num_cols * num_rows)
    grid = [padded_text[i:i + num_cols] for i in range(0, len(padded_text), num_cols)]
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    ciphertext = ''.join(''.join(grid[row][col] for row in range(num_rows)) for col in key_order)
    
    return ciphertext

def columnar_transposition_decrypt(ciphertext, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = -(-len(ciphertext) // num_cols)  # Ceiling division
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    index = 0
    
    for col in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                grid[row][col] = ciphertext[index]
                index += 1

    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext.rstrip()

def main():
    text = input("Enter the plaintext: ").replace(" ", "").strip()
    key = input("Enter the key: ").strip()
    
    encrypted_text = columnar_transposition_encrypt(text, key)
    decrypted_text = columnar_transposition_decrypt(encrypted_text, key)
    
    print(f"Encrypted text: {encrypted_text}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()