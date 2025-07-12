import string

def build_keyed_alphabet(key):
    key = key.upper()
    seen = set()
    cleaned_key = ''.join([ch for ch in key if ch.isalpha() and not (ch in seen or seen.add(ch))])
    base = ''.join([ch for ch in string.ascii_uppercase if ch not in cleaned_key])
    return cleaned_key + base

def decrypt_with_keyed_caesar(ciphertext, shift, keyed_alphabet):
    shifted_alphabet = keyed_alphabet[shift:] + keyed_alphabet[:shift]
    normal_alphabet = string.ascii_uppercase
    decrypted = ""

    for char in ciphertext:
        upper_char = char.upper()
        if upper_char in shifted_alphabet:
            index = shifted_alphabet.index(upper_char)
            new_char = normal_alphabet[index]
            # preserve original casing
            decrypted += new_char if char.isupper() else new_char.lower()
        else:
            decrypted += char  # keep punctuation/space

    return decrypted

def main():
    key = input("Enter the keyword: ").strip()
    ciphertext = input("Enter the ciphertext: ").strip()

    keyed_alphabet = build_keyed_alphabet(key)
    print("\n--- All 25 Shifts ---")
    for shift in range(1, 26):
        plaintext = decrypt_with_keyed_caesar(ciphertext, shift, keyed_alphabet)
        print(f"\nShift {shift}:\n{plaintext}")

if __name__ == "__main__":
    main()