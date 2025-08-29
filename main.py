import sys
from stats import count_words, get_char_counts, get_sorted_char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    num_words = count_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = get_sorted_char_counts(char_counts)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============ END =============")

main()

