def caesar_brute_force(text):
    text = text.upper()
    for shift in range(1, 26):
        decrypted = ""
        for char in text:
            if char.isalpha():
                shifted = (ord(char) - 65 - shift) % 26 + 65
                decrypted += chr(shifted)
            else:
                decrypted += char
        print(f"Shift {shift:2}: {decrypted}\n")

# --- Run the script ---
if __name__ == "__main__":
    input_text = input("Enter text to decrypt: ")
    print("\nTrying all 25 Caesar cipher shifts:\n")
    caesar_brute_force(input_text)
