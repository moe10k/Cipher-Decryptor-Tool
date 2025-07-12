# 🔐 Cipher Decryption Toolkit

This repository contains multiple Python scripts to decrypt ciphertexts using various classical ciphers, including Vigenère (keyed, autokey, progressive), Caesar, Atbash, and Beaufort variants.

Each decryption script attempts brute-force or dictionary-based decryption using provided wordlists and outputs possible plaintext candidates. A centralized ranking script (`sort_vigenere.py`) is used to filter and score the most legible outputs.

This was created with the intent and ultimate goal of decrypting the unsolved ciphers from Black ops 3 Zombies.

---

## ⚙️ How It Works
In root folder, create:

- `keywords.txt`
   - You can go to this spreadsheet and copy and paste all the keywords to `keywords.txt`
   - Link to spreadsheet: https://docs.google.com/spreadsheets/d/1R79Y2xCuyJf9sYHrPODwJEcLWe-yxU8McP22n97p5p4/edit?usp=sharing
   - This is the list of keywords each cipher will use to iterate over as keys or to create custom/keyed alphabets

- `dictionary.txt`
   - you can download this .txt file of a list of words and copy and paste it to your `dictionary.txt`
   - Link to file: https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
   - `sort_output.py` will use this `dictionary.txt file` as a reference when sorting/ranking the decrytions as real english sentences

Each script:
- Takes a ciphertext via `ciphertext.txt` that is also in your root folder
- Uses keywords from `key.txt` as keys and/or keyed alphabets
- Outputs all possible decrypted results to `decrypted_output.txt`

Then you can run the sorting tool:
```bash
python sort_output.py
```

You'll be prompted to enter a folder name (e.g., vigenere-decryptor), and it will:
- Read from `decrypted_output.txt` inside that folder
- Write the ranked/sorted results to `sorted_output.txt` in the same folder


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
- Web UI (e.g., Streamlit or Flask)
- Add multiprocessing for faster brute-force runs
- CLI flags for all decryption scripts
- Encrypted file input support

## 🤝 Contributions
- Feel free to fork, modify, or submit pull requests. Bug reports and suggestions are welcome!

## 🧠 Inspiration
- Built as a hands-on cryptography exploration project, focused on classical ciphers and brute-force techniques with modern filtering.
- Lets solve those ciphers