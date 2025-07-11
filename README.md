# 🔐 Keyed Vigenère Decryptor

This script attempts to decrypt a ciphertext using a **keyed Vigenère cipher**, where both the alphabet and the key are derived from a list of keywords. It brute-forces combinations of keys and custom keyed alphabets from a provided wordlist.

## 📂 How It Works

1. `key.txt` contains a list of keywords (one per line).
2. Each word in the list is used to:
   - Generate a **custom alphabet** starting with the keyword.
   - Try every word in the list again as the Vigenère **key**.
3. Results are written to `decrypted_output.txt`.

## 🧪 Example

Given:

```plaintext
Ciphertext: Rc qipv jhx vld plson fhceuh itp jui gh qhzu dg sq xie dhw. U gbfl lf fluz pcag wrgkv zw, dinyg zw, qge gnvm L thx.

The script will try all permutations of custom alphabets and Vigenère keys from key.txt.

📄 File Structure:

keyed-vigenere-decryptor/
├── keyed_vigenere.py          # Main decryption script
├── key.txt                    # List of keywords used as alphabets and keys
└── decrypted_output.txt       # Output file with decryption attempts


🚀 Usage

python keyed_vigenere.py
Make sure key.txt is in the same directory.

🛠️ Customization
You can change the ciphertext by editing the ciphertext variable at the bottom of the script.

To enable or disable plaintext scoring (English word detection), comment/uncomment the relevant lines in try_keys_against_each_alphabet().

✅ Features
Uses keyed alphabets for decryption

Supports custom key lists

Flags likely English plaintext lines

Clean output format

📌 To Do
Add scoring and ranking system

Add CLI options (e.g., input file, verbose mode)

Optimize with multiprocessing for large key lists

Feel free to contribute or open issues!