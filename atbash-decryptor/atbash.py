def atbash_cipher(text):
    text = text.upper()
    decrypted = ""
    for char in text:
        if char.isalpha():
            mirrored = 90 - (ord(char) - 65)  # 90 = ord('Z'), 65 = ord('A')
            decrypted += chr(mirrored)
        else:
            decrypted += char
    print(f"Atbash Decryption: {decrypted}")

# --- Run the script ---
if __name__ == "__main__":
    input_text = input("Enter text to decrypt using Atbash: ")
    atbash_cipher(input_text)