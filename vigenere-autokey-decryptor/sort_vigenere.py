import re
import time
from langdetect import detect, DetectorFactory

# Fix randomness in langdetect
DetectorFactory.seed = 0

# Start timer
start = time.time()

# Load common English words from words.txt
with open('../words.txt') as f:
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

def rank_legible_lines(input_file, output_file, top_n=100000):
    dictionary_scored = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Skip empty or junk lines
            if not line or line.startswith('=') or len(line.split()) < 4:
                continue

            ratio = word_ratio(line)
            if ratio > 0.3:  # adjust this threshold as needed
                dictionary_scored.append((ratio, line))

    # Sort by dictionary ratio descending
    dictionary_scored.sort(reverse=True, key=lambda x: x[0])

    # Apply langdetect only to top N lines
    top_candidates = dictionary_scored[:top_n]
    final_results = []

    for score, line in top_candidates:
        if is_english(line):
            final_results.append((score, line))

    #for score, line in top_candidates:
    #    final_results.append((score, line))  # Temporarily bypass langdetect

    # Save to output
    with open(output_file, 'w', encoding='utf-8') as out:
        for score, line in final_results:
            out.write(f"[Score: {score:.2f}] {line}\n")

    print(f"Wrote {len(final_results)} filtered lines to '{output_file}'")

# Run
rank_legible_lines('decrypt_output.txt', 'ranked_output.txt')

# End timer
elapsed = time.time() - start
print(f"Ranking complete in {elapsed:.2f} seconds ({elapsed/60:.2f} minutes)")
