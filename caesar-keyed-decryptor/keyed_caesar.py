import string
import os
import time

def build_keyed_alphabet(key):
    key = key.upper()
    seen = set()
    cleaned_key = ''.join([ch for ch in key if ch.isalpha() and not (ch in seen or seen.add(ch))])
    base = ''.join([ch for ch in string.ascii_uppercase if ch not in cleaned_key])
    full_alphabet = (cleaned_key + base)[:26]  # Ensure exactly 26 characters
    return full_alphabet

def decrypt_with_keyed_caesar(ciphertext, shift, keyed_alphabet):
    shifted_alphabet = keyed_alphabet[shift:] + keyed_alphabet[:shift]
    normal_alphabet = string.ascii_uppercase
    decrypted = ""

    for char in ciphertext:
        upper_char = char.upper()
        if upper_char in shifted_alphabet:
            index = shifted_alphabet.index(upper_char)
            new_char = normal_alphabet[index]
            decrypted += new_char if char.isupper() else new_char.lower()
        else:
            decrypted += char

    return decrypted

def main():
    start = time.time()
    base_path = os.path.dirname(os.path.abspath(__file__))
    keyword_path = os.path.abspath(os.path.join(base_path, '../keywords.txt'))
    ciphertext_path = os.path.abspath(os.path.join(base_path, '..', 'ciphertext.txt'))
    output_path = os.path.join(base_path, 'decrypted_output.txt')

    # Load keywords
    try:
        with open(keyword_path, 'r') as f:
            keywords = sorted(set(line.strip().upper() for line in f if line.strip()))
    except FileNotFoundError:
        print(f"Error: '{keyword_path}' not found.")
        return

    # Load ciphertext
    try:
        with open(ciphertext_path, 'r', encoding='utf-8') as f:
            ciphertext = f.read().strip()
    except FileNotFoundError:
        print(f"Error: '{ciphertext_path}' not found.")
        return

    with open(output_path, 'w', encoding='utf-8') as out:
        for keyword in keywords:
            keyed_alphabet = build_keyed_alphabet(keyword)
            out.write(f"{'='*50}\n")
            out.write(f"KEY: {keyword} | ALPHABET: {keyed_alphabet}\n")
            out.write(f"{'='*50}\n")

            for shift in range(1, 26):
                decrypted = decrypt_with_keyed_caesar(ciphertext, shift, keyed_alphabet)
                out.write(f"Shift {shift}: {decrypted}\n")
            out.write("\n")

    elapsed = time.time() - start
    print(f"Decryption results written to '{output_path}'")
    print(f"Completed in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")

if __name__ == "__main__":
    main()
