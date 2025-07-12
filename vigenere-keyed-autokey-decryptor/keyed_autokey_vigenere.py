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

def autokey_decrypt(ciphertext, keyword, keyed_alphabet):
    plaintext = ''
    key_stream = list(keyword.upper())
    keyed_alphabet = keyed_alphabet.upper()

    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in keyed_alphabet:
            is_upper = char.isupper()
            key_char = key_stream.pop(0)
            shift = keyed_alphabet.index(key_char)
            char_index = keyed_alphabet.index(char_upper)
            decrypted_index = (char_index - shift + len(keyed_alphabet)) % len(keyed_alphabet)
            decrypted_char = keyed_alphabet[decrypted_index]
            plaintext_char = decrypted_char if is_upper else decrypted_char.lower()
            plaintext += plaintext_char
            key_stream.append(decrypted_char)  # Append decrypted character to key stream
        else:
            plaintext += char
    return plaintext

def try_autokey_with_keyed_alphabets(ciphertext):
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
                try:
                    decrypted = autokey_decrypt(ciphertext, key, keyed_alphabet)
                    out.write(f"{key} | {decrypted}\n")
                except Exception as e:
                    out.write(f"{key} | ERROR: {e}\n")

    print(f"Autokey decryption results written to '{output_file}'")

start = time.time()

ciphertext = '../ciphertext.txt'

try_autokey_with_keyed_alphabets(ciphertext)

end = time.time()
elapsed = end - start
print(f"Autokey decryption complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")