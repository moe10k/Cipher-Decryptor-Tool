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


def vigenere_decrypt_custom(ciphertext, key, keyed_alphabet):
    plaintext = ''
    key_index = 0

    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in keyed_alphabet:
            is_upper = char.isupper()
            char_index = keyed_alphabet.index(char_upper)
            key_char = key[key_index % len(key)]
            shift = keyed_alphabet.index(key_char)
            decrypted_index = (char_index - shift + len(keyed_alphabet)) % len(keyed_alphabet)
            decrypted_char = keyed_alphabet[decrypted_index]
            plaintext += decrypted_char if is_upper else decrypted_char.lower()
            key_index += 1
        else:
            plaintext += char

    return plaintext


def try_keys_against_each_alphabet(ciphertext):
    key_file = '../key.txt'
    output_file = 'decrypt_output.txt'
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
        with open(key_file, 'r') as f:
            lines = sorted(set(line.strip() for line in f if line.strip()))
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

                decrypted = vigenere_decrypt_custom(ciphertext, key, keyed_alphabet)

                out.write(f"{key} | {decrypted}\n")

    print(f"Decryption results written to '{output_file}'")


start = time.time()

# Ciphertext to decrypt
try:
    with open('../ciphertext.txt', 'r', encoding='utf-8') as f:
        ciphertext = f.read()
except FileNotFoundError:
    print("Error: '../ciphertext.txt' not found.")
    exit()

# Run decryption attempts
try_keys_against_each_alphabet(ciphertext)

end = time.time()
elapsed = end - start
print(f"Decryption complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")