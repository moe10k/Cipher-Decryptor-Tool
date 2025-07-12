import time

def create_keyed_alphabet(keyword, base_alphabet):
    seen = set()
    keyed = []

    for char in keyword:
        if char not in seen and char in base_alphabet:
            seen.add(char)
            keyed.append(char)

    for char in base_alphabet:
        if char not in seen:
            keyed.append(char)

    return ''.join(keyed)

def shift_key_once(key, alphabet):
    shifted = ''
    for char in key:
        idx = alphabet.index(char.upper())
        shifted += alphabet[(idx + 1) % len(alphabet)]
    return shifted

def generate_progressive_keystream(base_key, length, alphabet):
    keystream = ''
    current_key = base_key.upper()
    while len(keystream) < length:
        for char in current_key:
            if len(keystream) >= length:
                break
            keystream += char
        current_key = shift_key_once(current_key, alphabet)
    return keystream

def progressive_keyed_vigenere_decrypt(ciphertext, base_key, keyed_alphabet):
    keystream = generate_progressive_keystream(base_key, len(ciphertext), keyed_alphabet)
    plaintext = ''
    key_index = 0

    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in keyed_alphabet:
            is_upper = char.isupper()
            cipher_index = keyed_alphabet.index(char_upper)
            key_char = keystream[key_index]
            shift = keyed_alphabet.index(key_char)
            decrypted_index = (cipher_index - shift + len(keyed_alphabet)) % len(keyed_alphabet)
            decrypted_char = keyed_alphabet[decrypted_index]
            plaintext += decrypted_char if is_upper else decrypted_char.lower()
            key_index += 1
        else:
            plaintext += char
            key_index += 1  # Still consume the keystream
    return plaintext

def try_keys_with_progressive_keyed_alphabet(ciphertext):
    key_file = '../key.txt'
    output_file = 'decrypt_output.txt'
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        with open(key_file, 'r') as f:
            lines = sorted(set(line.strip().upper() for line in f if line.strip()))
    except FileNotFoundError:
        print(f"Error: '{key_file}' not found.")
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        for alphabet_keyword in lines:
            keyed_alphabet = create_keyed_alphabet(alphabet_keyword, base_alphabet)
            out.write(f"{'='*50}\n")
            out.write(f"{alphabet_keyword} | {keyed_alphabet}\n")
            out.write(f"{'='*50}\n")

            for key in lines:
                if not all(c in keyed_alphabet for c in key):
                    continue
                decrypted = progressive_keyed_vigenere_decrypt(ciphertext, key, keyed_alphabet)
                out.write(f"{key} | {decrypted}\n")

    print(f"Decryption results written to '{output_file}'")

# --- Main Run ---
start = time.time()

try:
    with open('../ciphertext.txt', 'r', encoding='utf-8') as f:
        ciphertext = f.read()
except FileNotFoundError:
    print("Error: '../ciphertext.txt' not found.")
    exit()

try_keys_with_progressive_keyed_alphabet(ciphertext)

end = time.time()
elapsed = end - start
print(f"Decryption complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")
