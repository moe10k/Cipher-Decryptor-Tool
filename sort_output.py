import os
import re
import time
import sys
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0
start = time.time()

# Load common English words
with open('words.txt') as f:
    COMMON_WORDS = set(word.strip().lower() for word in f if word.strip())

def word_ratio(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    if not words:
        return 0
    return sum(1 for word in words if word in COMMON_WORDS) / len(words)

def is_english(text):
    try:
        return detect(text.strip()) == 'en'
    except:
        return False

def rank_legible_lines(input_path, output_path, top_n=100000):
    dictionary_scored = []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('=') or len(line.split()) < 4:
                continue
            ratio = word_ratio(line)
            if ratio > 0.3:
                dictionary_scored.append((ratio, line))

    dictionary_scored.sort(reverse=True, key=lambda x: x[0])
    top_candidates = dictionary_scored[:top_n]
    final_results = []

    for score, line in top_candidates:
        if is_english(line):
            final_results.append((score, line))

    with open(output_path, 'w', encoding='utf-8') as out:
        for score, line in final_results:
            out.write(f"[Score: {score:.2f}] {line}\n")

    print(f"Wrote {len(final_results)} filtered lines to '{output_path}'")
    elapsed = time.time() - start
    print(f"Ranking complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")

# Main flow
if __name__ == "__main__":
    folder = input("Enter folder name: ").strip()
    input_file = os.path.join(folder, 'decrypt_output.txt')
    output_file = os.path.join(folder, 'sorted_output.txt')

    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
    else:
        rank_legible_lines(input_file, output_file)
