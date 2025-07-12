def shift_key_once(key):
    shifted = ''
    for char in key:
        shifted += chr((ord(char.upper()) - ord('A') + 1) % 26 + ord('A'))
    return shifted

def generate_progressive_keystream(base_key, length):
    keystream = ''
    current_key = base_key.upper()
    while len(keystream) < length:
        for char in current_key:
            if len(keystream) >= length:
                break
            keystream += char
        current_key = shift_key_once(current_key)
    return keystream

def progressive_vigenere_decrypt(ciphertext, base_key):
    keystream = generate_progressive_keystream(base_key, len(ciphertext))
    plaintext = ''
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            k = keystream[key_index]
            shift = ord(k) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
            key_index += 1  # Non-alpha chars still consume keystream
    return plaintext

def try_keys_from_file(ciphertext):
    key_file = '../keywords.txt'
    output_file = 'decrypted_output.txt'

    try:
        with open(key_file, 'r') as f:
            keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{key_file}' not found.")
        return

    with open(output_file, 'w') as out:
        for key in keys:
            decrypted = progressive_vigenere_decrypt(ciphertext, key)
            out.write(f"{key} | {decrypted}\n")

    print(f"Progressive Vigenere decryption results written to '{output_file}'")

# Read ciphertext from file
ciphertext_file = '../ciphertext.txt'
try:
    with open(ciphertext_file, 'r') as f:
        ciphertext = f.read()
except FileNotFoundError:
    print(f"Error: '{ciphertext_file}' not found.")
    exit()

# Run
try_keys_from_file(ciphertext)
