# 🔐 Cipher Decryption Toolkit

This repository contains multiple Python scripts to decrypt ciphertexts using various classical ciphers, including Vigenère (keyed, autokey, progressive), Caesar, Atbash, and Beaufort variants.

Each decryption script attempts brute-force or dictionary-based decryption using provided wordlists and outputs possible plaintext candidates. A centralized ranking script (`sort_vigenere.py`) is used to filter and score the most legible outputs.

---

## ⚙️ How It Works

Each script:
- Takes a ciphertext (either hardcoded or via `ciphertext.txt`)
- Uses keywords from `key.txt` as either:
  - Cipher **keys**
  - Custom **keyed alphabets**
- Outputs possible decrypted results to `decrypt_output.txt`

Then you can run the ranking tool:


```bash
python sort_vigenere.py
```

You'll be prompted to enter a folder name (e.g., vigenere-keyed-decryptor), and it will:

- Read from `decrypt_output.txt` inside that folder
- Write ranked results to `ranked_output.txt` in the same folder


## 📌 Features
✅ Supports multiple cipher variations (classic and keyed)

✅ Modular structure for easy experimentation

✅ Centralized scoring and filtering with language detection

✅ Works with large keylists (tested with 3000+ keys)

✅ Simple CLI prompt for scoring decrypted output

✅ Outputs ranked plaintexts with word ratio + language check

## 🧪 Example
Given:
```bash
Ciphertext: Rc qipv jhx vld plson fhceuh itp jui gh qhzu dg sq xie dhw. U gbfl lf fluz pcag wrgkv zw, dinyg zw, qge gnvm L fhx.
```

The keyed_vigenere.py script will try every key and keyed alphabet combination from key.txt and output results. Then:
```bash
python sort_vigenere.py
```

Input:
```bash
vigenere-keyed-decryptor
```

```bash
Output:
vigenere-keyed-decryptor/ranked_output.txt with scored lines
```

## 🛠️ Customization
- Add or modify words in `key.txt` (for decryption attempts) and `words.txt` (for scoring)
- Replace hardcoded ciphertext or use `ciphertext.txt` for batch testing
- Modify scoring thresholds in `sort_vigenere.py` (e.g., `word_ratio`, `language_match`)
- Tweak filters (e.g., line skipping with `startswith('=')`, minimum word count)

## 🚀 Future Plans
- Add multiprocessing for faster brute-force runs
- CLI flags for all decryption scripts
- Web UI (e.g., Streamlit or Flask)
- Encrypted file input support

## 🤝 Contributions
Feel free to fork, modify, or submit pull requests. Bug reports and suggestions are welcome!

## 🧠 Inspiration
Built as a hands-on cryptography exploration project, focused on classical ciphers and brute-force techniques with modern filtering.