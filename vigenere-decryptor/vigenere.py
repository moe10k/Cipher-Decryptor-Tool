def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext

def try_keys_from_file(ciphertext):
    key_file = '../key.txt'
    output_file = 'decrypt_output.txt'

    try:
        with open(key_file, 'r') as f:
            keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{key_file}' not found.")
        return

    with open(output_file, 'w') as out:
        for key in keys:
            decrypted = vigenere_decrypt(ciphertext, key)
            out.write(f"{key} | {decrypted}\n")

    print(f"Decryption results written to '{output_file}'")

# Hardcoded ciphertext
ciphertext = '../ciphertext.txt'

# Try all keys from key.txt and write to file
try_keys_from_file(ciphertext)
