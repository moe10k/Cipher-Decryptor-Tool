import time

def autokey_vigenere_decrypt(ciphertext, keyword):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ''
    key_stream = list(keyword.upper())

    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in base_alphabet:
            is_upper = char.isupper()
            key_char = key_stream.pop(0)
            shift = base_alphabet.index(key_char)
            char_index = base_alphabet.index(char_upper)
            decrypted_index = (char_index - shift + 26) % 26
            decrypted_char = base_alphabet[decrypted_index]
            plaintext_char = decrypted_char if is_upper else decrypted_char.lower()
            plaintext += plaintext_char
            key_stream.append(decrypted_char)  # Add decrypted character to key stream
        else:
            plaintext += char

    return plaintext

def try_autokey_keys(ciphertext):
    key_file = '../keywords.txt'
    output_file = 'decrypted_output.txt'

    try:
        with open(key_file, 'r') as f:
            keys = sorted(set(line.strip().upper() for line in f if line.strip()))
    except FileNotFoundError:
        print(f"Error: '{key_file}' not found.")
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        for key in keys:
            if not key.isalpha():
                continue
            try:
                decrypted = autokey_vigenere_decrypt(ciphertext, key)
                out.write(f"{key} | {decrypted}\n")
            except Exception as e:
                out.write(f"{key} | ERROR: {e}\n")

    print(f"Autokey decryption (standard alphabet) results written to '{output_file}'")

# --- Run ---
start = time.time()

try:
    with open('../ciphertext.txt', 'r', encoding='utf-8') as f:
        ciphertext = f.read()
except FileNotFoundError:
    print("Error: '../ciphertext.txt' not found.")
    exit()

try_autokey_keys(ciphertext)

end = time.time()
elapsed = end - start
print(f"Autokey decryption complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")
