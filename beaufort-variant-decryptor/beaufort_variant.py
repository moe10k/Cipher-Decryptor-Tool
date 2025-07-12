def variant_beaufort_decrypt(ciphertext, key):
    plaintext = ''
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                c_val = ord(char) - ord('A')
                p_val = (c_val - shift + 26) % 26
                decrypted_char = chr(p_val + ord('A'))
            else:
                c_val = ord(char) - ord('a')
                p_val = (c_val - shift + 26) % 26
                decrypted_char = chr(p_val + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext

def try_keys_from_file(ciphertext):
    key_file = '../keydictionary.txt'
    output_file = 'decrypted_output.txt'

    try:
        with open(key_file, 'r') as f:
            keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{key_file}' not found.")
        return

    with open(output_file, 'w') as out:
        for key in keys:
            decrypted = variant_beaufort_decrypt(ciphertext, key)
            out.write(f"{key} | {decrypted}\n")

    print(f"Variant Beaufort decryption results written to '{output_file}'")

# Hardcoded ciphertext
ciphertext = '../ciphertext.txt'

# Try all keys from keydictionary.txt and write to file
try_keys_from_file(ciphertext)
